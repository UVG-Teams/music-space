from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from pymongo import MongoClient

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
