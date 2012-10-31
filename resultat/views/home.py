#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fadiga

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


from nosmsd.models import Inbox, SentItems


def home(request):

    context = {"category": 'home'}

    return render(request, 'home.html', context)