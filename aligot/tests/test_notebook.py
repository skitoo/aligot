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
        self.assertEquals(400, self.client.post(self.url).status_code)
        self.assertEquals(0, NoteBook.objects.count())

    def test_create(self):
        response = self.client.post(self.url, {'title': 'a title', 'created_by': reverse('user-detail', args=[self.user.id])})
        self.assertEquals(status.HTTP_201_CREATED, response.status_code, response.content)
        self.assertEquals(1, NoteBook.objects.count())
