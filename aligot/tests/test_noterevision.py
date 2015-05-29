
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Note, NoteBook, NoteRevision, User


class TestNoteRevisionAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='user', password='pass', email='mail@mail.com')
        self.notebook = NoteBook.objects.create(title='a title', created_by=self.user)
        self.note = Note.objects.create(title='a title for note', created_by=self.user, notebook=self.notebook)
        self.note2 = Note.objects.create(title='a title for note2', created_by=self.user, notebook=self.notebook)
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
        self.assertEquals(self.user.username, NoteRevision.objects.all()[0].created_by.username)

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

    def test_get_all(self):
        rev1 = NoteRevision.objects.create(content='a content for note', created_by=self.user, note=self.note)
        rev2 = NoteRevision.objects.create(content='a content for note. Yep.', created_by=self.user, note=self.note)
        response = self.client.get(reverse('revision-list'))
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(2, len(response.data))
        self.assertEquals(rev1.content, response.data[0]['content'])
        self.assertEquals(rev2.content, response.data[1]['content'])

    def test_get_all_of_note(self):
        rev1 = NoteRevision.objects.create(content='a content for note', created_by=self.user, note=self.note)
        rev2 = NoteRevision.objects.create(content='a content for note. Yep.', created_by=self.user, note=self.note)
        rev3 = NoteRevision.objects.create(content='a content for note. Foo', created_by=self.user, note=self.note2)
        rev4 = NoteRevision.objects.create(content='a content for note. FooFoo.', created_by=self.user, note=self.note2)
        response = self.client.get(reverse('note-revisionlist', args=[self.note.id]))
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(2, len(response.data))
        self.assertEquals(rev1.content, response.data[0]['content'])
        self.assertEquals(rev2.content, response.data[1]['content'])
        response = self.client.get(reverse('note-revisionlist', args=[self.note2.id]))
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(2, len(response.data))
        self.assertEquals(rev3.content, response.data[0]['content'])
        self.assertEquals(rev4.content, response.data[1]['content'])


class TestNoteRevisionApiWithoutUser(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='user', password='pass')
        self.notebook = NoteBook.objects.create(title='a title', created_by=self.user)
        self.note = Note.objects.create(title='note 1', created_by=self.user, notebook=self.notebook)
        self.revision = NoteRevision.objects.create(content='a content for note', created_by=self.user, note=self.note)

    def test_get(self):
        response = self.client.get(reverse('revision-detail', args=[self.revision.id]))
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_get_all(self):
        response = self.client.get(reverse('revision-list'))
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_get_all_of_note(self):
        response = self.client.get(reverse('note-revisionlist', args=[self.note.id]))
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_create(self):
        response = self.client.post(
            reverse('revision-list'),
            {'content': 'a content for note', 'note': self.note.id}
        )
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)

    def test_update(self):
        response = self.client.put(
            reverse('revision-detail', args=[self.revision.id]),
            {'content': 'new content', 'note': self.note.id}
        )
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)


class TestNoteRevisionApiWithDifferentUser(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create(username='user1', password='pass', email='mail1@mail.com')
        self.user2 = User.objects.create(username='user2', password='pass', email='mail2@mail.com')
        self.notebook1 = NoteBook.objects.create(title='a title', created_by=self.user1)
        self.notebook2 = NoteBook.objects.create(title='a title', created_by=self.user2)
        self.note1 = Note.objects.create(title='a title for note', created_by=self.user1, notebook=self.notebook1)
        self.note2 = Note.objects.create(title='a title for note2', created_by=self.user2, notebook=self.notebook2)
        self.client.force_authenticate(user=self.user1)

    def test_get_all(self):
        rev1 = NoteRevision.objects.create(content='a content for note', created_by=self.user1, note=self.note1)
        rev2 = NoteRevision.objects.create(content='a content for note. Yep.', created_by=self.user1, note=self.note1)
        NoteRevision.objects.create(content='a content for note. Foo', created_by=self.user2, note=self.note2)
        response = self.client.get(reverse('revision-list'))
        self.assertEquals(status.HTTP_200_OK, response.status_code, response.content)
        self.assertEquals(2, len(response.data))
        self.assertEquals(rev1.content, response.data[0]['content'])
        self.assertEquals(rev2.content, response.data[1]['content'])

    def test_get(self):
        rev = NoteRevision.objects.create(content='a content for note', created_by=self.user2, note=self.note2)
        response = self.client.get(reverse('revision-detail', args=[rev.id]))
        self.assertEquals(status.HTTP_403_FORBIDDEN, response.status_code, response.content)

    def test_create(self):
        response = self.client.post(
            reverse('revision-list'),
            {'content': 'a content for note', 'note': self.note2.id}
        )
        self.assertEquals(status.HTTP_403_FORBIDDEN, response.status_code, response.content)
