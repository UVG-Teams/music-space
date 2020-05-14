from django.urls import path

from . import views

app_name = 'reports'
urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.reports, name='all'),
    path('sales/', views.get_sales_on, name='sales'),
]