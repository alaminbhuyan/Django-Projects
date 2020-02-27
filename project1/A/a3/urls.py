from django.contrib import admin
from django.urls import include, path

# we import this path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('signup', views.signup, name='signup'),
]
