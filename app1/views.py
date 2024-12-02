from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import *
from .models import *




# Create your views here.

def search(request):
    search_query = request.GET.get('search', '')  # Use the get() method with a default value
    datas = Data.objects.filter(category__icontains=search_query)

    
   
    context = {'datas' : datas}
    return render(request, 'app1/search.html', context)



# def cat1(request, pk):
    
#     # data = get_object_or_404(Data, pk=pk)
#     data = Data.objects.all()
#     context = {'data' : data}
#     return render(request, 'app1/cat1.html', context)

# def cat1(request, pk):
#     category_recipes = Data.objects.all()
#     context = {'data': category_recipes}
#     return render(request, 'app1/cat1.html', context)

def cat1(request, pk):
    data = get_object_or_404(Data, pk=pk)
    context = {'data': data}
    return render(request, 'app1/cat1.html', context)

def cat2(request):
    mydata = Datareceipe.objects.all()
    context = {'mydata' : mydata}
    return render(request, 'app1/cat2.html', context)

def addcatreceipe(request):
    if request.method == "POST":
        form = DataForm1(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = DataForm1()
   
    img = Datareceipe.objects.all()
    context = {'form' : form, 'img' : img}
    return render(request, 'app1/addcatreceipe.html', context)

# @login_required
def index(request):
    datas = Data.objects.all()
    username = request.user.username
    context = {'datas' : datas, 'username': username}
    return render(request, 'app1/index.html', context)

def addreceipe(request):
    if request.method == "POST":
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = DataForm()
   
    img = Data.objects.all()
    context = {'form' : form, 'img' : img}
    return render(request, 'app1/addreceipe.html', context)

# def register(request): 
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#            form.save
#            return redirect('index')
#     else:
#         form = RegistrationForm()
#     context = {'form': form}
#     return render(request, 'app1/register.html', context)


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             return render(request, 'app1/login.html')
#     return render(request, "app1/login.html")

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             return render(request, 'app1/login.html')
#     return render(request, "app1/login.html")