from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/login/signup/', views.createuser, name='signup'),

    path('home/', views.home, name='home'),

    path('home/search/', views.search, name='search'),

    path('musicStreaming/admin/users/', views.admin_users, name='admin'),
    path('musicStreaming/admin/users/update/<int:id>/done', views.admin_users_update_object, name='update_user'),

    path('musicStreaming/admin/groups/', views.admin_groups, name='admin_groups'),
    path('musicStreaming/admin/groups/create/new', views.admin_groups_create_new, name='create_group'),
    path('musicStreaming/admin/groups/update/<int:id>/done', views.admin_groups_update_object, name='update_group'),
    path('musicStreaming/admin/groups/delete/<int:id>/', views.admin_groups_delete, name='delete_group'),
    
    path('musicStreaming/admin/permissions/', views.admin_permissions, name='admin_permissions'),

    path('reports/', include('reports.urls', namespace='reports')),

    path('mongo/', include('mongoServices.urls', namespace='mongo')),
    
    path('albums/', include('albums.urls', namespace='albums')),

    path('artists/', include('artists.urls', namespace='artists')),

    path('genres/', include('genres.urls', namespace='genres')),

    path('playlists/', include('playlists.urls', namespace='playlists')),

    path('tracks/', include('tracks.urls', namespace='tracks')),

]