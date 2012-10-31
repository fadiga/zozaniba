#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fadiga

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


from nosmsd.models import Inbox, SentItems


def dashboard(request):

    context = {"category": 'dashboard'}

    return render(request, 'dashboard.html', context)