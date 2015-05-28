# coding: utf-8

from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import User


class TestUser(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_without_params(self):
        self.assertEquals(status.HTTP_400_BAD_REQUEST, self.client.post(reverse('user-create')).status_code)
        self.assertEquals(0, User.objects.count())

    def test_create(self):
        """
        Create user & wait for 201 response.
        """
        data = {
            'username': 'test',
            'password': 'test',
            'email': 'test@mail.com'
        }
        response = self.client.post(reverse('user-create'), data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code, response.content)
        self.assertEqual(1, User.objects.count())

        # Check the first
        user = User.objects.all()[0]
        self.assertEqual(user.username, data['username'], 'Username in DB don\'t match')




