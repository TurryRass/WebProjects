from django.shortcuts import redirect, render,HttpResponse
from .models import Post,blogComment
from django.contrib import messages

# The below is not required as simply it is of no use here and this is true.
# from blog.templatetags import extras

# what request is the information that the django has brought from the request for a page by the client and just djanog then gets this data from the server and sends it as request parameter to the called django function in views according to the path for which the request is asking for.

# Create your views here.
def blogHome(request):
    # print("user is:",request.user)
    posts = Post.objects.all()
    context = {'posts':posts}
    post_titles = ['Modi - The Unrated Leader','How The West So Rich','The South China Sea']
    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    post = Post.objects.filter(sno = slug).first()
    post.views += 1
    post.save()
    # below will all those blogcomment which are being done on the current blogPost.
    comments = blogComment.objects.filter(post=post,parent=None)
    replies = blogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    # print(replyDict)
    # print(comments)
    context = {'post':post,'comments':comments,'user':request.user,'replyDict':replyDict,}
    return render(request,'blog/blogPost.html',context)

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')

        if parentSno == "":
            comment = blogComment(comment=comment,user = user,post = post)
            comment.save()
            messages.success(request,'Your Comment have been posted successfully')
        else:
            parent = blogComment.objects.get(sno=parentSno)
            comment = blogComment(comment=comment,user = user,post = post,parent=parent)
            comment.save()
            messages.success(request,'Your reply have been posted successfully')
    # all the following are correct
    return redirect(f'/blog/{postSno}')
    # return redirect(f'/blog/{post.sno}')
    # return redirect(f'/blog/{postSno}')
