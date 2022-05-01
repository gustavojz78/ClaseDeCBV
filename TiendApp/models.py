
from django.db import models
from django.contrib.auth.models import User
#recordar que para ingresar datos, debo ingresar todos los atributos
class Tiendas(models.Model):
    sucursal= models.IntegerField(primary_key=True)
    ubicacion=models.CharField(max_length=30)
    def __str__(self):
        return f"{(self.sucursal)} | {(self.ubicacion)}"

class Contacto(models.Model):
    telefono=models.IntegerField(primary_key=True)
    email=models.EmailField()
    def __str__(self):
        return f"{(self.telefono)} | {(self.email)}"
   

class Staff(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    puesto=models.CharField(max_length=30)
    dni=models.IntegerField(primary_key=True)
    email=models.EmailField()
    telefono=models.IntegerField()
    def __str__(self):
        return f"{(self.nombre)}-{(self.apellido)} | {(self.dni)}"

class Ventas(models.Model):
    id=models.IntegerField(primary_key=True)
    productos=models.CharField(max_length=30)
    precio=models.IntegerField()
    def __str__(self):
        return f"{(self.productos)} | {(self.id)}"

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta avatares de media
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    