from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from genres.models import Genre
# Create your views here.

def index(request):
    return HttpResponse("Hello World, You are at genres index.")

def detail(request, id):
    return HttpResponse("Hello World, You are at genre {id}.".format(id=id))
