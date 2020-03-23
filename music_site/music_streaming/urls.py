from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('home/', views.home, name='home'),

    path('musicStreaming/admin/', views.admin, name='admin'),
    path('musicStreaming/admin/artists', views.admin_artists, name='admin_artists'),
    path('musicStreaming/admin/albums', views.admin_albums, name='admin_albums'),
    path('musicStreaming/admin/tracks', views.admin_tracks, name='admin_tracks'),
    path('musicStreaming/admin/playlists', views.admin_playlists, name='admin_playlists'),

    path('reports/', views.reports, name='reports'),
    
    path('albums/', include('albums.urls')),

    path('artists/', include('artists.urls')),

    path('genres/', include('genres.urls')),

    path('playlists/', include('playlists.urls')),

    path('tracks/', include('tracks.urls')),

]