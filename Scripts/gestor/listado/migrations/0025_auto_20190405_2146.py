# Generated by Django 2.1.7 on 2019-04-06 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listado', '0024_auto_20190404_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurante',
            name='Menu',
        ),
        migrations.AddField(
            model_name='restaurante',
            name='Menu',
            field=models.ManyToManyField(to='listado.menu'),
        ),
    ]
