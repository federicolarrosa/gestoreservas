# from django.db import models
# from django.contrib.auth.models import User

# class Reserva(models.Model):
#     usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     nombre = models.CharField(max_length=100)
#     apellido = models.CharField(max_length=100)
#     telefono = models.IntegerField()
#     email = models.EmailField(max_length=100)
#     personas = models.IntegerField()
#     dia = models.CharField(max_length=100)
#     hora = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nombre
