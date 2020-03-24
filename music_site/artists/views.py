from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from artists.models import Artist

# Create your views here.

@login_required
def index(request):
    user = request.user
    artists = Artist.objects.all()
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
