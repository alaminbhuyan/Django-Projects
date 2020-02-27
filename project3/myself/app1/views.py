from django.shortcuts import render

from django.http import HttpResponse
from .models import destination
# Create your views here.
def home(request):
    ''' dest1 = destination()
    dest1.name = 'Comilla'
    dest1.price = 1500
    dest1.img='popular_1.jpg'
    
    dest2 = destination()
    dest2.name = 'Manikkandi'
    dest2.price = 1000
    dest2.img = 'popular_2.jpg'
    
    dest3 = destination()
    dest3.name = 'Dhaka'
    dest3.price = 2000
    dest3.img = 'popular_3.jpg'
    
    dest4 = destination()
    dest4.name = 'Khulna'
    dest4.price = 2250
    dest4.img = 'popular_4.jpg'
    
    dest5 = destination()
    dest5.name = 'Barisal'
    dest5.price = 2500
    dest5.img = 'popular_6.jpg'
    
    dests = [dest1,dest2,dest3,dest4,dest5] '''
    
    
    dests = destination.objects.all()
    #return render(request, 'index.htm', {'price': 500,'name':'Dhaka'})
    return render(request, 'index.htm', {'dest': dests})
