# Generated by Django 4.1.3 on 2022-12-02 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_remove_contacts_all_department_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts_all',
            name='department_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contacts.departures', verbose_name='Название отдела'),
        ),
    ]