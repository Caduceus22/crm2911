from django.urls import path

from .views import *

urlpatterns = [
    path('depts/', departures),
    path('', contacts_page),
]