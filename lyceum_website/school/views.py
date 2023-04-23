from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

def sch(request):
    return HttpResponse('Страница приложения school')

def index(request):
    return render(request, 'school/index.html')

def contacts(request):
    return render(request, 'school/contacts.html')

def sign_in(request):
    return render(request, 'school/sign-in.html')

def sign_up(request):
    return render(request, 'school/sign-up.html')

def test(request):
    posts = School.objects.all()
    return render(request, 'school/test.html', {'posts': posts})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')