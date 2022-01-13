from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Album,Song

# Create your views here.
def songs(request,album_id):
    album = Album.objects.get(sno=album_id)
    my_songs = Song.objects.filter(album=album)
    # print(len(my_songs[0].title))
    print(album.cover)
    params = {'songs':my_songs,'cover':album.cover}
    return render(request,'Music/m_songs_list.html',params)

