from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.blog,name='blogPage'),
    path('<int:ref_no>',views.blogPost,name='blogPostPage'),
    path('year<str:year>/',views.year,name='year'),
    path('comment/',views.comment,name='comment'),
    # path('blog/ear2019',views.year,name='year'),
    # path('/blog/year<str:year>',views.year,name='year')
]
