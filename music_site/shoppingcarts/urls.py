from django.urls import path

from . import views

app_name = 'shoppingcarts'
urlpatterns = [
    path('', views.index, name='index'),

    path('delete/<int:id>/', views.delete, name='delete'),

    path('buy/', views.buy, name='buy'),
]