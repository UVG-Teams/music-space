from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from pymongo import MongoClient
import random

from userTracks.models import UserTrack
from tracks.models import Track
from django.contrib.auth.models import User
from mongoServices.services import save_recommendations_on_mongo

# Create your views here.

client = MongoClient()
db = client.music_space

@login_required
def index(request):
    user = request.user
    return render(
        request, 
        'mongo.html',
        {
            'user': user,
        }
    )

@login_required
def print_collection(request):
    collection = request.POST.get('collection')
    data = { collection : [] }

    for x in db[collection].find():
        x['_id'] = str(x['_id'])
        data[collection].append(x)
    
    return JsonResponse(data)

@login_required
def empty_collection(request):
    collection = request.POST.get('collection')
    db[collection].delete_many({})
    return redirect('mongo:index')

@login_required
def recomendacion(request):
    userTracks = UserTrack.objects.filter(relation = 'uploaded').order_by('userid', '-id').distinct('userid')[:25]

    data = {}
    if len(list(userTracks)) < 10:
        random_userTracks = random.sample(list(userTracks), len(list(userTracks)))
    else:
        random_userTracks = random.sample(list(userTracks), 10)

    for usertrack in random_userTracks:
        user = usertrack.userid
        track = usertrack.trackid
        album = track.albumid
        composer = track.composer
        genre = track.genreid

        recommendedtracks = Track.objects.filter(
            # albumid=album,
            genreid=genre,
            composer=composer
        )[:60]

        recommendedtracks2 = Track.objects.filter(
            genreid=genre,
        )[:40]

        merge_recommendations = list(recommendedtracks) + list(recommendedtracks2)
        random_recommendation = random.sample(merge_recommendations, 5)

        data.update({user.username: [{"name":track.name, "composer":track.composer} for track in random_recommendation]})

    save_recommendations_on_mongo('recommendations', data)

    return JsonResponse(data)

