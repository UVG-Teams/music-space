from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required

from albums.models import Album
from artists.models import Artist
from userAlbums.models import UserAlbum

# Create your views here.

@login_required
def index(request):
    user = request.user
    albums = Album.objects.all()
    return render(
        request,
        'albums.html', 
        {
            'user': user,
            'albums': albums
        }
    )

@login_required
def detail(request, id):
    try:
        album = Album.objects.get(pk = id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'albumDetail.html', {'album': album})

@login_required
def create(request):
    user = request.user
    return render(
        request,
        'album_create.html',
        {
            'user' : user
        }
    )
    
@login_required
def create_new(request):
    user = request.user
    title = request.POST.get('title')
    artistName = request.POST.get('artistName')
    artist = Artist.objects.get_or_create(name = artistName)
    # artist.save()
    album = Album.objects.get_or_create(title = title, artistid = artist[0])
    album.save()
    userAlbum = UserAlbum.objects.create(albumid = album[0], userid = user[0])
    userAlbum.save()
    return redirect('artists:index')

@login_required
def update(request, id):
    try:
        album = Album.objects.get(pk = id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(
        request,
        'album_edit.html',
        {
            'album' : album
        }
    )

@login_required
def update_object(request, id):
    try:
        title = request.POST.get('title')
        artistName = request.POST.get('artistName')
        artist = Artist.objects.get_or_create(name = artistName)
        album = Album.objects.filter(pk = id).update(title = title, artistid = artist[0])
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return redirect('albums:index')

@login_required
def delete(request, id):
    try:
        album = Album.objects.get(pk = id)
        album.delete()
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return redirect('albums:index')