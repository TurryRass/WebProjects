from django.shortcuts import HttpResponse,render

def signIn(request):
    return render(request,'Home/signIn.html')

def login(request):
    return render(request,'Home/login.html')