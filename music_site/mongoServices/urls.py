from django.urls import path

from . import views

app_name = 'mongo'
urlpatterns = [
    path('', views.index, name='index'),
    path('print-collection/', views.print_collection, name='print'),
    path('empty-collection/', views.empty_collection, name='empty'),
]