from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post

# Create your views here.
def home(request): 
    blog_len = len(Post.objects.all())
    cng_len = blog_len - 4
    xi = []
    for i in range(cng_len,blog_len):
        xi.append(Post.objects.filter(sno=i+1).first())
    params = {
        'posts':xi
    }
    return render(request,'home/home.html',params)

def contact(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        usertext = request.POST['textarea']
        if len(name)>2 and  len(email)>6 and len(password)>6 and len(usertext)>2:
            contact = Contact(name = name ,email = email ,password = password ,content = usertext)
            contact.save()
            messages.success(request,f'Namaste {name}, your message has been successfully sent')
        else:
            messages.error(request,'Please fill out the form properly')
    return render(request,'home/contact.html')
    
def about(request):
    return render(request,'home/about.html')
