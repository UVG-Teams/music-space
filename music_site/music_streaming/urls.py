from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('home/', views.home, name='home'),

    path('musicStreaming/admin/', views.admin, name='admin'),

    path('reports/', views.reports, name='reports'),
    
    path('albums/', include('albums.urls', namespace='albums')),

    path('artists/', include('artists.urls', namespace='artists')),

    path('genres/', include('genres.urls', namespace='genres')),

    path('playlists/', include('playlists.urls', namespace='playlists')),

    path('tracks/', include('tracks.urls', namespace='tracks')),

]