from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('tel_list/', tel_list, name='tel_list'),
    path('login/', login, name='login'),
]