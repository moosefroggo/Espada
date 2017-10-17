from django.conf.urls import url
from . import views

app_name = 'homepage'

urlpatterns = [
    
    #/homepage/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/music/album_id
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='details'),

    #/homepage/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    #homepage/album/2
    url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(), name='album-update'),
    
    #homepage/album/2/delete
    url(r'^album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(), name='album-delete'),
]