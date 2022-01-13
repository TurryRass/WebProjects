from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('album<int:id>',views.all_album,name='all_album'),
    path('search/',views.search,name='search'),
    path('about/',views.about,name='about'),
    path('feedback/',views.feedback,name='feedback'),
]