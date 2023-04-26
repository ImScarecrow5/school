from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import get_template

from .forms import SchoolForm
from lyceum_website.settings import EMAIL_SERVER, EMAIL_ADMIN
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives

from .models import *

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

def feedback(request):
    context = {}
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid(): 
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            context = {'success': 1}
    else:
        form = SchoolForm()
    context['form'] = form
    return render(request, 'school/email.html', context=context)

def send_message(name, email, message):
    text = get_template('school/message_feedback.html')
    text_html = get_template('school/message_feedback.html')
    context = {'name': name, 'email': email, 'message': message}
    subject = 'Письмо от пользователя'
    text_content = text.render(context)
    send_mail(subject, text_content, EMAIL_SERVER, EMAIL_ADMIN)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')