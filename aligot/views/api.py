# -*- coding: utf-8 -*-

import logging

from rest_framework import generics, permissions

from ..models import Note, NoteBook, User
from ..permissions import IsNoteBookOwner, IsOwner
from ..serializers import NoteBookSerializer, NoteSerializer, UserSerializer

logger = logging.getLogger(__name__)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NoteBookList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner,)
    serializer_class = NoteBookSerializer

    def get_queryset(self):
        return NoteBook.objects.filter(created_by=self.request.user)


class NoteBookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner,)
    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializer


class NoteList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner, IsNoteBookOwner,)
    serializer_class = NoteSerializer

    def get_queryset(self):
        query = Note.objects.filter(created_by=self.request.user)
        notebook = self.kwargs.get('notebook')
        return query.filter(notebook=notebook) if notebook else query


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
