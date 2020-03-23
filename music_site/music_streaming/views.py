from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import connection

# Create your views here.

def index(request):
    print(" ~"*75)
    # GENEROS CON MAS ARTISTAS
    print('GENEROS CON MAS ARTISTAS')
    print_query(custom_sql_fetchAll(
        # """
        # SELECT genre.name as Genre, artistAlbumTrack.name as Artist FROM genre JOIN (
        #     SELECT DISTINCT artistAlbum.name, track.genreid FROM track JOIN (
        #         SELECT artist.name, album.albumid FROM album JOIN artist ON artist.artistid = album.artistid
        #     ) as artistAlbum ON track.albumid = artistAlbum.albumid
        # ) as artistAlbumTrack ON genre.genreid = artistAlbumTrack.genreid
        # ORDER BY Genre
        # """
        """
        SELECT genre.name as Genre, COUNT(artistAlbumTrack.name) as CantidadArtistas FROM genre JOIN (
            SELECT DISTINCT artistAlbum.name, track.genreid FROM track JOIN (
                SELECT artist.name, album.albumid FROM album JOIN artist ON artist.artistid = album.artistid
            ) as artistAlbum ON track.albumid = artistAlbum.albumid
        ) as artistAlbumTrack ON genre.genreid = artistAlbumTrack.genreid
        GROUP BY Genre ORDER BY CantidadArtistas DESC LIMIT 5
        """
    ))
    print(" ~"*75)
    # ARTISTAS POR GENERO
    print('ARTISTAS POR GENERO')
    print_query(custom_sql_fetchAll(
        """
        SELECT genre.name as Genre, artistAlbumTrack.name as Artist FROM genre JOIN (
            SELECT DISTINCT artistAlbum.name, track.genreid FROM track JOIN (
                SELECT artist.name, album.albumid FROM album JOIN artist ON artist.artistid = album.artistid
            ) as artistAlbum ON track.albumid = artistAlbum.albumid
        ) as artistAlbumTrack ON genre.genreid = artistAlbumTrack.genreid
        ORDER BY Genre
        """
    ))
    print(" ~"*75)
    # GENEROS CON MAS CANCIONES
    print('GENEROS CON MAS CANCIONES')
    print_query(custom_sql_fetchAll(
        """
        SELECT genre.name, COUNT(*) as Cantidad FROM genre JOIN track ON genre.genreid = track.genreid
        GROUP BY genre.name ORDER BY Cantidad DESC LIMIT 5
        """
    ))
    print(" ~"*75)
    # ARTISTAS CON MAS ALBUMES
    print('ARTISTAS CON MAS ALBUMES')
    print_query(custom_sql_fetchAll(
        """
        SELECT artist.name, COUNT(*) as Cantidad FROM artist JOIN album ON artist.artistid = album.artistid
        GROUP BY artist.name ORDER BY Cantidad DESC LIMIT 5
        """
    ))
    print(" ~"*75)
    # CANCIONES DE MAYOR DURACION Y SUS ARTISTAS
    print('CANCIONES DE MAYOR DURACION Y SUS ARTISTAS')
    print_query(custom_sql_fetchAll(
        """
        SELECT track.name, track.milliseconds as Duracion, albumArtist.name FROM track JOIN (
            SELECT album.albumid, artist.name FROM artist JOIN album ON artist.artistid = album.artistid
        ) as albumArtist ON track.albumid = albumArtist.albumid
        ORDER BY Duracion DESC LIMIT 5
        """
    ))
    print(" ~"*75)
    # USUARIOS QUE HAN REGISTRADO MAS CANCIONES
    # TODO
    print('USUARIOS QUE HAN REGISTRADO MAS CANCIONES')
    # print_query(custom_sql_fetchAll(
    #     """
    #     """
    # ))
    print(" ~"*75)
    # PROMEDIO DE DURACION DE CANCIONES POR GENERO
    print('PROMEDIO DE DURACION DE CANCIONES POR GENERO')
    print_query(custom_sql_fetchAll(
        """
        SELECT genre.name, AVG(track.milliseconds) as Tiempo FROM genre JOIN track ON genre.genreid = track.genreid
        GROUP BY genre.genreid ORDER BY Tiempo DESC
        """
    ))
    print(" ~"*75)
    # ALBUMES MAS RECIENTES
    # TODO
    print('ALBUMES MAS RECIENTES')
    print_query(custom_sql_fetchAll(
        """
        SELECT album.title FROM album 
        LIMIT 5
        """
    ))
    print(" ~"*75)
    # ARTISTAS MAS COLABORATIVOS
    print('ARTISTAS MAS COLABORATIVOS')
    print_query(custom_sql_fetchAll(
        """
        SELECT artist.name, COUNT(*) as Cantidad FROM artist JOIN (
            SELECT album.artistid, track.name FROM album JOIN track ON album.albumid = track.albumid
        ) as albumTrack ON artist.artistid = albumTrack.artistid
        GROUP BY artist.name ORDER BY Cantidad DESC LIMIT 5
        """
    ))
    print(" ~"*75)
    return redirect('accounts/login/')

@login_required
def home(request):
    user = request.user
    return render(request, 'home.html', {'user': user})

@login_required
def admin(request):
    user = request.user
    return render(request, 'admin.html', {'user': user})

@login_required
def reports(request):
    return render(request, 'reports.html')

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