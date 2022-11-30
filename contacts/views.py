from django.http import HttpResponse
from django.shortcuts import render
from .models import Contacts_all


def contacts_page(request):
    return render(request, 'contacts/contacts.html')


def departures(request):
    departures_list = Contacts_all.objects.all().order_by('department_tel')
    return render(request, 'contacts/depts.html', {'departures_list': departures_list})
