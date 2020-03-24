from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from genres.models import Genre
# Create your views here.

def index(request):
    return HttpResponse("Hello World, You are at genres index.")

def detail(request, id):
    return HttpResponse("Hello World, You are at genre {id}.".format(id=id))

@login_required
def create(request):
    user = request.user
    return render(
        request,
        'genre_create.html',
        {
            'user' : user
        }
    )
