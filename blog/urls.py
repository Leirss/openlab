from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',
        views.PostDetailView.as_view(), name='detail'),  # 更改
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',
        views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',
        views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^team/', views.TeamView.as_view(), name='team'),
    url(r'^projects/', views.ProjectsView.as_view(), name='projects'),
    url(r'^events/', views.EventsView.as_view(), name='events'),
    url(r'articles/', views.ArticleView.as_view(), name="articles"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
