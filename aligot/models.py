# -*- coding: utf-8 -*-

import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):

    class Meta(object):
        unique_together = ('email', )


class NoteBook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='notebooks')
    created_at = models.DateTimeField(auto_now_add=True)

    def note_count(self):
        return self.notes.count()

    def __str__(self):
        return self.title

    def __repr__(self):
        return str(self)


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    starred = models.BooleanField(default=False)
    crypted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='notes')
    notebook = models.ForeignKey(NoteBook, related_name='notes')

    def __str__(self):
        return self.title

    def __repr__(self):
        return str(self)


class NoteRevision(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    note = models.ForeignKey(Note, related_name='revisions')

    def __str__(self):
        return '%s#%s' % (self.note.title, self.created_at)

    def __repr__(self):
        return str(self)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
