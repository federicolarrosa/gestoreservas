from django.contrib import admin
from .models import restaurante, Reserva, menu, reservamenu
# Register your models here.
admin.site.register(Reserva)
admin.site.register(restaurante)
admin.site.register(menu)
admin.site.register(reservamenu)
