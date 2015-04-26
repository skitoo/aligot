# coding: utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from rest_framework import status
from ..models import NoteBook, User
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class TestNoteBookApi(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='user', password='pass')
        self.client.force_authenticate(user=self.user)
        self.url = reverse('notebook-list')

    def test_create_without_params(self):
        self.assertEquals(status.HTTP_400_BAD_REQUEST, self.client.post(self.url).status_code)
        self.assertEquals(0, NoteBook.objects.count())

    def test_create(self):
        response = self.client.post(self.url, {'title': 'a title', 'created_by': reverse('user-detail', args=[self.user.id])})
        self.assertEquals(status.HTTP_201_CREATED, response.status_code, response.content)
        self.assertEquals(1, NoteBook.objects.count())

    def test_update(self):
        notebook = NoteBook.objects.create(title='a title', created_by=self.user)
        self.assertEquals(1, NoteBook.objects.count())
        response = self.client.put(reverse('notebook-detail', args=[notebook.id]), {'title': 'new title', 'created_by': reverse('user-detail', args=[self.user.id])})
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

    def test_get_all(self):
        nb1 = NoteBook.objects.create(title='notebook 1', created_by=self.user)
        nb2 = NoteBook.objects.create(title='notebook 2', created_by=self.user)
        response = self.client.get(reverse('notebook-list'))
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(2, len(response.data))
        self.assertEquals('notebook 1', response.data[0]['title'])
        self.assertEquals('notebook 2', response.data[1]['title'])
