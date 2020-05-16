from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import connection

from mongoServices.services import save_sales_on_mongo

# Create your views here.

@login_required
def index(request):
    user = request.user
    return render(
        request, 
        'reports.html',
        {
            'user': user,
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
        SELECT playlist.name, SUM(track.milliseconds) as Tiempo FROM playlist
        JOIN playlisttrack on playlist.playlistid = playlisttrack.playlistid
        JOIN track  on playlisttrack.trackid = track.trackid 
        GROUP BY playlist.name ORDER BY Tiempo DESC
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

    usuariosMasCanciones = custom_sql_dictfetchall(
        """
        SELECT username, COUNT(*) as Cantidad 
        FROM usertrack JOIN auth_user ON usertrack.userid = auth_user.id
        GROUP BY username ORDER BY Cantidad DESC LIMIT 5
        """
    )

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
        ORDER BY COUNT(artist) DESC
        """
    )

    # REVISAR
    artistasDiversidadGenero = custom_sql_dictfetchall(
        """
        SELECT DISTINCT artist.name, count(DISTINCT genre.genreid) as Cantidad FROM artist
        JOIN album on artist.artistid = album.artistid 
        JOIN track on album.albumid = track.trackid 
        JOIN genre on track.genreid = genre.genreid
        GROUP BY artist.name ORDER BY Cantidad DESC LIMIT 5
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
        'allreports.html',
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
def get_sales_on(request):
    date = request.POST.get('date')
    data = {
        'status': 'ok',
        'date': date,
        'sales': custom_sql_dictfetchall(
            """
            SELECT invoicedate, total, firstname, lastname, phone, email, country, address FROM invoice JOIN customer
                on invoice.customerid = customer.customerid
            WHERE invoicedate = '{date}'
            """.format(
                date = date
                )
            )
    }

    collection = 'compras_clientes'
    save_sales_on_mongo(collection, data)
    return JsonResponse(data)
