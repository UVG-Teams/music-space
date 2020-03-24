from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required

from artists.models import Artist

# Create your views here.

@login_required
def index(request):
    user = request.user
    artists = Artist.objects.all()
    return render(
        request,
        'artists.html', 
        {
            'user': user,
            'artists': artists
        }
    )

def detail(request, id):
    return HttpResponse("Hello World, You are at artist {id}.".format(id=id))

@login_required
def create(request):
    user = request.user
    return render(
        request,
        'artist_create.html',
        {
            'user' : user
        }
    )

@login_required
def update(request, id):
    try:
        artist = Artist.objects.get(pk = id)
        
    except Artist.DoesNotExist:
        raise Http404("Artist does not exist")
    return redirect('artists:index')

@login_required
def delete(request, id):
    try:
        artist = Artist.objects.get(pk = id)
        artist.delete()
    except Artist.DoesNotExist:
        raise Http404("Artist does not exist")
    return redirect('artists:index')
