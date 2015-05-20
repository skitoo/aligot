# -*- coding: utf-8 -*-


from rest_framework import permissions

from .models import Note, NoteBook


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user


class IsNoteBookOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.notebook.created_by == request.user

    def has_permission(self, request, view):
        notebook_id = request.data.get('notebook')
        if notebook_id:
            notebook = NoteBook.objects.get(pk=notebook_id)
            return notebook and notebook.created_by == request.user
        return True


class IsNoteOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.note.created_by == request.user

    def has_permission(self, request, view):
        note_id = request.data.get('note')
        if note_id:
            note = Note.objects.get(pk=note_id)
            return note and note.created_by == request.user
        return True
