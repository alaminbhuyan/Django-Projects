from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    #return HttpResponse("<h2 style=font-style:italic;color:green;>Hello World</h2>")
    return render(request,'index.htm',{'content':'HTML'})

def profile(request):
    return HttpResponse("<h1 style= color:red;>Hello, Alamin now you have profile page.<a href='/'>Go home</a></h1><a href='about'>Go about</a>")

def about(request):
    return HttpResponse("<h1 style=font-weight:bold;color:orange;>Hi,Alamin this is about page!!!!!!!!!</h1><a href='app2'>Go App2</a>")


def details(request):
    a = int(request.POST['text1'])
    b = int(request.POST['text2'])
    c = a+b
    return render(request,'index.htm',{'result':c})
