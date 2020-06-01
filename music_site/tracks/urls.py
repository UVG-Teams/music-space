from django.urls import path

from . import views

app_name = 'tracks'
urlpatterns = [
    path('', views.index, name='index'),

    path('<int:id>/', views.detail, name='detail'),

    path('search/', views.search, name="search"),

    path('create/', views.create, name='create'),
    path('create/new', views.create_new, name='create_new'),

    path('update/<int:id>/', views.update, name='update'),
    path('update/<int:id>/done', views.update_object, name='update_object'),

    path('delete/<int:id>/', views.delete, name='delete'),
    
    path('buy/<int:id>/', views.buy, name='buy'),
]