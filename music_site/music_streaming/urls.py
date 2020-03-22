from django.urls import path

from . import views
# from albums import views as albums_views

urlpatterns = [
    path('', views.index, name='index'),

    # path('albums/', 
    #     albums_views, 
    #     name = "albums"),
]