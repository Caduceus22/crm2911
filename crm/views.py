from django.http import HttpResponse
from django.shortcuts import render, redirect
from contacts.models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Внутренние номера телефонов", 'url_name': 'tel_list'},
        {'title': "Войти", 'url_name': 'login'},
        ]


def index(request):
    departures = Departures.objects.all()
    context = {
        'depts': departures,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'crm/index.html', context=context)


def about(request):
    return HttpResponse("О сайте")


def tel_list(request):
    return HttpResponse("Список внутренних номеров телефонов")


def login(request):
    return HttpResponse("Авторизация")
