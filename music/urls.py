from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('music/<int:song_id>/', views.detail, name='detail')
]