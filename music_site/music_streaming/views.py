from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import connection

from genres.models import Genre
from artists.models import Artist
from tracks.models import Track
from albums.models import Album
from playlists.models import Playlist
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

# Create your views here.

def index(request):
    return redirect('accounts/login/')

@login_required
def home(request):
    user = request.user
    genres = Genre.objects.all()
    artists = Artist.objects.all()
    tracks = Track.objects.all()
    albums = Album.objects.all()
    playlists = Playlist.objects.all()
    return render(
        request, 
        'home.html', 
        {
            'user': user,
            'genres': genres,
            'artists': artists,
            'tracks': tracks,
            'albums': albums,
            "playlists": playlists
        }
    )

def search(request):
    user = request.user
    search = request.POST.get('search')
    resultSearch = custom_sql_dictfetchall(
        """
        select id, tipo, name from (
            select artistid as id, 'artist' as tipo, name as name from artist a
            union
            select genreid as id, 'genre' as tipo, name as name from genre g
            union
            select albumid as id, 'album' as tipo, title as name from album a
            union
            select trackid as id, 'track' as tipo, name as name from track t
        ) as global
        where LOWER(name) LIKE LOWER('%{search}%');
        """.format(search=search)
    )
    return render(
        request, 
        'search.html',
        {
            'user': user,
            'resultSearch': resultSearch
        }
    )

@login_required
def admin_users(request):
    user = request.user
    users = User.objects.all()
    return render(
        request,
        'admin_users.html',
        {
            'user': user,
            'users': users
        }
    )

@login_required
def admin_groups(request):
    user = request.user
    groups = Group.objects.all()
    return render(
        request,
        'admin_groups.html', 
        {
            'user': user,
            'groups': groups
        }
    )

@login_required
def admin_groups_create_new(request):
    user = request.user
    name = request.POST.get('name')
    group = Group.objects.create(name = name)
    group.save()
    return redirect('admin_groups')

@login_required
def admin_groups_update_object(request, id):
    try:
        name = request.POST.get('name')
        group = Group.objects.filter(pk = id).update(name = name)
    except Group.DoesNotExist:
        raise Http404("Group does not exist")
    return redirect('admin_groups')

@login_required
def admin_groups_delete(request, id):
    try:
        group = Group.objects.get(pk = id)
        group.delete()
    except Group.DoesNotExist:
        raise Http404("Group does not exist")
    return redirect('admin_groups')

@login_required
def admin_permissions(request):
    user = request.user
    permissions = Permission.objects.all()
    return render(
        request,
        'admin_permissions.html', 
        {
            'user': user,
            'permissions': permissions
        }
    )


@login_required
def reports(request):
    user = request.user

    artistasMasAlbumes = custom_sql_dictfetchall(
        """
        SELECT artist.name, COUNT(*) as Cantidad FROM artist JOIN album ON artist.artistid = album.artistid
        GROUP BY artist.name ORDER BY Cantidad DESC LIMIT 5
        """
    )

    generosMasCanciones = custom_sql_dictfetchall(
        """
        SELECT genre.name, COUNT(*) as Cantidad FROM genre JOIN track ON genre.genreid = track.genreid
        GROUP BY genre.name ORDER BY Cantidad DESC LIMIT 5
        """
    )
    
    totalDuracionPlaylists = custom_sql_dictfetchall(
        """
        SELECT playlist.name, SUM(track.milliseconds) FROM playlist
        JOIN playlisttrack on playlist.playlistid = playlisttrack.playlistid
        JOIN track  on playlisttrack.trackid = track.trackid 
        GROUP BY playlist.name 
        """
    )

    cancionesMasDuracion = custom_sql_dictfetchall(
        """
        SELECT track.name, track.milliseconds as Duracion, albumArtist.name FROM track JOIN (
            SELECT album.albumid, artist.name FROM artist JOIN album ON artist.artistid = album.artistid
        ) as albumArtist ON track.albumid = albumArtist.albumid
        ORDER BY Duracion DESC LIMIT 5
        """
    )

    usuariosMasCanciones = {}

    promedioCancionPorGenero = custom_sql_dictfetchall(
        """
        SELECT genre.name, AVG(track.milliseconds) as Tiempo FROM genre JOIN track ON genre.genreid = track.genreid
        GROUP BY genre.genreid ORDER BY Tiempo DESC
        """
    )

    cantidadArtistasPlaylists = custom_sql_dictfetchall(
        """
        SELECT results.plname, COUNT(results.artist) 
        FROM (SELECT DISTINCT playlist.name as plname, artist.name as artist 
                FROM playlist 
                JOIN playlisttrack ON playlist.playlistid = playlisttrack.playlistid
                JOIN track ON playlisttrack.trackid = track.trackid 
                JOIN album ON track.albumid = album.albumid 
                JOIN artist ON album .artistid  = artist.artistid) as results 
        GROUP BY plname 
        ORDER BY COUNT(artist)
        """
    )

    # REVISAR
    artistasDiversidadGenero = custom_sql_dictfetchall(
        """
        SELECT DISTINCT artist.name, count(DISTINCT genre.genreid) FROM artist
        JOIN album on artist.artistid = album.artistid 
        JOIN track on album.albumid = track.trackid 
        JOIN genre on track.genreid = genre.genreid
        GROUP BY artist.name
        """
    )

    artistasPorGenero = custom_sql_dictfetchall(
        """
        SELECT genre.name as Genre, artistAlbumTrack.name as Artist FROM genre JOIN (
            SELECT DISTINCT artistAlbum.name, track.genreid FROM track JOIN (
                SELECT artist.name, album.albumid FROM album JOIN artist ON artist.artistid = album.artistid
            ) as artistAlbum ON track.albumid = artistAlbum.albumid
        ) as artistAlbumTrack ON genre.genreid = artistAlbumTrack.genreid
        ORDER BY Genre
        """
    )

    artistasMasCanciones = custom_sql_dictfetchall(
        """
        SELECT artist.name, COUNT(*) as Cantidad FROM artist JOIN (
            SELECT album.artistid, track.name FROM album JOIN track ON album.albumid = track.albumid
        ) as albumTrack ON artist.artistid = albumTrack.artistid
        GROUP BY artist.name ORDER BY Cantidad DESC LIMIT 5
        """
    )

    generosMasArtistas = custom_sql_dictfetchall(
        """
        SELECT genre.name as Genre, COUNT(artistAlbumTrack.name) as CantidadArtistas FROM genre JOIN (
            SELECT DISTINCT artistAlbum.name, track.genreid FROM track JOIN (
                SELECT artist.name, album.albumid FROM album JOIN artist ON artist.artistid = album.artistid
            ) as artistAlbum ON track.albumid = artistAlbum.albumid
        ) as artistAlbumTrack ON genre.genreid = artistAlbumTrack.genreid
        GROUP BY Genre ORDER BY CantidadArtistas DESC LIMIT 5
        """
    )


    return render(
        request, 
        'reports.html',
        {
            'user': user,
            "artistasMasAlbumes": artistasMasAlbumes,
            "generosMasCanciones": generosMasCanciones,
            "totalDuracionPlaylists": totalDuracionPlaylists,
            "cancionesMasDuracion": cancionesMasDuracion,
            "usuariosMasCanciones": usuariosMasCanciones,
            "promedioCancionPorGenero": promedioCancionPorGenero,
            "cantidadArtistasPlaylists": cantidadArtistasPlaylists,
            "artistasDiversidadGenero": artistasDiversidadGenero,
            "artistasMasCanciones": artistasMasCanciones,
            "generosMasArtistas": generosMasArtistas
        }
    )

def custom_sql_fetchOne(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchone()
    return data

def custom_sql_fetchAll(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
    return data

def custom_sql_dictfetchall(query):
    "Return all rows from a cursor as a dict"
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

def print_query(data):
    for item in data:
        print(item)