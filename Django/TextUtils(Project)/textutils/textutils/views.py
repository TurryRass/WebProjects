from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def display(request):
    punc_remove = request.POST.get('puncremover','off')
    newline = request.POST.get('newline','off')
    extraspace = request.POST.get('ES_remover','off')
    upper = request.POST.get('uppercase','off')
    lower = request.POST.get('lowercase','off')
    words = request.POST.get('count_words','off')
    letters = request.POST.get('count_letters','off')
    capitalize = request.POST.get('capitalizeAll','off')

    if punc_remove == 'on':
       user_text,extra = puncremover_func(request)
    if newline == 'on':
       user_text,extra = newlineremover_func(request)
    if extraspace == 'on':
       user_text,extra = extraspaceremover_func(request)
    if upper == 'on':
       user_text,extra = upper_func(request)
    if lower == 'on':
       user_text,extra = lower_func(request)
    if words == 'on':
        user_text,extra = countwords_func(request)
    if letters == 'on':
        user_text,extra = countletters_func(request)
    if capitalize == 'on':
       user_text,extra = capitalize_func(request)

    use_dict = {'title':'Analyzed Text','text':user_text,'analysed_text':"Your Analysed Text Is ready!",'extra':extra}
    return render(request,'rest_all.html',use_dict)

def account(request):
    return HttpResponse('<h1>This is Your Page</h1>')

def puncremover_func(request):   
    will_text = request.POST.get('text','default')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    user_text = ''

    for char in will_text:
            if char not in punctuations:
                user_text += char
            else:
                user_text += ''

    return user_text,''

def upper_func(request):
    will_text = request.POST.get('text','default')
    user_text = ''

    for words in will_text:
        user_text += words.upper()

    return user_text,''

def lower_func(request):
    will_text = request.POST.get('text','default')
    user_text = ''

    for words in will_text:
        user_text += words.upper()

    return user_text,''

def newlineremover_func(request):
    will_text = request.POST.get('text','default')
    temp_text = ''
    for char in will_text:
            if char != '\n' and char != '\r':
                temp_text += char
            else:
                temp_text += ''
    
    words_list = will_text.split('\r\n')
    user_text = ''
    print(words_list)
    give = 0

    for index,word in enumerate(words_list):
        if word == '':
            try:
                while not(words_list[index+1+give] == ''):
                    user_text += ''
                    give += 1
            except:
                user_text += ''
        else:
            user_text += word + ' '
        

    return user_text,''

def extraspaceremover_func(request):
    will_text = request.POST.get('text','default')
    user_text = ''
    will_list = list(will_text)

    for index,words in enumerate(will_list):
        if not(will_list[index] == ' ' and will_list[index+1] == ' '):
            user_text += words
            
    return user_text,''

def countwords_func(request):
    user_text = request.POST.get('text','default')
    user_words = user_text.split(' ')
    extra = f"There are in total {len(user_words)} words in your given text."
    
    return user_text,extra

def countletters_func(request):
    user_text = request.POST.get('text','default')
    extra = f'''There are in total {(len(list(user_text)))+1} letters in your given text.'''
    
    return user_text,extra

def capitalize_func(request):
    will_text = request.POST.get('text','default')
    will_list = will_text.split(' ')
    user_text = ''

    for words in will_list:
        user_text += words.capitalize() + ' '
        
    return user_text,''

def help(request):
    return HttpResponse('Hello I am about')

def privacypolicy(request):
    return HttpResponse('Hello I am about')

def about(request):
    return HttpResponse('About Us')

