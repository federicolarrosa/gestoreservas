# Generated by Django 2.1.7 on 2019-05-03 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listado', '0037_auto_20190501_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='dia',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='hora',
        ),
        migrations.AddField(
            model_name='reserva',
            name='dia_hora',
            field=models.DateTimeField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='telefono',
            field=models.IntegerField(default=0),
        ),
    ]
