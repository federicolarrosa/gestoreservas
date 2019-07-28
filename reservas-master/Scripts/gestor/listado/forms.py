from django import forms
from .models import Reserva, restaurante, menu, reservamenu
from django.views.generic import ListView, DetailView, CreateView, FormView, DeleteView

class NuevaReserva(forms.ModelForm):
   
    def get_initial(self):
        return {"restaurante": self.kwargs.get("pk")} 
 

    
    
    class Meta:
        model = Reserva
        fields = ['User', 'restaurante', 'email', 'telefono',
                  'personas', 'dia', 'hora', 'mesa', 'nombre', 'apellido']
        widgets = {'User': forms.HiddenInput(attrs={'class': 'from-control'}),
                   'restaurante': forms.HiddenInput(attrs={'class': 'from-control'}),
                   'nombre': forms.HiddenInput(attrs={'class': 'from-control'}),
                   'apellido': forms.HiddenInput(attrs={'class': 'from-control'}),
                   'personas': forms.Select(attrs={'class': 'from-control'}),
                   'dia': forms.DateInput(attrs={'class': 'from-control','id':'datepicker','type':'date'}),
                   'hora': forms.TimeInput(attrs={'class': 'from-control', 'id': 'timepicker', 'type': 'time'}),
                   }

class ModificarReserva(forms.ModelForm):

    class Meta:
        model=Reserva
        fields=['personas', 'dia', 'hora']
        widgets = {
                   'personas': forms.Select(attrs={'class': 'from-control'}),
                   'dia': forms.DateInput(attrs={'class': 'from-control', 'id': 'datepicker', 'type': 'date'}),
                   'hora': forms.TimeInput(attrs={'class': 'from-control', 'id': 'timepicker', 'type': 'time'}),
                   }
class ReservaMenu(forms.ModelForm):
   # campo = forms.ModelChoiceField(queryset=menu.objects.all())

    
    class Meta:
        model = reservamenu
        fields = ['campo','menu','precio','repeticion']
        widgets={'menu':forms.TextInput(attrs={'class': 'from-control'}),
                 'precio':forms.NumberInput(attrs={'class': 'from-control'}),
                 'repeticion':forms.Select(attrs={'class': 'from-control'}),
                 'campo': forms.CheckboxInput(attrs={'class': 'from-control'}),
        }
                                    