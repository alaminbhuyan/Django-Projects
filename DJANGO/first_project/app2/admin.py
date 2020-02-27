from django.contrib import admin
#we add this path
from .models import employee
admin.site.register(employee)
# Register your models here.
