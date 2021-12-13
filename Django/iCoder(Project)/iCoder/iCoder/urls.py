"""iCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

admin.site.site_header = "iCoder Admin"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "iCoder"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('search/',views.search,name='search'),
    # since we are using post request for the following paths so we don't need to put a / in the below path as has been the case in the above paths.
    path('signUp',views.handleSignUp,name="signUp"),
    path('login',views.handleLogin,name="login"),
    path('logout',views.handleLogout,name="logout"),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

# in above static actually is also removing the path till /media/ in the document_root and then is joining this path to the settings.URL = /media/ and this is how we are able to get that path of the file.
