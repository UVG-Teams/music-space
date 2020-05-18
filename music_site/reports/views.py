from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import connection
import csv

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
    artistasMasAlbumes = artistas_Mas_Albumes()
    generosMasCanciones = generos_Mas_Canciones()
    totalDuracionPlaylists = total_Duracion_Playlists()
    cancionesMasDuracion = canciones_Mas_Duracion()
    usuariosMasCanciones = usuarios_Mas_Canciones()
    promedioCancionPorGenero = promedio_Cancion_Por_Genero()
    cantidadArtistasPlaylists = cantidad_Artistas_Playlists()
    artistasDiversidadGenero = artistas_Diversidad_Genero()
    artistasMasCanciones = artistas_Mas_Canciones()
    generosMasArtistas = generos_Mas_Artistas()
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

def artistas_Mas_Albumes():
    artistasMasAlbumes = custom_sql_dictfetchall(
        """
        SELECT artist.name, COUNT(*) as Cantidad FROM artist JOIN album ON artist.artistid = album.artistid
        GROUP BY artist.name ORDER BY Cantidad DESC LIMIT 5
        """
    )
    return(artistasMasAlbumes)

def archivo_csv_artistasMasAlbumes(request):
    artistasMasAlbumes = artistas_Mas_Albumes()
    # Generar y guardar la info del query "generosmas artistas" en archivo CSV
    with open('static/artistas_Mas_Albumes.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        # header del archivo
        wr.writerow(["Artistas", "Cantidad"])
        # obtener la info
        for item in artistasMasAlbumes:
            item['name']
            wr.writerow([item['name'], item['cantidad']])
    
    #leer el archivo y descargarlo
    with open('static/artistas_Mas_Albumes.csv', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['status_code'] = 200
        response['Content-Disposition'] = 'attachment; filename="artistas_Mas_Albumes.csv"'
        
    return response

def generos_Mas_Canciones():
    generosMasCanciones = custom_sql_dictfetchall(
        """
        SELECT genre.name, COUNT(*) as Cantidad FROM genre JOIN track ON genre.genreid = track.genreid
        GROUP BY genre.name ORDER BY Cantidad DESC LIMIT 5
        """
    )
    return(generosMasCanciones)

def archivo_csv_generosMasCanciones(request):
    generosMasCanciones = generos_Mas_Canciones()
    # Generar y guardar la info del query "generosmas artistas" en archivo CSV
    with open('static/generos_Mas_Canciones.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        # header del archivo
        wr.writerow(["Genero", "Cantidad"])
        # obtener la info
        for item in generosMasCanciones:
            item['name']
            wr.writerow([item['name'], item['cantidad']])
    
    #leer el archivo y descargarlo
    with open('static/generos_Mas_Canciones.csv', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['status_code'] = 200
        response['Content-Disposition'] = 'attachment; filename="generos_Mas_Canciones.csv"'
        
    return response

def total_Duracion_Playlists():
    totalDuracionPlaylists = custom_sql_dictfetchall(
        """
        SELECT playlist.name, SUM(track.milliseconds) as Tiempo FROM playlist
        JOIN playlisttrack on playlist.playlistid = playlisttrack.playlistid
        JOIN track  on playlisttrack.trackid = track.trackid 
        GROUP BY playlist.name ORDER BY Tiempo DESC
        """
    )
    return(totalDuracionPlaylists)

def archivo_csv_totalDuracionPlaylists(request):
    totalDuracionPlaylists = total_Duracion_Playlists()
    # Generar y guardar la info del query "generosmas artistas" en archivo CSV
    with open('static/total_Duracion_Playlists.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        # header del archivo
        wr.writerow(["Playlist", "Tiempo"])
        # obtener la info
        for item in totalDuracionPlaylists:
            item['name']
            wr.writerow([item['name'], item['tiempo']])
    
    #leer el archivo y descargarlo
    with open('static/total_Duracion_Playlists.csv', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['status_code'] = 200
        response['Content-Disposition'] = 'attachment; filename="total_Duracion_Playlists.csv"'
        
    return response

def canciones_Mas_Duracion():
    cancionesMasDuracion = custom_sql_dictfetchall(
        """
        SELECT track.name, track.milliseconds as Duracion, albumArtist.name FROM track JOIN (
            SELECT album.albumid, artist.name FROM artist JOIN album ON artist.artistid = album.artistid
        ) as albumArtist ON track.albumid = albumArtist.albumid
        ORDER BY Duracion DESC LIMIT 5
        """
    )
    return(cancionesMasDuracion)

def archivo_csv_cancionesMasDuracion(request):
    cancionesMasDuracion = canciones_Mas_Duracion()
    # Generar y guardar la info del query "generosmas artistas" en archivo CSV
    with open('static/canciones_Mas_Duracion.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        # header del archivo
        wr.writerow(["artistas", "Cantidad de albumes"])
        # obtener la info
        for item in cancionesMasDuracion:
            item['name']
            wr.writerow([item['name'], item['duracion']])
    
    #leer el archivo y descargarlo
    with open('static/canciones_Mas_Duracion.csv', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['status_code'] = 200
        response['Content-Disposition'] = 'attachment; filename="canciones_Mas_Duracion.csv"'
        
    return response

def usuarios_Mas_Canciones():
    usuariosMasCanciones = custom_sql_dictfetchall(
        """
        SELECT username, COUNT(*) as Cantidad 
        FROM usertrack JOIN auth_user ON usertrack.userid = auth_user.id
        GROUP BY username ORDER BY Cantidad DESC LIMIT 5
        """
    )
    return(usuariosMasCanciones)

def archivo_csv_usuariosMasCanciones(request):
    usuariosMasCanciones = usuarios_Mas_Canciones()
    # Generar y guardar la info del query "generosmas artistas" en archivo CSV
    with open('static/usuarios_Mas_Canciones.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        # header del archivo
        wr.writerow(["artistas", "Cantidad de albumes"])
        # obtener la info
        for item in usuariosMasCanciones:
            item['username']
            wr.writerow([item['username'], item['cantidad']])
    
    #leer el archivo y descargarlo
    with open('static/usuarios_Mas_Canciones.csv', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['status_code'] = 200
        response['Content-Disposition'] = 'attachment; filename="usuarios_Mas_Canciones.csv"'
        
    return response

def promedio_Cancion_Por_Genero():
    promedioCancionPorGenero = custom_sql_dictfetchall(
        """
        SELECT genre.name, AVG(track.milliseconds) as Tiempo FROM genre JOIN track ON genre.genreid = track.genreid
        GROUP BY genre.genreid ORDER BY Tiempo DESC
        """
    )
    return(promedioCancionPorGenero)

def archivo_csv_promedioCancionPorGenero(request):
    promedioCancionPorGenero = promedio_Cancion_Por_Genero()
    # Generar y guardar la info del query "generosmas artistas" en archivo CSV
    with open('static/promedio_Cancion_Por_Genero.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        # header del archivo
        wr.writerow(["artistas", "Cantidad de albumes"])
        # obtener la info
        for item in promedioCancionPorGenero:
            item['name']
            wr.writerow([item['name'], item['tiempo']])
    
    #leer el archivo y descargarlo
    with open('static/promedio_Cancion_Por_Genero.csv', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['status_code'] = 200
        response['Content-Disposition'] = 'attachment; filename="promedio_Cancion_Por_Genero.csv"'
        
    return response

def cantidad_Artistas_Playlists():
    cantidadArtistasPlaylists = custom_sql_dictfetchall(
        """
        SELECT results.plname as name, COUNT(results.artist) as cantidad
        FROM (SELECT DISTINCT playlist.name as plname, artist.name as artist 
                FROM playlist 
                JOIN playlisttrack ON playlist.playlistid = playlisttrack.playlistid
                JOIN track ON playlisttrack.trackid = track.trackid 
                JOIN album ON track.albumid = album.albumid 
                JOIN artist ON album .artistid  = artist.artistid) as results 
        GROUP BY name
        ORDER BY cantidad DESC
        """
    )
    return(cantidadArtistasPlaylists)

def archivo_csv_cantidadArtistasPlaylists(request):
    cantidadArtistasPlaylists = cantidad_Artistas_Playlists()
    # Generar y guardar la info del query "generosmas artistas" en archivo CSV
    with open('static/cantidad_Artistas_Playlists.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        # header del archivo
        wr.writerow(["artistas", "Cantidad de albumes"])
        # obtener la info
        for item in cantidadArtistasPlaylists:
            item['name']
            wr.writerow([item['name'], item['cantidad']])
    
    #leer el archivo y descargarlo
    with open('static/cantidad_Artistas_Playlists.csv', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['status_code'] = 200
        response['Content-Disposition'] = 'attachment; filename="cantidad_Artistas_Playlists.csv"'
        
    return response

def artistas_Diversidad_Genero():
    artistasDiversidadGenero = custom_sql_dictfetchall(
        """
        SELECT DISTINCT artist.name, count(DISTINCT genre.genreid) as Cantidad FROM artist
        JOIN album on artist.artistid = album.artistid 
        JOIN track on album.albumid = track.trackid 
        JOIN genre on track.genreid = genre.genreid
        GROUP BY artist.name ORDER BY Cantidad DESC LIMIT 5
        """
    )
    return(artistasDiversidadGenero)

def archivo_csv_artistasDiversidadGenero(request):
    artistasDiversidadGenero = artistas_Diversidad_Genero()
    # Generar y guardar la info del query "generosmas artistas" en archivo CSV
    with open('static/artistas_Diversidad_Genero.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        # header del archivo
        wr.writerow(["artistas", "Cantidad de albumes"])
        # obtener la info
        for item in artistasDiversidadGenero:
            item['name']
            wr.writerow([item['name'], item['cantidad']])
    
    #leer el archivo y descargarlo
    with open('static/artistas_Diversidad_Genero.csv', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['status_code'] = 200
        response['Content-Disposition'] = 'attachment; filename="artistas_Diversidad_Genero.csv"'
        
    return response

def artistas_Mas_Canciones():
    artistasMasCanciones = custom_sql_dictfetchall(
        """
        SELECT artist.name, COUNT(*) as Cantidad FROM artist JOIN (
            SELECT album.artistid, track.name FROM album JOIN track ON album.albumid = track.albumid
        ) as albumTrack ON artist.artistid = albumTrack.artistid
        GROUP BY artist.name ORDER BY Cantidad DESC LIMIT 5
        """
    )
    return(artistasMasCanciones)

def archivo_csv_artistasMasCanciones(request):
    artistasMasCanciones = artistas_Mas_Canciones()
    # Generar y guardar la info del query "generosmas artistas" en archivo CSV
    with open('static/artistas_Mas_Canciones.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        # header del archivo
        wr.writerow(["artistas", "Cantidad de albumes"])
        # obtener la info
        for item in artistasMasCanciones:
            item['name']
            wr.writerow([item['name'], item['cantidad']])
    
    #leer el archivo y descargarlo
    with open('static/artistas_Mas_Canciones.csv', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['status_code'] = 200
        response['Content-Disposition'] = 'attachment; filename="artistas_Mas_Canciones.csv"'
        
    return response

def generos_Mas_Artistas():
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
    return(generosMasArtistas)

def archivo_csv_generosMasArtistas(request):
    generosMasArtistas = generos_Mas_Artistas()
    # Generar y guardar la info del query "generosmas artistas" en archivo CSV
    with open('static/generos_Mas_Artistas.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        # header del archivo
        wr.writerow(["artistas", "Cantidad de albumes"])
        # obtener la info
        for item in generosMasArtistas:
            item['genre']
            wr.writerow([item['genre'], item['cantidadartistas']])
    
    #leer el archivo y descargarlo
    with open('static/generos_Mas_Artistas.csv', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['status_code'] = 200
        response['Content-Disposition'] = 'attachment; filename="generos_Mas_Artistas.csv"'
        
    return response

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
    # return JsonResponse(data)
    return redirect('reports:index')


