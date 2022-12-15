from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Tkp(models.Model):
    """ТКП"""
    nomer = models.PositiveSmallIntegerField("Номер ТКП", default=2023)
    data_tkp = models.DateField("Дата ТКП", default=date.today)
    contragent = models.CharField("Организация (Клиент)", max_length=150)
    offers_cost = models.PositiveSmallIntegerField("Сумма ТКП", default=0, help_text="указывать сумму в рублях с НДС")
    contact_person = models.CharField("Контактное лицо", max_length=100)
    locality = models.CharField("Населенный пункт", max_length=150)
    main_offer = models.TextField("Оборудование содержание, предложение")
    tender = models.BooleanField("Тендер да/нет", default=False)
    note = models.CharField("Примечание", max_length=150)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tkp")
    members = models.ManyToManyField(User, related_name="members", blank=True)
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.locality

    class Meta:
        verbose_name = "ТКП"
        verbose_name_plural = "Реестр ТКП"