from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NuevoUsuario

def Registro(request):
    if request.method == 'POST':
        f = NuevoUsuario(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('/')
 
    else:
        f = NuevoUsuario()
 
    return render(request, 'usuarios/registro.html', {'form': f})


