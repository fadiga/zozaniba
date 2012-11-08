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


class DiabiliForm(forms.ModelForm):

    class Meta:
        model = QuestionReponse

    def __init__(self, request, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, *args, **kwargs):
        return forms.ModelForm.save(self, *args, **kwargs)


def diabili(request, *args, **kwargs):

    context = {"category": 'diabili'}

    nonresponse = QuestionReponse.objects.filter(is_amswer=False)

    context.update({"nonresponse": nonresponse})
    form = DiabiliForm(request, request.POST)

    print "iittttttttttttttttttiiii"
    if request.method == "POST":
        form = DiabiliForm(request, request.POST)
        print "hhhhhhh"

    context.update({'form': form})
    return render(request, 'diabili.html', context)


def getask(*args, **kwargs):

    data = {'asks': [ask.to_dict() for ask in
                    QuestionReponse.objects.filter(is_amswer=False)],
            'nbr_inbox': Inbox.objects.count(),
            'nbr_send': SentItems.objects.count()}

    return HttpResponse(json.dumps(data))


def answer(request):
    print "iiiiiiiiiiiiiiiii"
    # answer = request.form.get('answer', None)
