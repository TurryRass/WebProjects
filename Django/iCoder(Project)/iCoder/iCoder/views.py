from django.shortcuts import HttpResponse, redirect,render
from blog.models import Post
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from simple_search import search_filter
from django.contrib import messages
import time


def search(request):
    if request.method == "GET":
        timeStart = time.time()
        search_titles = ['title','author','content','timestamp']
        try:
            query = request.GET['query']
            if query == '':
                return redirect('/')
        except:
            return redirect('/')
        if len(query) > 100:
            messages.warning(request,"Your query is too long!Enter a small query")
            posts = []
        else:
            posts = Post.objects.filter(search_filter(search_titles,query))
        now_time = str(time.time() - timeStart)
        # the following is our params dictionary where:
        # results_found - is the total number of posts found
        params = {'all_posts':posts,'query':query,'results_found':len(posts),'find_time':now_time}
        # params = {'all_posts':posts,'results_found':len(posts)}
    return render(request,'search.html',params)

# Below are the authentication APIs which are only useful for redirecting and authentication and not for going to other endpoints.
def handleSignUp(request):
    if request.method == "POST":
        # To get the post parameters
        # in below request.post is actually a dictionary corresponding to which the values like username has been taken
        username = request.POST['userName']
        email = request.POST['email']
        password = request.POST['password1'] # main entered password
        c_password = request.POST['password2'] # for confirm password

        # check for errorneous input
        test_len_name = username.split(' ')
        # 1. Username should be under 10 characters
        if len(username) > 30:
            messages.error(request,"Sign Up Failed. Your user name must be under less than 20 characters!")
            return redirect('/')
        # 2.Username check for full name
        if len(test_len_name) != 2:
            messages.error(request,"Sign Up Failed. Enter your full name (First name and Last name)!")
            return redirect('/')
        # 3. Username should be more than 3 characters.
        if len(test_len_name[0]) < 3 or len(test_len_name[1]) < 3:
            messages.error(request,"Sign Up Failed. Please Enter a valid user name!")
            return redirect('/')
        # 4.Username must be alphaNumeric
        for i in ['!','@','#','$','%','^','&','*','(',')','+','-','=','_','  ']:
            if i in username:
                messages.error(request,"Sign Up Failed. UserName should only contain letters and numbers!")
                return redirect('/')
        # 5.passwords in both the boxes must match.
        if password != c_password:
            messages.error(request,"Sign Up Failed. Passwords do not match!")
            return redirect('/')
        #Create The User
        user = User.objects.create_user(username,email,password)
        user.first_name = test_len_name[0]
        user.last_name = test_len_name[1]
        user.save()
        messages.success(request,"Your iCoder account has been successfully created!")
        return redirect('/')

    else:
        return redirect('/')

def handleLogin(request):
    if request.method == "POST":
        userName = request.POST['loginUsername']
        print(userName)
        password = request.POST['loginPassword']
        print(password)
        user = authenticate(username = userName,password = password)
        print(user)

        if user is not None:
            login(request,user)
            messages.success(request,f"Welcome {user.get_username()},You have been suucessfully logged In!")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials,please try again!")
            return redirect('/')
    else:
        return redirect('/')

def handleLogout(request):
    logout(request)
    messages.success(request,f"You have been successfully logged out!")
    return redirect('/')