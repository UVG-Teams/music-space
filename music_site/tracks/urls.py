from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='tracksIndex'),

    path('<int:id>/', views.detail, name='detail'),
]