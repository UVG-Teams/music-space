from django.urls import path

from . import views

app_name = 'userTrack'
urlpatterns = [
    path('play/<int:id>/', views.play_song, name='play'),
    path('load/', views.load_song, name='load'),
]

