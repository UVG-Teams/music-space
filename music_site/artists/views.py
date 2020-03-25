from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.db import connection

from artists.models import Artist
from userArtists.models import UserArtist

# Create your views here.

@login_required
def index(request):
    user = request.user
    artists = Artist.objects.all()

    if request.GET.get('Next') == 'Next':
            print('user clicked summary')

    return render(
        request,
        'artists.html', 
        {
            'user': user,
            'artists': artists
        }
    )

def detail(request, id):
    return HttpResponse("Hello World, You are at artist {id}.".format(id=id))

@login_required
def create(request):
    user = request.user
    return render(
        request,
        'artist_create.html',
        {
            'user' : user
        }
    )

@login_required
def create_new(request):
    user = request.user
    id = (Artist.objects.latest('artistid').artistid) + 1
    name = request.POST.get('name')
    try:
        artist = Artist.objects.get(name = name)
    except Artist.DoesNotExist:
        artist = Artist.objects.get_or_create(name = name, artistid = id)
        userArtist = UserArtist.objects.create(artistid = artist[0], userid = user)
    return redirect('artists:index')

@login_required
def update(request, id):
    try:
        artist = Artist.objects.get(pk = id)
    except Artist.DoesNotExist:
        raise Http404("Artist does not exist")
    return render(
        request,
        'artist_edit.html',
        {
            'artist' : artist
        }
    )

@login_required
def update_object(request, id):
    try:
        name = request.POST.get('name')
        artist = Artist.objects.filter(pk = id).update(name = name)
    except Artist.DoesNotExist:
        raise Http404("Artist does not exist")
    return redirect('artists:index')

@login_required
def delete(request, id):
    try:
        artist = Artist.objects.get(pk = id)
        artist.delete()
    except Artist.DoesNotExist:
        raise Http404("Artist does not exist")
    return redirect('artists:index')

def search(request):
    user = request.user
    search = request.POST.get('search')
    resultSearch = custom_sql_dictfetchall(
        """
        select *
        from artist
        where LOWER(name) LIKE LOWER('%{search}%');
        """.format(search=search)
    )
    return render(
        request, 
        'artists.html',
        {
            'user': user,
            'artists': resultSearch
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
