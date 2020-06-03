from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import connection

from playlists.models import Playlist
from userPlaylists.models import UserPlaylist
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

def search(request):
    user = request.user
    search = request.POST.get('search')
    resultSearch = custom_sql_dictfetchall(
        """
        select *
        from playlist
        where LOWER(name) LIKE LOWER('%{search}%');
        """.format(search=search)
    )
    return render(
        request, 
        'playlists.html',
        {
            'user': user,
            'playlists': resultSearch
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


@login_required
def create_new(request):
    user = request.user
    id = (Playlist.objects.latest('id').id) + 1
    name = request.POST.get('name')
    try:
        playlist = Playlist.objects.get(name = name)
    except Playlist.DoesNotExist:
        if (user.has_perm('playlist.add_playlist')):
            playlist = Playlist.objects.get_or_create(name = name, id = id)
            userPlaylist = UserPlaylist.objects.create(playlistid = playlist[0], userid = user)
        else:
            raise Http404('No tiene permiso')
    return redirect('playlists:index')

@login_required
def update(request, id):
    try:
        playlist = Playlist.objects.get(pk = id)
    except Playlist.DoesNotExist:
        raise Http404("Playlist does not exist")
    return render(
        request,
        'playlist_edit.html',
        {
            'playlist' : playlist
        }
    )

@login_required
def update_object(request, id):
    user = request.user
    try:
        if (user.has_perm('playlist.change_playlist')):
            name = request.POST.get('name')
            playlist = Playlist.objects.filter(pk = id).update(name = name)
        else:
            raise Http404('No tiene permiso')
    except Playlist.DoesNotExist:
        raise Http404("Playlist does not exist")
    return redirect('playlists:index')


@login_required
def delete(request, id):
    user = request.user
    try:
        if (user.has_perm('playlist.delete_playlist')):
            playlist = Playlist.objects.get(pk = id)
            playlist.delete()
        else:
            raise Http404('No tiene permiso')
    except Playlist.DoesNotExist:
        raise Http404("Playlist does not exist")
    return redirect('playlists:index')
