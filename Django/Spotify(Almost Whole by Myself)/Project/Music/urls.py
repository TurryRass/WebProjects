from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('songs<int:album_id>',views.songs,name='songs'),
]