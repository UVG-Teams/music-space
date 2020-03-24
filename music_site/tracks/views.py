from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from tracks.models import Track
# Create your views here.

@login_required
def index(request):
    user = request.user
    tracks = Track.objects.all()
    return render(
        request,
        'tracks.html', 
        {
            'user': user,
            'tracks': tracks
        }
    )

def detail(request, id):
    return HttpResponse("Hello World, You are at track {id}.".format(id=id))

@login_required
def create(request):
    user = request.user
    return render(
        request,
        'track_create.html',
        {
            'user' : user
        }
    )
