from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.db import connection

from userTracks.models import UserTrack
from tracks.models import Track

# Create your views here.

@login_required
def play_song(request, id):
    user = request.user
    track = Track.objects.get(pk = id)
    play(user, track)
    return redirect(track.url)

def play(user, track):
    UserTrack.objects.create(
        trackid = track,
        userid = user,
        relation = "played"
    )

def load_song(request):
    tracks = Track.objects.all()
    for track in tracks:
        track.url = "https://www.youtube.com/results?search_query=" + track.name
        track.save()
    
    return redirect("home")