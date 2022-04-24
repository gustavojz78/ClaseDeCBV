from django.urls import path
from TiendApp.views import *

 
urlpatterns = [
    path("", inicio, name="Inicio"),
    path("tiendas/", tiendas, name = "Tiendas"),
    path("contactos/", agenda, name = "Contacto"),
    path("staff/", staff, name ="Staff"),
    path("ventas/", ventas, name= "Ventas"),
    path("formulario/", entrar, name="Entrar"),
    path("buscarProducto/", buscarProducto, name="Buscar"),
    path("buscar/", buscar),
    path("borrarEmpleado/<empleados_dni>/", eliminarStaff, name="eliminarEmpleado"),
    path("editarEmpleado/<empleados_dni>/", actualizar, name="editarEmpleado"),
#Estos name, son los que hacen que la url se relacione con el template
#por ejemplo en tienda_lista.html encontramos los url Ver, Editar, Borrar
    path("tienda/lista", TiendaLista.as_view(), name="tienda_lista"),
#El orden de la ruta importa. Nuevo debe estar antes de detail para que funcione
    path("nuevo/", TiendaCrear.as_view(), name="Nuevo"),
    path("<pk>/", TiendaDetalle.as_view(), name="Ver"),
    path("editar/<pk>", TiendaModificar.as_view(), name="Editar"),
    path("borrar/<pk>", TiendaBorrar.as_view(), name="Borrar")

#recordar que esta ultima url es la que uso en el template para buscar productos
]

