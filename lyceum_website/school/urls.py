from django.urls import path

from .views import *

urlpatterns = [
    path('school/', sch),
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('test/', test, name='test'),
    path('sign-in/', sign_in, name='sign-in'),
    path('sign-up/', sign_up, name='sign-up'),
]

