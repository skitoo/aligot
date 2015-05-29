# coding: utf-8

from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Note, NoteBook, User


class TestNoteApi(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='user', password='pass', email='mail@mail.com')
        self.notebook = NoteBook.objects.create(title='a title', created_by=self.user)
        self.notebook2 = NoteBook.objects.create(title='a title 2', created_by=self.user)
        self.client.force_authenticate(user=self.user)

    def test_create_without_params(self):
        self.assertEquals(status.HTTP_400_BAD_REQUEST, self.client.post(reverse('note-list')).status_code)
        self.assertEquals(0, Note.objects.count())

    def test_create(self):
        response = self.client.post(
            reverse('note-list'),
            {'title': 'a title for note', 'notebook': self.notebook.id}
        )
        self.assertEquals(status.HTTP_201_CREATED, response.status_code, response.content)
        self.assertEquals(1, Note.objects.count())
        self.assertEquals(self.user.username, Note.objects.all()[0].created_by.username)

    def test_create_without_notebook(self):
        response = self.client.post(
            reverse('note-list'),
            {'title': 'a title for note'}
        )
        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code, response.content)

    def test_update(self):
        note = Note.objects.create(title='a title for note', created_by=self.user, notebook=self.notebook)
        self.assertEquals(1, Note.objects.count())
        response = self.client.put(
            reverse('note-detail', args=[note.id]),
            {'title': 'new title', 'notebook': self.notebook.id}
        )
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(1, Note.objects.count())
        self.assertEquals('new title', Note.objects.all()[0].title)
        self.assertEquals(self.user.username, Note.objects.all()[0].created_by.username)

    def test_patch(self):
        note = Note.objects.create(title='a title for note', created_by=self.user, notebook=self.notebook)
        self.assertEquals(1, Note.objects.count())
        response = self.client.patch(
            reverse('note-detail', args=[note.id]),
            {'title': 'new title'}
        )
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(1, Note.objects.count())
        self.assertEquals('new title', Note.objects.all()[0].title)

    def test_delete(self):
        note = Note.objects.create(title='a title for note', created_by=self.user, notebook=self.notebook)
        self.assertEquals(1, Note.objects.count())
        response = self.client.delete(reverse('note-detail', args=[note.id]))
        self.assertEquals(status.HTTP_204_NO_CONTENT, response.status_code, response.content)
        self.assertEquals(0, Note.objects.count())

    def test_get(self):
        note = Note.objects.create(title='a title for note', created_by=self.user, notebook=self.notebook)
        self.assertEquals(1, Note.objects.count())
        response = self.client.get(reverse('note-detail', args=[note.id]))
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals('a title for note', response.data['title'], response.data)
        self.assertEquals(self.user.username, response.data['created_by'], response.data)

    def test_get_all(self):
        Note.objects.create(title='note 1', created_by=self.user, notebook=self.notebook)
        Note.objects.create(title='note 2', created_by=self.user, notebook=self.notebook)
        response = self.client.get(reverse('note-list'))
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(2, len(response.data))
        self.assertEquals('note 1', response.data[0]['title'])
        self.assertEquals('note 2', response.data[1]['title'])

    def test_get_all_of_notebook(self):
        Note.objects.create(title='note 1', created_by=self.user, notebook=self.notebook)
        Note.objects.create(title='note 2', created_by=self.user, notebook=self.notebook)
        Note.objects.create(title='note 3', created_by=self.user, notebook=self.notebook2)
        Note.objects.create(title='note 4', created_by=self.user, notebook=self.notebook2)
        response = self.client.get(reverse('notebook-notelist', args=[self.notebook.id]))
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(2, len(response.data))
        self.assertEquals('note 1', response.data[0]['title'])
        self.assertEquals('note 2', response.data[1]['title'])
        response = self.client.get(reverse('notebook-notelist', args=[self.notebook2.id]))
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(2, len(response.data))
        self.assertEquals('note 3', response.data[0]['title'])
        self.assertEquals('note 4', response.data[1]['title'])


class TestNoteApiWithoutUser(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='user', password='pass')
        self.notebook = NoteBook.objects.create(title='a title', created_by=self.user)
        self.note = Note.objects.create(title='note 1', created_by=self.user, notebook=self.notebook)

    def test_get(self):
        response = self.client.get(reverse('note-detail', args=[self.note.id]))
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_get_all(self):
        response = self.client.get(reverse('note-list'))
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_get_all_of_notebook(self):
        response = self.client.get(reverse('notebook-notelist', args=[self.notebook.id]))
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_create(self):
        response = self.client.post(reverse('note-list'), {'title': 'a title', 'notebook': self.notebook.id})
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_update(self):
        response = self.client.put(
            reverse('note-detail', args=[self.note.id]),
            {'title': 'new title', 'notebook': self.notebook.id}
        )
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_delete(self):
        response = self.client.delete(reverse('note-detail', args=[self.note.id]))
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_patch(self):
        response = self.client.patch(
            reverse('note-detail', args=[self.note.id]),
            {'title': 'new title'}
        )
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)


class TestNoteApiWithDifferentUser(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create(username='user1', password='pass', email='mail1@mail.com')
        self.user2 = User.objects.create(username='user2', password='pass', email='mail2@mail.com')
        self.client.force_authenticate(user=self.user1)
        self.notebook = NoteBook.objects.create(title='a title', created_by=self.user1)
        self.notebook2 = NoteBook.objects.create(title='a title', created_by=self.user2)

    def test_get_all(self):
        Note.objects.create(title='note 1', created_by=self.user1, notebook=self.notebook)
        Note.objects.create(title='note 2', created_by=self.user1, notebook=self.notebook)
        Note.objects.create(title='note 3', created_by=self.user2, notebook=self.notebook2)
        response = self.client.get(reverse('note-list'))
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(2, len(response.data))
        self.assertEquals('note 1', response.data[0]['title'])
        self.assertEquals('note 2', response.data[1]['title'])

    def test_get(self):
        note = Note.objects.create(title='note 1', created_by=self.user2, notebook=self.notebook2)
        response = self.client.get(reverse('note-detail', args=[note.id]))
        self.assertEquals(status.HTTP_403_FORBIDDEN, response.status_code, response.content)

    def test_create(self):
        response = self.client.post(
            reverse('note-list'),
            {'title': 'a title for note', 'notebook': self.notebook2.id}
        )
        self.assertEquals(status.HTTP_403_FORBIDDEN, response.status_code, response.content)

    def test_delete(self):
        note = Note.objects.create(title='note 1', created_by=self.user2, notebook=self.notebook2)
        response = self.client.get(reverse('note-detail', args=[note.id]))
        self.assertEquals(status.HTTP_403_FORBIDDEN, response.status_code, response.content)

    def test_update(self):
        note = Note.objects.create(title='note 1', created_by=self.user2, notebook=self.notebook2)
        response = self.client.put(
            reverse('note-detail', args=[note.id]),
            {'title': 'new title', 'notebook': self.notebook2.id}
        )
        self.assertEquals(status.HTTP_403_FORBIDDEN, response.status_code, response.content)

    def test_update_with_other_notebook(self):
        note = Note.objects.create(title='note 1', created_by=self.user1, notebook=self.notebook)
        response = self.client.put(
            reverse('note-detail', args=[note.id]),
            {'title': 'new title', 'notebook': self.notebook2.id}
        )
        self.assertEquals(status.HTTP_403_FORBIDDEN, response.status_code, response.content)

    def test_patch(self):
        note = Note.objects.create(title='note 1', created_by=self.user2, notebook=self.notebook2)
        response = self.client.patch(
            reverse('note-detail', args=[note.id]),
            {'title': 'new title'}
        )
        self.assertEquals(status.HTTP_403_FORBIDDEN, response.status_code, response.content)
