from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from .models import destination
# Create your views here.


def function2(request):
    
    ''' desc1 = destination()
    desc1.price = 1000
    desc1.img='destination_1.jpg'
    desc1.desc='The city that is not sleep'
    desc1.name='Dhaka'
    desc1.offer=False
    
    desc2 = destination()
    desc2.price = 2000
    desc2.img = 'destination_2.jpg'
    desc2.desc='The city is looking nice'
    desc2.name='Comilla'
    desc2.offer = True
    
    desc3 = destination()
    desc3.price = 3000
    desc3.img = 'destination_3.jpg'
    desc3.desc = 'The city is very nice'
    desc3.name = 'Sylhet'
    desc3.offer = False
    all_desc = [desc1,desc2,desc3]
     '''
    all_desc = destination.objects.all()
    return render(request, 'index.htm', {'desc': all_desc})

