from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members:login')
    else:
        form = RegistrationForm()

    return render(request, 'members/register.html', {'form':form})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'members/Login.html')
    return render(request, 'members/Login.html') 



