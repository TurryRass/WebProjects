from django.shortcuts import redirect, render 
from Blog.models import Post
from simple_search import search_filter
import time

def search(request):
    if request.method == 'GET':
        try:
            start_time = time.time()
            search_fields = ['title','author','timestamp','content']
            query = request.GET['query']
            search_posts = Post.objects.filter(search_filter(search_fields,query))
            timeout = str(time.time() - start_time)
            # statements for the posts
            allow_posts = False # this is boolean for to show yes or no results on searach.html template 
            len_posts = len(search_posts)
            len_query = len(query)
            # conditions for false and true of allow_posts
            vote1,vote2,vote3 = False,False,False
            if len_posts > 0:
                vote1 = True 
            if len_query > 0:
                vote2 = True
            if len_query < 72:
                vote3 = True
            if vote1 and vote2 and vote3:
                allow_posts = True
            else:
                if not vote2:
                    query = 'was nothing and'
            params = {'search_posts':search_posts,'query':query,'timeout':timeout,'allow_posts':allow_posts}
            return render(request,'search.html',params)
        except:
            return redirect('/')
    else:
        redirect('/')
    return render(request,'search.html')