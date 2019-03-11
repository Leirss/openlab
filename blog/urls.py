from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),#更改
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
	url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
	url(r'^projects/',views.projects,name='projects'),
	url(r'^team/',views.team,name='team'),
	url(r'^events/',views.events,name='events'),
]