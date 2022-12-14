# Generated by Django 4.1.3 on 2022-11-30 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts_all',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterField(
            model_name='contacts_all',
            name='department_cont',
            field=models.CharField(max_length=100, verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='contacts_all',
            name='department_position',
            field=models.CharField(max_length=100, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='contacts_all',
            name='department_tel',
            field=models.CharField(max_length=3, verbose_name='Внутренний телефон'),
        ),
        migrations.AlterField(
            model_name='contacts_all',
            name='position_email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='contacts_all',
            name='position_first_name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='contacts_all',
            name='position_last_name',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='contacts_all',
            name='position_mob_tel',
            field=models.CharField(max_length=35, verbose_name='Мобильный телефон'),
        ),
        migrations.AlterField(
            model_name='contacts_all',
            name='position_patronymic',
            field=models.CharField(max_length=100, verbose_name='Отчество'),
        ),
    ]
