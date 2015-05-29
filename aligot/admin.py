# coding: utf-8

from django.contrib import admin

from .models import Note, NoteBook, NoteRevision, User

admin.site.register(User)
admin.site.register(NoteBook)
admin.site.register(Note)
admin.site.register(NoteRevision)
