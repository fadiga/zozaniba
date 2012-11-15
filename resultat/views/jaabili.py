#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fadiga

import json
import sqlite3

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django import forms


from nosmsd.models import Inbox, SentItems
from resultat.models import QuestionReponse

SUCCESS = u'success'
INFO = u'info'
WARNING = u'warning'
ERROR = u'error'


def dict_return(data, level, message, message_html=None):
    data.update({'return': level,
                 'return_text': message})
    if message_html:
        data.update({'return_html': message_html})


class jaabiliForm(forms.ModelForm):

    class Meta:
        model = QuestionReponse

    def __init__(self, request, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, *args, **kwargs):
        return forms.ModelForm.save(self, *args, **kwargs)


def jaabili(request, *args, **kwargs):

    context = {"category": 'jaabili'}

    nonresponse = QuestionReponse.objects.filter(is_amswer=False)

    context.update({"nonresponse": nonresponse})
    form = jaabiliForm(request)

    if request.method == "POST":
        print request.POST.values()

    context.update({'form': form})
    return render(request, 'jaabili.html', context)


def getask(*args, **kwargs):

    data = {'asks': [ask.to_dict() for ask in
                     QuestionReponse.objects.filter(is_amswer=False)],
            'nbr_inbox': Inbox.objects.count(),
            'nbr_send': SentItems.objects.count()}

    return HttpResponse(json.dumps(data))


def answer(request):

    if request.method == "POST":
        answer = request.form.get('answer', None)
        print answer

    data = {}
    subst = {'group': answer}

    if not answer:
        dict_return(data, WARNING, u"Veuillez saisir un nom de groupe",
                    message_html=u"Veuillez saisir un nom de"
                                 u"<strong> groupe</strong>.")

        return HttpResponse(json.dumps(data))

    try:
        ask_anw = QuestionReponse(name=answer)
        ask_anw.save()
        dict_return(data, SUCCESS,
                    u"%(group)s a été ajouté avec succès." % subst,
                    message_html=u"<strong>%(group)s</strong> "
                                 u"a été ajouté avec succès." % subst)
    except sqlite3.IntegrityError:
        dict_return(data, INFO,
                    u"%(group)s existe déjà." % subst,
                    message_html=u"<strong>%(group)s</strong> existe déjà."
                                 % subst)
    except Exception as e:
        subst.update({'err': e.message})
        dict_return(data, ERROR,
                    u"Impossible d'enregistrer le groupe %(group)s : %(err)r" % subst,
                    message_html=u"Impossible d'enregistrer le groupe "
                                 u"<strong>%(group)s</strong><br />"
                                 u"<em>%(err)r</em>" % subst)

    return HttpResponse(json.dumps(data))
