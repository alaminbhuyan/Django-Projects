from django.shortcuts import render
from django.contrib import messages
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
        if len(name)<2 or len(phone)<11 or len(email)<4 or len(content)<5:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact( name = name, email = email, phone= phone, content= content)
            contact.save()
            messages.success(request,"Your message is Successfully send")
    return render(request,'homeapp/contact.html')
def about(request):
    return render(request, 'homeapp/about.html')
