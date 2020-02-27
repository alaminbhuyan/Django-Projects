from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    #path('admin/', admin.site.urls),
    path('',views.app2,name='app2')
]

