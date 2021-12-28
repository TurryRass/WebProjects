from django.shortcuts import render,HttpResponse,redirect
from Blog.models import Post
from Home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.
def Home(request):
    All_Posts = Post.objects.all()
    total_authors = len(All_Posts)
    for i in range(total_authors):
        try:
            file = open(f'static/authors/{All_Posts[i].author}.txt','w+')
            file.write(All_Posts[i].author_story)
        except Exception as e:
            print()
    Top_Posts = []

    # To get the recent Posts Uploaded
    for i in range(len(All_Posts)):
        if len(Top_Posts) != 5:
            Top_Posts.append(All_Posts[len(All_Posts) - i - 1])
        else:
            Top_Posts.reverse()
    params = {'posts':Top_Posts}
    return render(request,'Home/index.html',params)

def Contact_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        text = request.POST.get('text')
        decide1 = False
        decide2 = False
        decide3 = False

        if len(name) <= 150:
            decide1 = True
        if len(email) <= 500:
            decide2 = True
        if len(password) <= 200:
            decide3 = True

        if decide1 and decide2 and decide3:
            contact = Contact(name=name,email=email,password=password,text=text)
            contact.save()
            messages.success(request,f'{name},your form has been submitted succesfully.We will reply to you soon!')

            return redirect('/')

        else:
            # messages.error(request,'Remember that\nName:Should be less than 151 Characters\n Email:Should be less than 501 characters\nPassword:Should be below 201 characters')
            messages.error(request,'You did not followed the instructions to fill the form,Please follow it and then submit.')

            return redirect('/contact')

    else:
        messages.warning(request,'Remember that\
        Name:Should be less than 151 Characters \
        Email:Should be less than 501 characters \
        Password:Should be below 201 characters')
        
    return render(request,'Home/contact.html')

def About(request):
    document = open('static/file/about.txt').read()
    files = document.split('</p>')
    params = {'files':files,'about':True,'title':'Our Story'}
    return render(request,'Home/about.html',params)

def about_author(request,author):
    author_document = open(f'static/authors/{author}.txt').read()
    files = author_document.split('</p>')
    params = {'files':files,'about':False,'title':f'Author - {author}'}
    return render(request,'Home/about.html',params)

def Terms(request):
    return render(request,'Home/terms.html')

def Policy(request):
    return render(request,'Home/policy.html')

def account(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['useremail']
        user_pass = request.POST['userpassword']

        vote1 = False
        vote2 = False
        vote3 = False

        if first_name.isalpha():
            vote1 = True
        if last_name.isalpha():
            vote2 = True
        if user_pass.isalnum():
            vote3 = True
    
        if vote1 and vote2 and vote3:
            New_user = User.objects.create_user(username,email,user_pass)
            New_user.first_name = first_name
            New_user.last_name = last_name
            New_user.save()
            messages.success(request,f'Hello {username},you have successfully signed in.Thank You!')
            return redirect('/')
        else:
            messages.error(request,'Please follow the instructions about form submission given before and sign in again!')
            return redirect('/account')
    else:
        messages.warning(request,'If you are a new user make sure that in the sign in form: 1.username,firstname,lastname should be more than 3 and less than 101 characters and firstname,lastname should be alphanumeric only 2.email should be less than 200 characters 3.password should be more than 7 and less than 12 characters and should be alphanumeric only.')

    return render(request,'Home/account.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['userpassword']
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            messages.success(request,f'Hello {username}, you have logged in successfully !')
            return redirect('/')
        else:
            messages.error(request,"Please input correct username and password,if you do not have one than please sign in here!")
            return redirect('/account/')
    else:
        return redirect('/')

def user_logout(request):
    logout(request)
    messages.success(request,'You have been successfully logged out!')
    return redirect('/')

