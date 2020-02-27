from django.shortcuts import render
# we import this path
from django.http import HttpResponse
# Create your views here.


def home(request):
    # return HttpResponse("Hello World")
    return render(request, 'index.htm', {'title': 'Alamin', 'link': 'https://www.youtube.com/', 'link2': 'http://127.0.0.1:8000/'})


def profile(request):
    return HttpResponse("Profile page")


def expression(request):
    a = int(request.POST['text1'])
    b = int(request.POST['text2'])
    c = a+b
    return render(request, 'output.htm', {'result': c})
