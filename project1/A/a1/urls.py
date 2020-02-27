
from django.contrib import admin
from django.urls import path,include
# we import this path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home page'),
    path('profile',views.profile,name='profile page'),
    path('about',views.about,name='about page'),
    path('details',views.details,name='details')
]
