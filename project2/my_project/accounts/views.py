from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Not credentials')
            return redirect('login')
    else:
        return render(request,'login.htm')
        


def register(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username take Already')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken Already')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password1)
                user.save()
                print('User Created')
        else:
            print('Password is not matchiing')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.htm')