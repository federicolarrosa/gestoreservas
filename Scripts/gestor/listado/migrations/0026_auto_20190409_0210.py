# Generated by Django 2.1.7 on 2019-04-09 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listado', '0025_auto_20190405_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='dia',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora',
            field=models.TimeField(auto_now=True),
        ),
    ]
