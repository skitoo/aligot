from django.conf.urls import include, patterns, url
from django.contrib import admin
from rest_framework.authtoken import views

from .views import api

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/token-auth/', views.obtain_auth_token),

    url(r'^api/user/create/$', api.UserCreate.as_view(), name='user-create'),
    url(r'^api/user/(?P<username>\w+)/$', api.UserDetail.as_view(), name='user-detail'),

    url(r'^api/notebooks/$', api.NoteBookList.as_view(), name='notebook-list'),
    url(r'^api/notebook/(?P<pk>[^/]+)/$', api.NoteBookDetail.as_view(), name='notebook-detail'),
    url(r'^api/notebook/(?P<notebook>[^/]+)/notes/$', api.NoteList.as_view(), name='notebook-notelist'),
    url(r'^api/notes/$', api.NoteList.as_view(), name='note-list'),
    url(r'^api/note/(?P<pk>[^/]+)/$', api.NoteDetail.as_view(), name='note-detail'),
    url(r'^api/note/(?P<note>[^/]+)/revisions/$', api.NoteRevisionList.as_view(), name='note-revisionlist'),
    url(r'^api/revisions/$', api.NoteRevisionList.as_view(), name='revision-list'),
    url(r'^api/revision/(?P<pk>[^/]+)/$', api.NoteRevisionDetail.as_view(), name='revision-detail'),

)
