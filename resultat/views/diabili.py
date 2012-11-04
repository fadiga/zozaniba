#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fadiga

import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django import forms


from nosmsd.models import Inbox, SentItems
from resultat.models import *


class DiabiliForm(forms.ModelForm):

    class Meta:
        model = QuestionReponse

    def __init__(self, request, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, *args, **kwargs):
        return forms.ModelForm.save(self, *args, **kwargs)


def diabili(request):

    context = {"category": 'diabili'}

    nonresponse = QuestionReponse.objects.filter(is_amswer=False)

    context.update({"nonresponse": nonresponse})
    form = DiabiliForm(request, request.POST)

    context.update({'form': form})
    return render(request, 'diabili.html', context)


def getask(*args, **kwargs):

    data = {'asks': [ask.to_dict() for ask in
                    QuestionReponse.objects.filter(is_amswer=False)],
            'nbr_inbox': Inbox.objects.count(),
            'nbr_send': SentItems.objects.count()}

    return   HttpResponse(json.dumps(data))

def answer(request):

    print  request.form.get('group_name', None)