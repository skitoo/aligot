# -*- coding: utf-8 -*-

import logging

from rest_framework import generics, permissions

from ..models import Note, NoteBook, NoteRevision, User
from ..permissions import IsNoteBookOwner, IsNoteOwner, IsOwner
from ..serializers import (NoteBookSerializer, NoteRevisionSerializer,
                           NoteSerializer, UserSerializer)

logger = logging.getLogger(__name__)


class UserCreate(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class NoteBookList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    serializer_class = NoteBookSerializer

    def get_queryset(self):
        return NoteBook.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class NoteBookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializer


class NoteList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner, IsNoteBookOwner,)
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        query = Note.objects.filter(created_by=self.request.user)
        notebook = self.kwargs.get('notebook')
        return query.filter(notebook=notebook) if notebook else query


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner, IsNoteBookOwner,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteRevisionList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner, IsNoteOwner,)
    serializer_class = NoteRevisionSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        query = NoteRevision.objects.filter(created_by=self.request.user)
        note = self.kwargs.get('note')
        return query.filter(note=note) if note else query


class NoteRevisionDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner, IsNoteOwner,)
    queryset = NoteRevision.objects.all()
    serializer_class = NoteRevisionSerializer
