from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.db import connection

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
    id = (Album.objects.latest('albumid').albumid) + 1
    title = request.POST.get('title')
    artistName = request.POST.get('artistName')
    try:
        artist = Artist.objects.get(name = artistName)
        try:
            album = Album.objects.get(title = title)
        except Album.DoesNotExist:
            album = Album.objects.get_or_create(title = title, artistid = artist, albumid = id)
            userAlbum = UserAlbum.objects.create(albumid = album[0], userid = user)
    except Artist.DoesNotExist:
        raise Http404("Can't create an album if artist does not exist")
    return redirect('albums:index')

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

def search(request):
    user = request.user
    search = request.POST.get('search')
    resultSearch = custom_sql_dictfetchall(
        """
        select *
        from album
        where LOWER(title) LIKE LOWER('%{search}%');
        """.format(search=search)
    )
    return render(
        request, 
        'albums.html',
        {
            'user': user,
            'albums': resultSearch
        }
    )

def custom_sql_dictfetchall(query):
    "Return all rows from a cursor as a dict"
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
