from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='homePage'),
    # the following is 'contact/' becuase there is already 1800 and nothing(that is '' ) and so anywhere going on my website a slash will be added by default and then when i say to go to '/contact' then it faces trouble as it actually means something like this (1800//contact) which obviously cannot happen.
    path('contact/',views.Contact_user,name='contactPage'),
    path('about/',views.About,name='aboutPage'),
    path('about<str:author>',views.about_author,name='about_author'),
    path('terms-conditions/',views.Terms,name='termsPage'),
    path('policy/',views.Policy,name='policy'),
    path('account/',views.account,name='account'),
    path('signin/',views.account,name='signIn'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
]

