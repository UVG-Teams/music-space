from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from playlists.models import Playlist
# Create your views here.

@login_required
def index(request):
    user = request.user
    playlists = Playlist.objects.all()
    return render(
        request,
        'playlists.html', 
        {
            'user': user,
            'playlists': playlists
        }
    )

def detail(request, id):
    return HttpResponse("Hello World, You are at playlist {id}.".format(id=id))

@login_required
def create(request):
    user = request.user
    return render(
        request,
        'playlist_create.html',
        {
            'user' : user
        }
    )
