from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #check password matching
        if password == password2:
            #check username exist
            if User.objects.filter(username=username).exists():
                messages.error(request, "username is already taken..")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "email is already taken..")
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    user.save()
                    messages.success(request, "you are now registered and can log in.. ")
                    return redirect('login')
        else:
            messages.error(request, "Password do not match..")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "you are now logged in..")
            return redirect('dashboard')
        else:
            messages.error(request, "invalid credentials..")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "you ar now logged out..")
    return redirect('home')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
