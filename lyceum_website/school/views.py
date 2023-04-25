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

def news(request):
    posts = School.objects.all()
    return render(request, 'school/news.html', {'posts': posts})

def show_post(request, post_id):
    posts = School.objects.get(pk = post_id)
    return render(request, 'school/post.html', {'posts': posts})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')