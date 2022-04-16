from json.tool import main
from re import sub
from sqlite3 import paramstyle
from django.shortcuts import render,HttpResponse,redirect
from simple_search import search_filter
from .models import Question, subject,TrendingChapter,For_Class_Subjects,Chapter
from Answer.templatetags import replace

# Create your views here.
def ask(request):
    all_objects = TrendingChapter.objects.all()
    main_list = [[],[]]
    for i in all_objects:
        if i.class_no <= 8:
            main_list[0].append(i)
        if i.class_no > 8:
            main_list[1].append(i)
    # print(main_list,'this is our list')
    subjects = subject.objects.all()
    params = {'subjects':subjects,'main_list':main_list,'show_classer':'true'}
    return render(request,'Answer/index.html',params)
    
def do(request,id):
    all_classes = For_Class_Subjects.objects.get(class_no = id)
    all_objects = TrendingChapter.objects.all()
    list_class_subjects = all_classes.subjects.split(',')
    # print('this is                our list and this',list_class_subjects)
    subjects = []
    for i in list_class_subjects:
        try:
            subjects.append(subject.objects.get(name = i))
        except:
            print('')
    main_list = [[],[]]
    for i in all_objects:
        if i.class_no <= 8:
            main_list[0].append(i)
        if i.class_no > 8:
            main_list[1].append(i)
    params = {'subjects':subjects,'show_classer':'false',"main_list":main_list,"student_class":id}
    return render(request,'Answer/index.html',params)
    # return HttpResponse(f'hello <h1> the id is {id} </h1>')

def chapters_list(request,id,subject_name):
    all_objects = TrendingChapter.objects.all()
    main_list = [[],[]]
    for i in all_objects:
        if i.class_no <= 8:
            main_list[0].append(i)
        if i.class_no > 8:
            main_list[1].append(i)

    chapters = Chapter.objects.filter(chapters_class = id,subject = subject_name.replace('_',' ')).first()
    
    if chapters == None:
        params = {'chapters_class':id,'no_chapters':'No','subject':subject_name.replace('_',' '),'main_list':main_list,'is_chapters':'false'}
    else:
        chapters_list = []
        for i in chapters.names.split(','):
            chapters_list.append(i)

        params = {'chapters_class':id,'subject':subject_name.replace('_',' '),'chapters_list':chapters_list,'no_chapters':len(chapters_list),'main_list':main_list,'is_chapters':'true'}

    return render(request,'Answer/chapter_list.html',params)

def questions_chapter(request,id,subject_name,chapter):
    all_objects = TrendingChapter.objects.all()
    main_list = [[],[]]
    for i in all_objects:
        if i.class_no <= 8:
            main_list[0].append(i)
        if i.class_no > 8:
            main_list[1].append(i)

    # for the questions display part
    questions = Question.objects.filter(question_class = id,chapter_name = chapter.replace('_',' '),subject = subject_name)
    print(questions)
    question_list = []
    for question in questions:
        question_list.append(question)
    if len(question_list) > 0:
        params = {'question_list':question_list,'questions_uploaded':'true','main_list':main_list,'chapters_class':id,'subject':subject_name,'no_questions':len(questions),'chapter':chapter.replace('_',' ')}
    else:
        params = {'question_list':question_list,'questions_uploaded':'false','main_list':main_list,'chapters_class':id,'subject':subject_name,'no_questions':len(questions),'chapter':chapter.replace('_',' ')}

    # print('yes the list is as follows',question_list)
    return render(request,'Answer/question_page.html',params)
    # return HttpResponse('hello how are you world!')




