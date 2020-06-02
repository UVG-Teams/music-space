from django.urls import path

from . import views

app_name = 'reports'
urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.reports, name='all'),
    path('sales/', views.get_sales_on, name='sales'),
    path('simulacion/', views.simulacion, name='simulacion'),
    path('generosMasArtistas/', views.archivo_csv_generosMasArtistas, name='generosMasArtistas'),
    path('artistasMasCanciones/', views.archivo_csv_artistasMasCanciones, name='artistasMasCanciones'),
    path('artistasDiversidadGenero/', views.archivo_csv_artistasDiversidadGenero, name='artistasDiversidadGenero'),
    path('cantidadArtistasPlaylists/', views.archivo_csv_cantidadArtistasPlaylists, name='cantidadArtistasPlaylists'),
    path('promedioCancionPorGenero/', views.archivo_csv_promedioCancionPorGenero, name='promedioCancionPorGenero'),
    path('usuariosMasCanciones/', views.archivo_csv_usuariosMasCanciones, name='usuariosMasCanciones'),
    path('cancionesMasDuracion/', views.archivo_csv_cancionesMasDuracion, name='cancionesMasDuracion'),
    path('totalDuracionPlaylists/', views.archivo_csv_totalDuracionPlaylists, name='totalDuracionPlaylists'),
    path('generosMasCanciones/', views.archivo_csv_generosMasCanciones, name='generosMasCanciones'),
    path('artistasMasAlbumes/', views.archivo_csv_artistasMasAlbumes, name='artistasMasAlbumes'),
    path('ventasPorSemana/', views.ventas_por_semana, name='ventasPorSemana'),
    path('artistasMayoresVentas/', views.artistas_mayores_ventas, name='artistasMayoresVentas'),
    path('ventasPorGenero/', views.ventas_Por_Genero, name='ventasPorGenero'),
    path('cancionesMasReproducciones/', views.canciones_Mas_Reproducciones, name='cancionesMasReproducciones'),
    path('ventasPorSemana_csv', views.csv_ventas_por_semana, name='ventasPorSemana_csv'),
    path('artistasMayoresVentas_csv/', views.csv_Artistas_mayores_ventas, name='artistasMayoresVentas_csv'),
    path('ventasPorGenero_csv/', views.csv_ventas_Por_Genero, name='ventasPorGenero_csv'),
    path('cancionesMasReproducciones_csv/', views.csv_Canciones_Mas_Reproducciones, name='cancionesMasReproducciones_csv'),
]