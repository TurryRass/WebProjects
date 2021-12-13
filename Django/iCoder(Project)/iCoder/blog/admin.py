from django.contrib import admin
from .models import Post
from .models import blogComment

# Register your models here.
admin.site.register((blogComment))

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        # if in below ',' is not given then we get js whose type is 'string' and not 'tuple' which we want.
        js = ('tinyInject.js',)
        # print('this is the type',type(js))
