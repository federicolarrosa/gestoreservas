from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms


class menu(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
   #foto = models.ImageField()
    ingredientes = models.TextField(max_length=200)
   #tipo = models.ManyToManyField(restaurante, choices=restaurante.TIPOCOMIDA)
    
    
    def __str__(self):
        return self.nombre


class restaurante(models.Model):
        
    OPCIONES = (
         ('Si', 'Si'),
         ('No', 'No'),
     )
    TIPOCOMIDA = (
        ('Vegana', 'Vegana'),
        ('Pastas', 'Pastas'),
        ('Parrilla', 'Parrilla'),
    )
    
    image = models.ImageField(default='default.jpg', upload_to='restaurant_pics')
    nombre = models.CharField(max_length=100)
    rating = models.IntegerField(null=True)
    ubicacion = models.CharField(max_length=200)
    horarios = models.CharField(max_length=100)
    telefono_restaurante = models.CharField(max_length=100)
    email_restaurante = models.EmailField(max_length=100)
    fumar = models.CharField(max_length=20, choices=OPCIONES)
    wifi = models.CharField(max_length=20, choices=OPCIONES)
    estacionamiento = models.CharField(max_length=20, choices=OPCIONES)
    tarjetas = models.CharField(max_length=20, choices=OPCIONES)
    tipoComida = models.CharField(max_length=100, choices=TIPOCOMIDA)
    comentarios = models.TextField(max_length=500)
    mesas_total= models.IntegerField(null=True)
    Menu = models.ManyToManyField(menu)
   


    def __str__(self):
        return self.nombre


    def get_absolute_url(self):
        return reverse('detalles', kwargs={'pk': self.pk})
   

class Reserva(models.Model):
    PERSONAS = (
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'),
        ('13', '13'), ('14', '14'), ('15', '15'),('16', '16'), ('17', '17'),('18', '18'),('19', '19'),('20', '20'),

    )
    User= models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    restaurante = models.ForeignKey(restaurante, on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField(default=0)
    email = models.EmailField(max_length=100)
    personas = models.CharField(max_length=20, choices=PERSONAS)
    dia = models.DateField(null=True)
    hora = models.TimeField(null=True)
    mesa= models.IntegerField(null=True)
    
    def get_absolute_url(self):
        return reverse('detalles','final', 'reserva-delete','menu1', kwargs={'pk': self.pk})

   
    
    def __str__(self):
            return self.User

class reservamenu(models.Model):
    CANTIDAD = (
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'),
        ('13', '13'), ('14', '14'), ('15', '15'),('16', '16'), ('17', '17'),('18', '18'),('19', '19'),('20', '20'),)
        
    repeticion = models.CharField(max_length=30, null=True, choices=CANTIDAD)
   # User = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    menu = models.ForeignKey(menu, on_delete=models.CASCADE, blank=True, null=True)
    campo = models.BooleanField(default=False)
    precio = models.IntegerField()
    def get_absolute_url(self):
        return reverse('menu','menu1', kwargs={'pk': self.pk})
      
   
 
