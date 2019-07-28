from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class NuevoUsuario(forms.Form):
    username = forms.CharField(label='Nombre de usuario', min_length=4, max_length=150)
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Primer nombre', max_length=150)
    last_name = forms.CharField(label='Primer apellido', max_length=150)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar la contraseña', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Este Usuario ya existe")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Este Email ya existe")
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].lower()
        r = User.objects.filter(first_name=first_name)
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].lower()
        r = User.objects.filter(last_name=last_name)
        return last_name

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden")
 
        return password2
 
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            
        )
        return user
