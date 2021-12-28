from django.shortcuts import redirect, render,HttpResponse
from .models import Post
from .models import Comment
import random
from Blog.templatetags import extras
from django.contrib import messages

# Create your views here.
def blog(request):
    all_posts = Post.objects.all()
    params = {'all_posts':all_posts}
    return render(request,'Blog/blog.html',params)

def blogPost(request,ref_no):
    post = Post.objects.filter(ref_no = ref_no).first() # [0] could have used too
    # post.viewedBy = ''
    # post.save()
    names = post.viewedBy
    new_viewer = 0
    for viewer in names.split(','):
        if request.user.username == viewer:
            print()
        else:
            new_viewer += 1
    if new_viewer == len(names.split(',')):
        post.views += 1
        try:
            if request.user.username not in post.viewedBy:
                post.viewedBy += request.user.username + ','
                post.save()
        except Exception as e:
            print()
        post.save()
        

    all_posts = list(Post.objects.all())
    also_read = random.sample(all_posts,3)
    comments = Comment.objects.filter(post = post,parent = None)
    # following are replies which are not complete and cannot be put directly but will need to be placed in a more systemataic manner
    raw_replies = Comment.objects.filter(post = post).exclude(parent = None)
    repDict = {}
    for reply in raw_replies:
        if reply.parent.sno not in repDict.keys():
            repDict[reply.parent.sno] = [reply]
        else:
            repDict[reply.parent.sno].append(reply)
    params = {'post':post,'also_read':also_read,'comments':comments,'replies':repDict}
    return render(request,'Blog/blogpost.html',params)

def year(request,year):
    all_posts = Post.objects.all()
    year_posts = []
    for post in all_posts:
        if year in str(post.timestamp):
            year_posts.append(post)
    params = {'all_posts':year_posts}
    return render(request,'Blog/blog.html',params)

def comment(request):
    if request.method == 'POST':
        content = request.POST['comment_content']
        post_id = request.POST['post_id']
        postsno = request.POST['postsno']
        post = Post.objects.get(ref_no=post_id)
        if postsno == '':
            comment = Comment(content = content,user = request.user,post = post)
            comment.save()
        else:
            parent = Comment.objects.get(sno = postsno)
            comment = Comment(content = content,user = request.user,post = post,parent = parent)
            comment.save()
        return redirect(f'/blog/{post_id}')
    return redirect('/')
