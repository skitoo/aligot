# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class NoteBook(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name='notebooks')
    create_at = models.DateTimeField(auto_now_add=True)


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', null=True)
    owner = models.ForeignKey(User, related_name='notes')
    starred = models.BooleanField(default=False)
    removed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(User)
