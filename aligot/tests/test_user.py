# coding: utf-8

from django.core.urlresolvers import reverse
from django.db.utils import IntegrityError
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import User


class TestUser(TestCase):
    def test_create_with_same_email(self):
        User.objects.create(username='user1', password='mypassword', email='email@email.com')
        self.assertRaises(
            IntegrityError,
            User.objects.create,
            username='user2', password='mypassword', email='email@email.com'
        )


class TestUserApi(TestCase):

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

    def test_delete(self):
        """
        Simple deletion of an user in DB
        Wait for 204 response.
        """
        user = User.objects.create_user(
            username='test',
            password='test',
            email='mail@mail.com'
        )

        self.client.force_authenticate(user=user)

        self.assertEqual(1, User.objects.count(), 'ORM don\'t insert user in DB')

        response = self.client.delete(reverse('user-detail', args=[user.id]))

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code, response.content)
