# coding: utf-8

from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import NoteBook, User


class TestNoteBookApi(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='user', password='pass', email='mail@mail.com')
        self.client.force_authenticate(user=self.user)

    def test_create_without_params(self):
        self.assertEquals(status.HTTP_400_BAD_REQUEST, self.client.post(reverse('notebook-list')).status_code)
        self.assertEquals(0, NoteBook.objects.count())

    def test_create(self):
        response = self.client.post(
            reverse('notebook-list'),
            {'title': 'a title'}
        )
        self.assertEquals(status.HTTP_201_CREATED, response.status_code, response.content)
        self.assertEquals(1, NoteBook.objects.count())
        self.assertEquals(self.user.username, NoteBook.objects.all()[0].created_by.username)

    def test_update(self):
        notebook = NoteBook.objects.create(title='a title', created_by=self.user)
        self.assertEquals(1, NoteBook.objects.count())
        response = self.client.put(
            reverse('notebook-detail', args=[notebook.id]),
            {'title': 'new title'}
        )
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(1, NoteBook.objects.count())
        self.assertEquals('new title', NoteBook.objects.all()[0].title)
        self.assertEquals(self.user.username, NoteBook.objects.all()[0].created_by.username)

    def test_patch(self):
        notebook = NoteBook.objects.create(title='a title', created_by=self.user)
        self.assertEquals(1, NoteBook.objects.count())
        response = self.client.patch(
            reverse('notebook-detail', args=[notebook.id]),
            {'title': 'new title'}
        )
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(1, NoteBook.objects.count())
        self.assertEquals('new title', NoteBook.objects.all()[0].title)

    def test_delete(self):
        notebook = NoteBook.objects.create(title='a title', created_by=self.user)
        self.assertEquals(1, NoteBook.objects.count())
        response = self.client.delete(reverse('notebook-detail', args=[notebook.id]))
        self.assertEquals(status.HTTP_204_NO_CONTENT, response.status_code, response.content)
        self.assertEquals(0, NoteBook.objects.count())

    def test_get(self):
        notebook = NoteBook.objects.create(title='a title', created_by=self.user)
        self.assertEquals(1, NoteBook.objects.count())
        response = self.client.get(reverse('notebook-detail', args=[notebook.id]))
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals('a title', response.data['title'], response.data)
        self.assertEquals(self.user.username, response.data['created_by'], response.data)

    def test_get_all(self):
        NoteBook.objects.create(title='notebook 1', created_by=self.user)
        NoteBook.objects.create(title='notebook 2', created_by=self.user)
        response = self.client.get(reverse('notebook-list'))
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(2, len(response.data))
        self.assertEquals('notebook 1', response.data[0]['title'])
        self.assertEquals('notebook 2', response.data[1]['title'])


class TestNoteBookApiWithoutUser(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='user', password='pass')
        self.notebook = NoteBook.objects.create(title='a title', created_by=self.user)

    def test_get(self):
        response = self.client.get(reverse('notebook-detail', args=[self.notebook.id]))
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_get_all(self):
        response = self.client.get(reverse('notebook-list'))
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)


class TestNoteBookApiWithDifferentUser(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create(username='user1', password='pass', email='mail1@mail.com')
        self.user2 = User.objects.create(username='user2', password='pass', email='mail2@mail.com')
        self.client.force_authenticate(user=self.user1)

    def test_get_all(self):
        NoteBook.objects.create(title='notebook 1', created_by=self.user1)
        NoteBook.objects.create(title='notebook 2', created_by=self.user1)
        NoteBook.objects.create(title='notebook 3', created_by=self.user2)
        response = self.client.get(reverse('notebook-list'))
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(2, len(response.data))
        self.assertEquals('notebook 1', response.data[0]['title'])
        self.assertEquals('notebook 2', response.data[1]['title'])

    def test_get(self):
        notebook = NoteBook.objects.create(title='notebook 1', created_by=self.user2)
        response = self.client.get(reverse('notebook-detail', args=[notebook.id]))
        self.assertEquals(status.HTTP_403_FORBIDDEN, response.status_code, response.content)

    def test_delete(self):
        notebook = NoteBook.objects.create(title='notebook 1', created_by=self.user2)
        response = self.client.delete(reverse('notebook-detail', args=[notebook.id]))
        self.assertEquals(status.HTTP_403_FORBIDDEN, response.status_code, response.content)

    def test_update(self):
        notebook = NoteBook.objects.create(title='notebook 1', created_by=self.user2)
        response = self.client.put(
            reverse('notebook-detail', args=[notebook.id]),
            {'title': 'new title'}
        )
        self.assertEquals(status.HTTP_403_FORBIDDEN, response.status_code, response.content)

    def test_patch(self):
        notebook = NoteBook.objects.create(title='notebook 1', created_by=self.user2)
        response = self.client.patch(
            reverse('notebook-detail', args=[notebook.id]),
            {'title': 'new title'}
        )
        self.assertEquals(status.HTTP_403_FORBIDDEN, response.status_code, response.content)
