from django.contrib import admin
from django.urls import path
from second_app import views

urlpatterns = [
        path('users/', views.users, name='users'),
        path('', views.index, name='index')
]
