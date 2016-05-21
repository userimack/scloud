from django.conf.urls import *
from django.conf import settings
from . import views

urlpatterns =patterns('',
    url(r'^$',views.index, name='index'),
    url(r'^music/$',views.music, name='music'),
#    url(r'^music/(?P<file>.+)$', views.download, name='download'),
    )

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
) + urlpatterns

