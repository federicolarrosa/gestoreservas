from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q

def home(request):
    return render(request, 'home/index.html') 



def info(request):
    return render(request,'home/informacion.html') 

def final(request):
    return render(request,'listado/final.html') 


# def Login(request):
#     form = AuthenticationForm()
#     if request.method == 'POST':
#         AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             return redirect('listado/')
#     else:
#         form = AuthenticationForm()
#         return render(request,'usuario/registro.html', {'form':form})


"""
def busqueda(restaurante,nombre,ubicacion,q,q2):
    resultado= restaurante.objects.filter(nombre__icontains=q | ubicacion__icontains =q2)
    return resultado
"""
