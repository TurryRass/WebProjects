from django.shortcuts import render
from .models import Blogpost

# Create your views here.
def index(request):
    blogpost = Blogpost.objects.all()
    for i in blogpost:
        print(blogpost)
        print(i)
    params = {'blogpost':blogpost}
    return render(request,'blog/index.html',params)

def blogpost(request,id):
    post = Blogpost.objects.filter(post_id = id)
    len_list = len(Blogpost.objects.all()) + 2
    return render(request,'blog/blogpost.html',{'post':post[0],'len_list':len_list})