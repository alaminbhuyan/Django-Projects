from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name = 'blogpage'),
    path('<str:slug>', views.blogpost, name = 'blogpost'),
]
