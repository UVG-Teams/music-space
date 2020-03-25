from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import connection

from genres.models import Genre
from userGenres.models import UserGenre

# Create your views here.

def index(request):
    user = request.user
    genres = Genre.objects.all()
    return render(
        request,
        'genres.html', 
        {
            'user': user,
            'genres': genres
        }
    )

def detail(request, id):
    return HttpResponse("Hello World, You are at genre {id}.".format(id=id))

@login_required
def create(request):
    user = request.user
    return render(
        request,
        'genre_create.html',
        {
            'user' : user
        }
    )

@login_required
def create_new(request):
    user = request.user
    name = request.POST.get('name')
    genre = Genre.objects.get_or_create(name = name)
    userGenre = UserGenre.objects.create(genreid = genre[0], userid = user[0])
    return redirect('genres:index')

@login_required
def update(request, id):
    try:
        genre = Genre.objects.get(pk = id)
    except Genre.DoesNotExist:
        raise Http404("Genre does not exist")
    return render(
        request,
        'genre_edit.html',
        {
            'genre' : genre
        }
    )

@login_required
def update_object(request, id):
    try:
        name = request.POST.get('name')
        genre = Genre.objects.filter(pk = id).update(name = name)
    except Genre.DoesNotExist:
        raise Http404("Genre does not exist")
    return redirect('genres:index')

@login_required
def delete(request, id):
    try:
        genre = Genre.objects.get(pk = id)
        genre.delete()
    except Genre.DoesNotExist:
        raise Http404("Genre does not exist")
    return redirect('genres:index')

def search(request):
    user = request.user
    search = request.POST.get('search')
    resultSearch = custom_sql_dictfetchall(
        """
        select *
        from genre
        where LOWER(name) LIKE LOWER('%{search}%');
        """.format(search=search)
    )
    return render(
        request, 
        'genres.html',
        {
            'user': user,
            'genres': resultSearch
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

