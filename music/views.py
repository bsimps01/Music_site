from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    context = {
        'song': Song.objects.all()
    }
    return render(request, 'home.html', context)


def detail(request, song_id):
    context = {
        'song': Song.objects.get(id=music_id)
    }
    return render(request, 'detail.html', context)