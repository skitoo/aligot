
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Note, NoteBook, NoteRevision, User


class TestNoteRevisionAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='user', password='pass')
        self.notebook = NoteBook.objects.create(title='a title', created_by=self.user)
        self.note = Note.objects.create(title='a title for note', created_by=self.user, notebook=self.notebook)
        self.client.force_authenticate(user=self.user)

    def test_create_without_params(self):
        self.assertEquals(status.HTTP_400_BAD_REQUEST, self.client.post(reverse('note-list')).status_code)
        self.assertEquals(0, NoteRevision.objects.count())

    def test_create(self):
        response = self.client.post(
            reverse('revision-list'),
            {'content': 'a content for note', 'note': self.note.id}
        )
        self.assertEquals(status.HTTP_201_CREATED, response.status_code, response.content)
        self.assertEquals(1, NoteRevision.objects.count())
        self.assertEquals(self.user.username, NoteRevision.objects.get(pk=1).created_by.username)

    def test_create_without_note(self):
        response = self.client.post(
            reverse('revision-list'),
            {'content': 'a content for note'}
        )
        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code, response.content)

    def test_update(self):
        revision = NoteRevision.objects.create(content='a content for note', created_by=self.user, note=self.note)
        response = self.client.put(
            reverse('revision-detail', args=[revision.id]),
            {'content': 'new content', 'note': self.note.id}
        )
        self.assertEquals(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code, response.content)
        self.assertEquals(revision.content, NoteRevision.objects.all()[0].content)

    def test_patch(self):
        revision = NoteRevision.objects.create(content='a content for note', created_by=self.user, note=self.note)
        response = self.client.put(
            reverse('revision-detail', args=[revision.id]),
            {'content': 'new content'}
        )
        self.assertEquals(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code, response.content)
        self.assertEquals(revision.content, NoteRevision.objects.all()[0].content)

    def test_delete(self):
        revision = NoteRevision.objects.create(content='a content for note', created_by=self.user, note=self.note)
        response = self.client.delete(reverse('revision-detail', args=[revision.id]))
        self.assertEquals(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code, response.content)
        self.assertEquals(1, NoteRevision.objects.count())

    def test_get(self):
        revision = NoteRevision.objects.create(content='a content for note', created_by=self.user, note=self.note)
        response = self.client.get(reverse('revision-detail', args=[revision.id]))
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(revision.content, response.data['content'], response.data)
        self.assertEquals(self.user.username, response.data['created_by'], response.data)
