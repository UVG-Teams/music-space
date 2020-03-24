from django.urls import path

from . import views

app_name = 'playlists'
urlpatterns = [
    path('', views.index, name='index'),

    path('<int:id>/', views.detail, name='detail'),
]