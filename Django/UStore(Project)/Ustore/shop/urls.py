from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.index,name="home"),
    path('tracker/',views.tracker,name='tracker'),
    path('search/',views.search,name='search'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('products/<int:myid>',views.productView,name='productView'),
    path('checkout/',views.checkOut,name='checkOut'),
    # path('handlerequest/',views.handlerequest,name='HandleRequest')
    # path('account',views.account,name='account'),
    # path('create',views.create,name='create'),
    # path('log',views.log,name='log')
]
