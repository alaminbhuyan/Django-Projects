from django.shortcuts import render
from django.http import HttpResponse
from . import views
# Create your views here.
def app2(request):
    return HttpResponse("<h1>This is app2</h1>")