# Generated by Django 2.1.7 on 2019-04-22 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listado', '0029_reserva_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='reservamenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='listado.menu')),
            ],
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='menu',
        ),
        migrations.AddField(
            model_name='reservamenu',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='listado.Reserva'),
        ),
    ]
