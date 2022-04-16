from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse,redirect
from .models import Graphic,ManyImage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    all_categories = set()
    home_card_category = []
    competitive_exam_cards = []
    edtech_awards = []
    syllabus_category = []
    many = Graphic.objects.all()
    for i in many:
        all_categories.add(i.category)
    for j in list(all_categories):
        if j == 'home-card-category':
            home_card_category = Graphic.objects.filter(category = j)
        if j == 'competitive-exam-card':
            competitive_exam_cards = Graphic.objects.filter(category= j)
        if j == 'edtech-award':
            edtech_awards = Graphic.objects.filter(category = j)
        if j == 'syllabus-card':
            syllabus_category = Graphic.objects.filter(category = j)

    boards_images = ManyImage.objects.filter(category = 'boards-image')
    exams_images = ManyImage.objects.filter(category = 'exams-image')
    subjects_images = ManyImage.objects.filter(category = 'subjects-image')

    params = {'home_card_category':home_card_category,'competitive_exam_cards':competitive_exam_cards,'edtech_awards':edtech_awards,'syllabus_cards':syllabus_category,'boards_images':boards_images,'exams_images':exams_images,'subjects_images':subjects_images}

    return render(request,'Home/index.html',params)

# for creating a new user
def Sign_in(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['user_email']
        password = request.POST['userpass']
        users = User.objects.all()
        yes_new_user = 0
                

        if ' ' not in username:
            if len(username) >= 3:
                if len(password) >= 5:
                    for user in users:
                        if user.username == username:
                            print('not possible beta!')
                            return render(request,'Home/index.html',{'applicable':'false'})
                        else:
                            # print('no of truth are as follow:',yes_new_user)
                            if user.email != email:
                                yes_new_user += 1
                                print('yes_new_user',yes_new_user)
        
        else:
            return render(request,'Home/index.html',{'username':username,'right_username':'false'})

        
        if len(users) == yes_new_user:
            # create_user = User.objects.create_user(username,email,password)
            print('hello do something!')
            # create_user.save()
            return render(request,'Home/index.html',{'applicable':'true'})
        else:
            print('i am gone this time men')
            return render(request,'Home/index.html',{'applicable':'false'})
        #     
        # for i in ['science','commerce','arts']:
        #     if stream == i:
        #         stream = stream
        # if stream == '':
        #     stream = 'none'
    else:
        return HttpResponse('404 - Not Found')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['userpass']

        user = authenticate(username=username,password = password)

        if user is not None:
            login(request,user)
            return redirect('/')
            # return render(request,'Home/index.html',{'login_user':'true'})
        else:
            return redirect('/')
            # return render(request,'Home/index.html',{'login_user':'false'})
    else:
        return HttpResponse('login')   

def user_logout(request):
    logout(request)
    return redirect('/')