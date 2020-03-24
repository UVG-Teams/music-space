from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required

from albums.models import Album

# Create your views here.

@login_required
def index(request):
    user = request.user
    albums = Album.objects.all()
    return render(
        request,
        'albums.html', 
        {
            'user': user,
            'albums': albums
        }
    )

@login_required
def detail(request, id):
    try:
        album = Album.objects.get(pk = id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'albumDetail.html', {'album': album})
