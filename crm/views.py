from django.shortcuts import render
from django.http import HttpResponse


def first_page(request):
    a = '<h1>Hello World</h1>'
    return render(request)
# Create your views here.
