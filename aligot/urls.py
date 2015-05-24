from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.authtoken import views

from .views import api

urlpatterns = patterns(
    '',
    url(r'^$', 'aligot.views.html.index', name='index'),
    url(r'^login$', 'aligot.views.html.index', name='login'),
    url(r'^register$', 'aligot.views.html.index', name='register'),


    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/token-auth/', views.obtain_auth_token),

    # url(r'^api/auth/$', api.AuthView.as_view(), name='authenticate'),
    # url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/user/(?P<pk>[0-9]+)/$', api.UserDetail.as_view(), name='user-detail'),
    url(r'^api/notebooks/$', api.NoteBookList.as_view(), name='notebook-list'),
    url(r'^api/notebook/(?P<pk>[0-9]+)/$', api.NoteBookDetail.as_view(), name='notebook-detail'),
    url(r'^api/notebook/(?P<notebook>[0-9]+)/notes/$', api.NoteList.as_view(), name='notebook-notelist'),
    url(r'^api/notes/$', api.NoteList.as_view(), name='note-list'),
    url(r'^api/note/(?P<pk>[0-9]+)/$', api.NoteDetail.as_view(), name='note-detail'),
    url(r'^api/note/(?P<note>[0-9]+)/revisions/$', api.NoteRevisionList.as_view(), name='note-revisionlist'),
    url(r'^api/revisions/$', api.NoteRevisionList.as_view(), name='revision-list'),
    url(r'^api/revision/(?P<pk>[0-9]+)/$', api.NoteRevisionDetail.as_view(), name='revision-detail'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
