# -*- coding: utf-8 -*-

from django.shortcuts import render


def index(request, page=None):
    return render(request, 'index.html')
