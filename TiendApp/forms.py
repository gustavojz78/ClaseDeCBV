from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Productos(forms.Form):
    ids=forms.IntegerField()
    productos=forms.CharField(max_length=30)
    precios=forms.IntegerField()

class AgregarTiendas(forms.Form):
    sucursales=forms.IntegerField()
    ubicaciones=forms.CharField(max_length=30)

class AgregarAgenda(forms.Form):
    telefonos=forms.IntegerField()
    emails=forms.EmailField()

class AgregarEmpleado(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    puesto=forms.CharField(max_length=30)
    dni=forms.IntegerField()
    email=forms.EmailField()
    telefono=forms.IntegerField()

class UsuarioRegistroForm(UserCreationForm):
    usuario=forms.CharField(max_length=30)
    email=forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['usuario', 'email', 'password1', 'password2']
        help_text = { k: "" for k in fields} 






  

