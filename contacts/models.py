from django.db import models


class Contacts_all(models.Model):
    department_cont = models.CharField(max_length=100, verbose_name='Отдел')
    department_tel = models.CharField(max_length=3, verbose_name='Внутренний телефон')
    department_position = models.CharField(max_length=100, verbose_name='Должность')
    position_first_name = models.CharField(max_length=100, verbose_name='Имя')
    position_last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    position_patronymic = models.CharField(max_length=100, verbose_name='Отчество')
    position_mob_tel = models.CharField(max_length=35, verbose_name='Мобильный телефон')
    position_email = models.EmailField(max_length=254, verbose_name='E-mail')

    def __str__(self):
        return self.department_position

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

