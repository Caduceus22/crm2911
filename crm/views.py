from django.shortcuts import render, redirect
from contacts.models import *


menu = ["Главная", "Отделы", "Контакты", "Вход"]
def index(request):
    return render(request, 'crm/index.html', {'menu': menu, 'title': 'Главная страница'})

