# -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework import mixins, generics
from .models import NoteBook
from .serializers import NoteBookSerializer


def index(request):
    return render(request, 'index.html')



