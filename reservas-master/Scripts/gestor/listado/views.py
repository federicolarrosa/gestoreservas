from django.shortcuts import render_to_response, render, reverse
from urllib import request
from .models import restaurante, Reserva, menu, reservamenu
from .forms import NuevaReserva, ReservaMenu
from django import forms
from django.views.generic import ListView, DetailView, CreateView, FormView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

class RestauranteListView(ListView):
    model = restaurante
    template_name = 'listado/listing.html'
    context_object_name = 'restaurantes'
    
    
    
    
def search(request):
    query = request.GET.get('q', '')
        
    if query:
        qset = (
                Q(ubicacion__icontains=query) |
                Q(nombre__icontains=query)
                    )
        results = restaurante.objects.all().distinct().order_by(qset)
    else:
        results = []
    return render_to_response("listado/listing.html", {
        "results": results,
        "query": query
})


class RestauranteDetailView(DetailView,CreateView ):
    model = Reserva
    form_class = NuevaReserva
    template_name = 'listado/detail.html'
    context_object_name = 'restaurantes'
    success_url = '/listado/gracias'
    
    def form_valid(self, form):
        form.instance.User = self.request.user
        form.save()
        return super().form_valid(form)

    def get_queryset(self):
        return restaurante.objects.all()
    
   
    
   

class reservasView(ListView):
    model= Reserva
    template_name = 'listado/final.html'
    context_object_name = 'reservas'
 
    def get_queryset(self):
        return Reserva.objects.filter(User=self.request.user).order_by('-id')[:1]

class reservasView1(ListView):
    model = Reserva
    template_name = 'listado/final1.html',
    context_object_name = 'reservas'

    def get_queryset(self):
        return Reserva.objects.filter(User=self.request.user).order_by('-id')[:1]



class MenuView(FormView, CreateView):
    model = menu
    form_class= ReservaMenu
    template_name = 'listado/menu.html'
    context_object_name = 'menu'
    success_url = '/listado/final1'


class ReservaMenuListView(ListView):
    # queryset = Reserva.objects.all()
    template_name = 'listado/personasmenu.html'
    context_object_name = 'reservas'
    paginate_by = 5
    ordering = ['-id']

    def get_queryset(self):
        return Reserva.objects.filter(User=self.request.user).order_by('-id')[:1]




def gracias(request):
    return render(request,'listado/gracias.html') 


def final(request):
    return render(request,'listado/final.html') 

def final1(request):
    return render(request,'listado/final1.html') 

def pago(request):
    return render(request,'listado/pago.html') 
