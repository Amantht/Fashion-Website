from django.contrib import admin
from django.urls import path,include 
from home import views


urlpatterns = [

    path("register",views.registerPage,name='regsiter'),

    path("login",views.loginPage,name='login'),
    
    path("logout",views.logoutUser,name='logout'),
    
    path("",views.index,name='home'),
    
    path("about",views.about,name='about'),
    
    path("category",views.category,name='category'),
    
    path("contact",views.contact,name='contact'),

    path("women",views.women,name='women'),

    path("man",views.man,name='man'),

    path("kid",views.kid,name='kid'),

    path("diwali",views.diwali,name='diwali'),

   
    
]