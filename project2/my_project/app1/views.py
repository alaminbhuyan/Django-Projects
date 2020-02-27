from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
# Create your views here.
def function1(request):
    #return HttpResponse('Hello world')
    return render(request,'base.htm')
