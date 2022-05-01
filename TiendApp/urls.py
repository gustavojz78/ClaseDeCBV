from django.urls import path
from TiendApp.views import *
from django.contrib.auth.views import LogoutView
 
urlpatterns = [
    path("", inicio, name="Inicio"),
    path("login/", login_request, name = "Login"),
    path("actualizarUsuario/", actualizarUsuario, name = "Actualizar"),
    path("login/",login_request, name="Login"),
    path("logout",logout, name="Logout"), 
    path("registrar/",register_request, name="Registrar"),
    path("logout/", LogoutView.as_view(template_name="TiendApp/logout.html"), name="Logout"),

    path("tiendas/", tiendas, name = "Tiendas"),
    path("contactos/", agenda, name = "Contacto"),
    path("staff/", staff, name ="Staff"),
    path("ventas/", ventas, name= "Ventas"),
    path("formulario/", entrar, name="Entrar"),
    path("buscarProducto/", buscarProducto, name="Buscar"),
    path("registro/", register_request, name="Registro"),
    path("buscar/", buscar),
    path("borrarEmpleado/<empleados_dni>/", eliminarStaff, name="eliminarEmpleado"),
    path("editarEmpleado/<empleados_dni>/", actualizar, name="editarEmpleado"),
#Estos name, son los que hacen que la url se relacione con el template
#por ejemplo en tienda_lista.html encontramos los url Ver, Editar, Borrar
    path("tienda/lista", TiendaLista.as_view(), name="tienda_lista"),
    path("cargar/", cargar_imagen, name="Cargar_Imagen"),
#El orden de la ruta importa. Nuevo debe estar antes de detail para que funcione
    path("nuevo/", TiendaCrear.as_view(), name="Nuevo"),
    path("<pk>/", TiendaDetalle.as_view(), name="Ver"),
    path("editar/<pk>", TiendaModificar.as_view(), name="Editar"),
    path("borrar/<pk>", TiendaBorrar.as_view(), name="Borrar")

#recordar que esta ultima url es la que uso en el template para buscar productos
]

