from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return redirect('accounts/login/')

@login_required
def home(request):
    user = request.user
    return render(request, 'home.html', {'user': user})

@login_required
def admin(request):
    user = request.user
    return render(request, 'admin.html', {'user': user})

@login_required
def reports(request):
    return render(request, 'reports.html')
