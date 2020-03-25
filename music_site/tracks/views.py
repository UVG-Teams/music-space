from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from tracks.models import Track
from genres.models import Genre
from albums.models import Album
from userTracks.models import UserTrack

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

@login_required
def create_new(request):
    user = request.user
    id = (Track.objects.latest('trackid').trackid) + 1
    name = request.POST.get('name')
    try:
        albumTitle = request.POST.get('albumTitle')
    except albumTitle.DoesNotExist:
        raise Http404("Can't add a track without a registed album")
    genreName = request.POST.get('genreName')
    composer = request.POST.get('composer')
    milliseconds = request.POST.get('milliseconds')
    unitprice = 0.9
    album = Album.objects.get_or_create(title = albumTitle)
    genre = Genre.objects.get_or_create(name = genreName)
    track = Track.objects.get_or_create(
        name = name,
        albumid = album[0],
        genreid = genre[0],
        composer = composer,
        milliseconds = milliseconds,
        unitprice = unitprice,
        trackid = id
    )
    userTrack = UserTrack.objects.create(trackid = track[0], userid = user)
    return redirect('tracks:index')

@login_required
def update(request, id):
    try:
        track = Track.objects.get(pk = id)
    except Track.DoesNotExist:
        raise Http404("Track does not exist")
    return render(
        request,
        'track_edit.html',
        {
            'track' : track
        }
    )

@login_required
def update_object(request, id):
    try:
        name = request.POST.get('name')
        albumTitle = request.POST.get('albumTitle')
        genreName = request.POST.get('genreName')
        composer = request.POST.get('composer')
        milliseconds = request.POST.get('milliseconds')
        unitprice = 0.9
        active = True if request.POST.get('active') else False
        album = Album.objects.get_or_create(title = albumTitle)
        genre = Genre.objects.get_or_create(name = genreName)
        track = Track.objects.filter(pk = id).update(
            name = name,
            albumid = album[0],
            genreid = genre[0],
            composer = composer,
            milliseconds = milliseconds,
            unitprice = unitprice,
            active = active
        )
    except Track.DoesNotExist:
        raise Http404("Track does not exist")
    return redirect('tracks:index')

@login_required
def delete(request, id):
    try:
        track = Track.objects.get(pk = id)
        track.delete()
    except Track.DoesNotExist:
        raise Http404("Track does not exist")
    return redirect('tracks:index')
