from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.db import connection

from tracks.models import Track
from genres.models import Genre
from albums.models import Album
from userTracks.models import UserTrack
from shoppingcarts.models import ShoppingCart, CartItem

# Create your views here.

@login_required
def index(request):
    user = request.user
    tracks = Track.objects.all()
    return render(
        request,
        'tracks.html', 
        {
            'user': user,
            'tracks': tracks
        }
    )

def detail(request, id):
    return HttpResponse("Hello World, You are at track {id}.".format(id=id))

@login_required
def create(request):
    user = request.user
    return render(
        request,
        'track_create.html',
        {
            'user' : user
        }
    )

@login_required
def create_new(request):
    user = request.user
    id = (Track.objects.latest('id').id) + 1
    name = request.POST.get('name')
    albumTitle = request.POST.get('albumTitle')
    genreName = request.POST.get('genreName')
    composer = request.POST.get('composer')
    milliseconds = request.POST.get('milliseconds')
    unitprice = 0.9
    url = "https://www.youtube.com/results?search_query=" + name
    
    try:
        album = Album.objects.get(title = albumTitle)
        try:
            genre = Genre.objects.get(name = genreName)
            try:
                track = Track.objects.get(name = name)
            except Track.DoesNotExist:
                if (user.has_perm('track.add_track')):
                    track = Track.objects.get_or_create(
                        name = name,
                        albumid = album,
                        genreid = genre,
                        composer = composer,
                        milliseconds = milliseconds,
                        unitprice = unitprice,
                        id = id,
                        url = url
                    )
                else:
                    raise Http404('No tiene permiso')
                userTrack = UserTrack.objects.create(trackid = track[0], userid = user)
        except Genre.DoesNotExist:
            raise Http404("Can't add a track without a registred genre")    
    except Album.DoesNotExist:
        raise Http404("Can't add a track without a registred album")
    return redirect('tracks:index')

@login_required
def update(request, id):
    try:
        track = Track.objects.get(pk = id)
    except Track.DoesNotExist:
        raise Http404("Track does not exist")
    return render(
        request,
        'track_edit.html',
        {
            'track' : track
        }
    )

@login_required
def update_object(request, id):
    user = request.user
    try:
        name = request.POST.get('name')
        albumTitle = request.POST.get('albumTitle')
        genreName = request.POST.get('genreName')
        composer = request.POST.get('composer')
        milliseconds = request.POST.get('milliseconds')
        unitprice = 0.9
        active = True if request.POST.get('active') else False
        album = Album.objects.get_or_create(title = albumTitle)
        genre = Genre.objects.get_or_create(name = genreName)
        if (user.has_perm('track.change_track')):
            track = Track.objects.filter(pk = id).update(
                name = name,
                albumid = album[0],
                genreid = genre[0],
                composer = composer,
                milliseconds = milliseconds,
                unitprice = unitprice,
                active = active
            )       
        else:
            raise Http404('No tiene permiso')
    except Track.DoesNotExist:
        raise Http404("Track does not exist")
    return redirect('tracks:index')

@login_required
def delete(request, id):
    user = request.user
    try:
        if (user.has_perm('track.delete_track')):
            track = Track.objects.get(pk = id)
            track.delete()
        else:
            raise Http404('No tiene permiso')
    except Track.DoesNotExist:
        raise Http404("Track does not exist")
    return redirect('tracks:index')

@login_required
def buy(request, id):
    user = request.user
    try:
        track = Track.objects.get(pk = id)
        add_to_cart(user, track)
    except Track.DoesNotExist:
        raise Http404("Track does not exist")
    return redirect('tracks:index')

def add_to_cart(user, track):
    shoppingCart = ShoppingCart.objects.filter(user = user.id).first()
    if not shoppingCart:
        shoppingCart = ShoppingCart.objects.create(
            user = user,
            total = 0
        )
    
    if (track not in [cartitem.item for cartitem in shoppingCart.cartitem_set.all()]):
        shoppingCart.total += track.unitprice
        shoppingCart.save()
        cartItem = CartItem.objects.create(
            cart = shoppingCart,
            item = track
        )


def search(request):
    user = request.user
    search = request.POST.get('search')
    resultSearch = custom_sql_dictfetchall(
        """
        select *
        from track
        where LOWER(name) LIKE LOWER('%{search}%');
        """.format(search=search)
    )
    return render(
        request, 
        'tracks.html',
        {
            'user': user,
            'tracks': resultSearch
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

