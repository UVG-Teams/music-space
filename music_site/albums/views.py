from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from albums.models import Album

# Create your views here.

def index(request):
    return HttpResponse("Hello World, You are at albums index.")

def detail(request, id):
    try:
        album = Album.objects.get(pk = id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'albumDetail.html', {'album': album})
