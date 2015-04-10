# -*- coding: utf-8 -*-

from rest_framework import generics, permissions
from ..models import User, NoteBook, Note
from ..serializers import UserSerializer, NoteBookSerializer, NoteSerializer
from ..permissions import IsOwner


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NoteBookList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner,)
    serializer_class = NoteBookSerializer

    def get_queryset(self):
        user = self.request.user
        return [] if user.is_anonymous() else NoteBook.objects.filter(created_by=user)


class NoteBookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner,)
    queryset = NoteBook.objects.all()
    serializer_class = NoteBookSerializer


class NoteList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner,)
    serializer_class = NoteSerializer

    def get_queryset(self):
        user = self.request.user
        notebook = self.kwargs.get('notebook', None)
        if not user.is_anonymous():
            query = Note.objects.filter(created_by=user)
            if notebook is not None:
                query = query.filter(notebook=notebook)
            return query
        else:
            return []


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
