from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='albumsIndex'),

    path('<int:id>/', views.detail, name='detail'),
]