
from django.shortcuts import render,redirect,HttpResponse
from Music.models import Album,Song
from .models import Feedback
from Music.templatetags import extras
import random
from simple_search import search_filter

# Create your views here.
def home(request):
    albums = Album.objects.all()
    categories = set()
    original_albums = []
    # print(type(category))
    for album in albums:
        categories.add(album.category)
    for category in categories:
        take_albums = random.sample(list(Album.objects.filter(category=category)),3)
        original_albums.append(take_albums)
    # print(len(original_albums))
    params = {'albums':original_albums,'categories':list(categories)}
    return render(request,'Home/home.html',params)

def all_album(request,id):
    albums = Album.objects.all()
    categories = set()
    original_albums = []
    for album in albums:
        categories.add(album.category)
    categories = list(categories)
    for category in categories:
        take_albums = Album.objects.filter(category=category)
        original_albums.append(take_albums)
    params = {'albums':original_albums[id-1]}
    return render(request,'Home/all_album.html',params)

def search(request):
    if request.method == 'POST':
        query = request.POST['query']
    
        if query == '':
            return redirect('/')
        else:
            if len(query) < 35:
                filter_fields1 = ['title','singer','category']
                filter_fields2 = ['title','singer']
                all_results = set()
                albums = Album.objects.filter(search_filter(filter_fields1,query))
            
                songs = Song.objects.filter(search_filter(filter_fields2,query))
                for album in albums:
                    all_results.add(album)

                if len(songs)!=0:
                    for song in songs:
                        print('album',song.album)
                        all_results.add(song.album)
            
                params = {'all_results':list(all_results),'query':query}
                return render(request,'search.html',params)
            else:
                params = {'query':query}
                return render(request,'search.html',params)
    return redirect('/')

def about(request):
    return render(request,'Home/about.html')

def feedback(request):
    if request.method == "POST":
        username = request.POST['username']
        useremail = request.POST['useremail']
        feedback = request.POST['feedback']
        user = Feedback(username = username,useremail = useremail,feedback = feedback)
        user.save()
        return redirect('/')
    return render(request,'Home/feedback.html')
