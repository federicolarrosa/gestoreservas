# Generated by Django 2.1.7 on 2019-05-02 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listado', '0036_auto_20190501_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='personas',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=20),
        ),
    ]