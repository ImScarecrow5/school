from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('feedback/', feedback, name='feedback'),
    path('news/', news, name='news'),
    path('news/<int:post_id>/', show_post, name='post'),
]

