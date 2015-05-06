# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from rest_framework import status

from ..models import Note, NoteBook, User


class TestNoteApi(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='user', password='pass')
        self.notebook = NoteBook.objects.create(title='a title', created_by=self.user)
        self.client.force_authenticate(user=self.user)

    def test_create_without_params(self):
        self.assertEquals(status.HTTP_400_BAD_REQUEST, self.client.post(reverse('note-list')).status_code)
        self.assertEquals(0, Note.objects.count())

    def test_create(self):
        response = self.client.post(
            reverse('note-list'),
            {'title': 'a title', 'created_by': self.user.id, 'notebook': self.notebook.id}
        )
        self.assertEquals(status.HTTP_201_CREATED, response.status_code, response.content)
        self.assertEquals(1, NoteBook.objects.count())

    def test_update(self):
        note = Note.objects.create(title='a title', created_by=self.user, notebook=self.notebook)
        self.assertEquals(1, Note.objects.count())
        response = self.client.put(
            reverse('note-detail', args=[note.id]),
            {'title': 'new title', 'created_by': self.user.id, 'notebook': self.notebook.id}
        )
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(1, Note.objects.count())
        self.assertEquals('new title', Note.objects.all()[0].title)

    def test_delete(self):
        note = Note.objects.create(title='a title', created_by=self.user, notebook=self.notebook)
        self.assertEquals(1, Note.objects.count())
        response = self.client.delete(reverse('note-detail', args=[note.id]))
        self.assertEquals(status.HTTP_204_NO_CONTENT, response.status_code, response.content)
        self.assertEquals(0, Note.objects.count())
