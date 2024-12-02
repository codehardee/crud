from django.urls import path
#from .views import *
from . import views
#from django.contrib import admin

app_name = 'members'
urlpatterns = [
    path('register/',views.register, name="register"),
     path('login/',views.Login, name="login"),
    
]
