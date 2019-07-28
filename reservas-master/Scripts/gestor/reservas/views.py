from django.shortcuts import render, render_to_response, redirect
from django.views.generic import ListView, UpdateView, DetailView, DeleteView
from listado.models import Reserva, restaurante
from listado.forms import ModificarReserva
from django.urls import reverse_lazy

class ReservaListView(ListView):
    # queryset = Reserva.objects.all()
    template_name = 'reservas/opciones.html'
    context_object_name = 'reservas'
    paginate_by = 5
    ordering = ['-id']

    def get_queryset(self):
        return Reserva.objects.filter(User=self.request.user).order_by('-id')

     
    
class ReservaDetailView(DetailView, UpdateView):
    model = Reserva
    form_class=ModificarReserva
    template_name = 'reservas/detalles.html'
    context_object_name = 'reservas'
    success_url= '/reservas/'
    

   
class ReservaDeleteView(DeleteView):

    model = Reserva
    success_url = reverse_lazy(ReservaListView)


