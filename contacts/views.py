from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def contacts_page(request):
    return HttpResponse("Контакты")