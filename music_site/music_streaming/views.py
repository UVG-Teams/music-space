from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return redirect('accounts/login/')

# def login_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect("home/{user_id}".format(user_id=user.id))
#     return redirect("/")

@login_required
def home(request):
    return HttpResponse("Hello World, You are at music streaming home")

def admin(request):
    return HttpResponse("Hello World, You are at music streaming admin.")

def reports(request):
    return HttpResponse("Hello World, You are at music streaming reports.")

# def logout_view(request):
#     logout(request)
#     return redirect('')