from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('music/musician/<int:musician_id>/', views.musician_detail, name='musician_detail'),
    path('music/album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('music/song/<int:song_id>/', views.song_detail, name='song_detail'),
]