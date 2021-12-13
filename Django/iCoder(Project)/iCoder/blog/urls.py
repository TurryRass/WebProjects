# urls in blog
from django.urls import path
from . import views

urlpatterns = [
    # API for post comment
    path('postComment',views.postComment,name='postComment'),

    path('', views.blogHome,name='blogHome'),
    path('<str:slug>', views.blogPost,name='blogPost'),
]
