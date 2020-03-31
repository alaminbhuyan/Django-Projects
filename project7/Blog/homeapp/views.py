from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from homeapp.models import Contact
from blogapp1.models import Post
from django.contrib.auth.models import User , auth

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


def search(request):
    query = request.GET['query']
    if len(query)>60:
        allPost = Post.objects.none()
    else:
        allPostTitle = Post.objects.filter(title__icontains=query)
        allPostContent = Post.objects.filter(content__icontains=query)
        allPost = allPostTitle.union(allPostContent)
    if allPost.count() == 0:
        messages.warning(request,"Youe search result not found.")
    value = {'allPost':allPost,'query':query}
    return render(request,'homeapp/search.html',value)


# signup function difinition
def singup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"User name already taken.Please try different username")
                return redirect('singup')
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email already use in a account.Please try with different email")
                return redirect('singup')
            else:
                user = User.objects.create_user(username=username,first_name=fname,last_name=lname,password=pass1,email=email)
                user.save()
                messages.success(request, "Your account is successfully Created")
                return redirect('/')
        else:
            messages.error(request,"Password is not matching")
            return redirect('singup')
    else:
        return HttpResponse('404 page not found')

# login function difinition


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Your account is successfully logIn")
            return redirect('/')
        else:
            messages.error(request, "Not credentials")
            return redirect('login')
    else:
        return redirect('login')

# logout function definition
def logout(request):
    auth.logout(request)
    return redirect('/')
