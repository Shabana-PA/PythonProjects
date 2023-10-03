# bankapp/urls.py
from django.urls import path
from . import views
app_name = 'bankapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('details/', views.details, name='details'),
    path('success/', views.success, name='success'),
    path('get_branches/', views.get_branches, name='get_branches'),
]
