# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Note, NoteBook, NoteRevision


class NoteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteBook


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note


class NoteRevisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteRevision
