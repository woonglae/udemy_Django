from django.conf.urls import url
from django.urls import path
from first_app import views

urlpatterns = [
    path('hello/',views.index, name='index'),
    url(r'^$', views.index, name='index'),
]
