from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homePage'),
    
    path('contact', views.contact, name='contactPage'),
    
    path('about', views.about, name='aboutPage'),
]
