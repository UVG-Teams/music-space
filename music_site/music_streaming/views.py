from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World, You are at music streaming index.")

def admin(request):
    return HttpResponse("Hello World, You are at music streaming admin.")

def reports(request):
    return HttpResponse("Hello World, You are at music streaming reports.")