# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Note, NoteBook, NoteRevision, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        write_only_fields = ('password',)


class NoteBookSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = NoteBook
        fields = ('id', 'title', 'created_by', 'created_at', 'note_count',)


class NoteSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Note


class NoteRevisionSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = NoteRevision
