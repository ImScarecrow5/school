from django.urls import path

from .views import *

urlpatterns = [
    path('school/', sch),
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('sign-in/', sign_in, name='sign-in'),
    path('sign-up/', sign_up, name='sign-up'),
    path('news/', news, name='news'),
    path('news/<int:post_id>/', show_post, name='post'),
]

