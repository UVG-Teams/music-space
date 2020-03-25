from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import connection

from playlists.models import Playlist
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


# @login_required
# def create(request):
#     user = request.user
#     return render(
#         request,
#         'playlist_create.html',
#         {
#             'user' : user
#         }
#     )


# @login_required
# def create_new(request):
#     user = request.user
#     name = request.POST.get('name')
#     playlist = Playlist.objects.get_or_create(name = name)
#     userArtist = UserArtist.objects.create(playlistid = playlist[0], userid = user[0])
#     return redirect('playlists:index')    

# @login_required
# def update(request, id):
#     try:
#         artist = Artist.objects.get(pk = id)
#     except Artist.DoesNotExist:
#         raise Http404("Artist does not exist")
#     return render(
#         request,
#         'artist_edit.html',
#         {
#             'artist' : artist
#         }
#     )

# @login_required
# def update_object(request, id):
#     try:
#         name = request.POST.get('name')
#         artist = Artist.objects.filter(pk = id).update(name = name)
#     except Artist.DoesNotExist:
#         raise Http404("Artist does not exist")
#     return redirect('artists:index')

# @login_required
# def delete(request, id):
#     try:
#         artist = Artist.objects.get(pk = id)
#         artist.delete()
#     except Artist.DoesNotExist:
#         raise Http404("Artist does not exist")
#     return redirect('artists:index')
