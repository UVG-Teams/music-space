from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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
#     try:
#         name = request.POST.get('name')
#         artist = Artist.objects.get_or_create(name = name)
#         userArtist = UserArtist.objects.create(artistid = artist.id, userid = user.id)
#     except Artist.DoesNotExist:
#         raise Http404("Artist does not exist")
#     return redirect('artists:index')

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
