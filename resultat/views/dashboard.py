#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fadiga

from django.shortcuts import render


def dashboard(request):

    context = {"category": 'dashboard'}

    return render(request, 'dashboard.html', context)
