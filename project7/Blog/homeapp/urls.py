from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homePage'),
    
    path('contact', views.contact, name='contactPage'),
    
    path('about', views.about, name='aboutPage'),
    
    path('search', views.search, name='search'),
    
    path('singup', views.singup, name='singup'),
    
    path('login', views.login, name='login'),
    
    path('logout', views.logout, name='logout'),
]
