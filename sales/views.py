from django.shortcuts import render
from django.views.generic.base import View

from .models import Tkp


class TkpView(View):
    """Список ТКП"""

    def get(self, request):
        tkps = Tkp.objects.all()
        return render(request, "sales/tkp_list.html", {"tkp_list": tkps})
