# Generated by Django 2.1.7 on 2019-03-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listado', '0002_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
    ]
