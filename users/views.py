from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import logging
from django.views.decorators.csrf import csrf_exempt


logger = logging.getLogger(__name__)

def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,(" Email or Password doesn't match!!!"))
            return redirect('login')
    else:
        return render(request,'users/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,("Logged Out Successfull!"))
    return redirect('login')

@csrf_exempt
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=email,password=password)
            login(request,user)
            messages.success(request,("Registration Successful")) 
            print("42")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})