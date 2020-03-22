from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('albums/', include('albums.urls')),

    path('artists/', include('artists.urls')),

    path('genres/', include('genres.urls')),

    path('playlists/', include('playlists.urls')),

    path('tracks/', include('tracks.urls')),

    path('reports/', views.reports, name='reports'),

    path('musicStreaming/admin/', views.admin, name='admin'),
]