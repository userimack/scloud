from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$',views.index, name='index'),
    url(r'^music/$',views.music, name='music'),
    url(r'^upload/$',views.upload, name='upload'),
    ]