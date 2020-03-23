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

@login_required
def admin(request):
    user = request.user
    users = User.objects.all()
    return render(
        request,
        'admin.html', 
        {
            'user': user,
            'users': users
        }
    )

@login_required
def admin_artists(request):
    user = request.user
    artists = Artist.objects.all()
    return render(
        request,
        'admin_artistas.html', 
        {
            'user': user,
            'artists': artists
        }
    )

@login_required
def admin_albums(request):
    user = request.user
    albums = Album.objects.all()
    return render(
        request,
        'admin_albums.html', 
        {
            'user': user,
            'albums': albums
        }
    )

@login_required
def admin_tracks(request):
    user = request.user
    tracks = Track.objects.all()
    return render(
        request,
        'admin_canciones.html', 
        {
            'user': user,
            'tracks': tracks
        }
    )

@login_required
def admin_playlists(request):
    user = request.user
    playlists = Playlist.objects.all()
    return render(
        request,
        'admin_canciones.html', 
        {
            'user': user,
            'playlists': playlists
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
    
    totalDuracionPlaylists = {}

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

    cantidadArtistasPlaylists = {}

    artistasDiversidadGenero = {}

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