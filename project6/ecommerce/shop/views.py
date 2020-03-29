from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.


def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil(n/4)-(n//4)
    Dict = {'num_of_slides': nSlides, 'range': range(1,nSlides), 'product': products}
    return render(request, 'shop/index.html' , Dict)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("<h1>This is contact page</h1>")


def tracker(request):
    return HttpResponse("<h1>This is tracker page</h1>")


def search(request):
    return HttpResponse("<h1>This is search page</h1>")


def productview(request):
    return HttpResponse("<h1>This is product page</h1>")


def chacker(request):
    return HttpResponse("<h1>This is chacker page</h1>")
