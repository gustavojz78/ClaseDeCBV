from django import forms

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






  

