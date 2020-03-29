from django.shortcuts import render

from django.http import HttpResponse
from .models import Contact

# Create your views here.
def home(request):
    return render(request,'homeapp/index.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['content']
        #print(name, email, phone, content)
        contact = Contact( name = name, email = email, phone= phone, content= content)
        contact.save()
    return render(request,'homeapp/contact.html')
def about(request):
    return render(request, 'homeapp/about.html')
