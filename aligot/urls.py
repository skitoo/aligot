from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from .views import api


urlpatterns = patterns(
    '',
    url(r'^$', 'aligot.views.html.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/user/(?P<pk>[0-9]+)/$', api.UserDetail.as_view(), name='user-detail'),
    url(r'^api/notebooks/$', api.NoteBookList.as_view(), name='notebook-list'),
    url(r'^api/notebook/(?P<pk>[0-9]+)/$', api.NoteBookDetail.as_view(), name='notebook-detail'),
    url(r'^api/notebook/(?P<notebook>[0-9]+)/notes/$', api.NoteList.as_view(), name='notebook-notelist'),
    url(r'^api/notes/$', api.NoteList.as_view()),
    url(r'^api/note/(?P<pk>[0-9]+)/$', api.NoteDetail.as_view()),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
