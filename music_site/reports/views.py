from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.db import connection
import csv
import json

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
        SELECT artist.name, COUNT(*) as Cantidad FROM artist JOIN album ON artist.id = album.artistid
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
        JOIN playlisttrack on playlist.id = playlisttrack.playlistid
        JOIN track  on playlisttrack.trackid = track.id 
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
            SELECT album.id, artist.name FROM artist JOIN album ON artist.id = album.artistid
        ) as albumArtist ON track.albumid = albumArtist.id
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
        wr.writerow(["Track", "Duracion"])
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
        wr.writerow(["Usuario", "Cantidad"])
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
        wr.writerow(["Genero", "Tiempo"])
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
                JOIN playlisttrack ON playlist.id = playlisttrack.playlistid
                JOIN track ON playlisttrack.trackid = track.id 
                JOIN album ON track.albumid = album.id 
                JOIN artist ON album .artistid  = artist.id) as results 
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
        wr.writerow(["artistas", "Cantidad"])
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
        JOIN album on artist.id = album.artistid 
        JOIN track on album.id = track.id 
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
        wr.writerow(["artistas", "Cantidad"])
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
            SELECT album.artistid, track.name FROM album JOIN track ON album.id = track.albumid
        ) as albumTrack ON artist.id = albumTrack.artistid
        GROUP BY artist.name ORDER BY Cantidad DESC LIMIT 5
        """
    )
    return(artistasMasCanciones)

@login_required
def ventas_por_semana(request):
    inicio= request.GET.get('fecha_inicio_a')
    inicio += ' 00:00:00'
    fin = request.GET.get('fecha_fin_a')
    fin += ' 00:00:00'
    queryd = "SELECT weeknumber as col1, total_semana as col2 FROM ventas_semana('{0}', '{1}')".format(inicio, fin)
    ventasPorSemana = custom_sql_dictfetchall(queryd)
    titulo="Total de ventas por semana"
    columna1="Semana"
    columna2="Total"
    what_cvs_is = "a"
    context = {
        "object_list": ventasPorSemana,
        "titulo": titulo,
        "columna1": columna1,
        "columna2": columna2
    }
    # Generar y guardar la info del query "generosmas artistas" en archivo CSV
    with open('static/ventas_por_semana.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        # header del archivo
        wr.writerow(["Semana", "Total"])
        # obtener la info
        for item in ventasPorSemana:
            wr.writerow([item['col1'], item['col2']])
    return render(request, 'reporteria.html',context)

def csv_ventas_por_semana(request):
    #leer el archivo y descargarlo
    with open('static/ventas_por_semana.csv', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['status_code'] = 200
        response['Content-Disposition'] = 'attachment; filename="ventas_por_semana.csv"'
    return response

def artistas_mayores_ventas(request):
    inicio= request.GET.get('fecha_inicio')
    inicio += ' 00:00:00'
    fin = request.GET.get('fecha_fin')
    fin += ' 00:00:00'
    n = request.GET.get('limit')
    queryd = "SELECT artist_name as col1, total as col2 FROM artistas_mayores_ventas('{0}', '{1}', {2})".format(inicio, fin, n)
    titulo="Artistas con mayores ventas"
    columna1="Artista"
    columna2="Total"
    artistasMayoresVentas = custom_sql_dictfetchall(queryd)
    context = {
        "object_list": artistasMayoresVentas,
        "titulo": titulo,
        "columna1": columna1,
        "columna2": columna2
    }
     # Generar y guardar la info del query "generosmas artistas" en archivo CSV
    with open('static/Artistas_mayores_ventas.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        # header del archivo
        wr.writerow(["Artista", "Total"])
        # obtener la info
        for item in artistasMayoresVentas:
            wr.writerow([item['col1'], item['col2']])
    return render(request, 'reporteria.html', context)

def csv_Artistas_mayores_ventas(request):
    #leer el archivo y descargarlo
    with open('static/Artistas_mayores_ventas.csv', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['status_code'] = 200
        response['Content-Disposition'] = 'attachment; filename="Artistas_mayores_ventas.csv"'
    return response


def ventas_Por_Genero(request):
    inicio= request.GET.get('fecha_inicio_g')
    inicio += ' 00:00:00'
    fin = request.GET.get('fecha_fin_g')
    fin += ' 00:00:00'
    queryd = "SELECT genero as col1, total as col2 FROM ventas_por_genero('{0}', '{1}')".format(inicio, fin)
    titulo="Ventas por genero"
    columna1="Genero"
    columna2="Total"
    ventasPorGenero = custom_sql_dictfetchall(queryd)
    context = {
        "object_list": ventasPorGenero,
        "titulo": titulo,
        "columna1": columna1,
        "columna2": columna2
    }
    # Generar y guardar la info del query "generosmas artistas" en archivo CSV
    with open('static/ventas_Por_Genero.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        # header del archivo
        wr.writerow(["Genero", "Total"])
        # obtener la info
        for item in ventasPorGenero:
            wr.writerow([item['col1'], item['col2']])
    return render(request, 'reporteria.html', context)

def csv_ventas_Por_Genero(request):
    #leer el archivo y descargarlo
    with open('static/ventas_Por_Genero.csv', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['status_code'] = 200
        response['Content-Disposition'] = 'attachment; filename="ventas_Por_Genero.csv"'
    return response

def canciones_Mas_Reproducciones(request):
    artista = request.GET.get('artista')
    numero = request.GET.get('numero')
    querye = "SELECT cancion as col1, total as col2 FROM canciones_con_mas_reproducciones('{0}', {1})".format(artista, numero)
    titulo="Canciones mas reproducidas"
    columna1="Cancion"
    columna2="Total"
    cancionesMasReproducciones = custom_sql_dictfetchall(querye)
    context = {
        "object_list": cancionesMasReproducciones,
        "titulo": titulo,
        "columna1": columna1,
        "columna2": columna2
    }
    # Generar y guardar la info del query "generosmas artistas" en archivo CSV
    with open('static/Canciones_Mas_Reproducciones.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        # header del archivo
        wr.writerow(["Cancion", "Total"])
        # obtener la info
        for item in cancionesMasReproducciones:
            wr.writerow([item['col1'], item['col2']])
    return render(request, 'reporteria.html', context)

def csv_Canciones_Mas_Reproducciones(request):
    #leer el archivo y descargarlo
    with open('static/Canciones_Mas_Reproducciones.csv', 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="text/csv")
        response['status_code'] = 200
        response['Content-Disposition'] = 'attachment; filename="Canciones_Mas_Reproducciones.csv"'
    return response

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
                SELECT artist.name, album.id FROM album JOIN artist ON artist.id = album.artistid
            ) as artistAlbum ON track.albumid = artistAlbum.id
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
        wr.writerow(["Genero", "Cantidad"])
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


