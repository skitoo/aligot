# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class NoteBook(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='notebooks')
    created_at = models.DateTimeField(auto_now_add=True)


class Note(models.Model):
    title = models.CharField(max_length=255)
    starred = models.BooleanField(default=False)
    crypted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='notes')
    notebook = models.ForeignKey(NoteBook, related_name='notes')


class NoteRevision(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    note = models.ForeignKey(Note, related_name='revisions')
