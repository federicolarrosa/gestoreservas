# Generated by Django 2.1.7 on 2019-03-13 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listado', '0003_auto_20190313_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='personas',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='telefono',
            field=models.IntegerField(default=1),
        ),
    ]
