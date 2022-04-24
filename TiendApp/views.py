
from msilib.schema import ListView
from django.http import HttpResponse
from TiendApp.forms import *
from django.shortcuts import render
from TiendApp.models import *

#vistas basadas en clases
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class TiendaLista(ListView):
    model = Tiendas
    template_name = "tiendapp/tienda_lista.html"

class TiendaDetalle(DetailView):
    model = Tiendas
    template_name = "tiendapp/tienda_detalle.html"

class TiendaCrear(CreateView):
    model = Tiendas
    success_url= "/tiendapp/tienda/lista"
    fields = ["sucursal","ubicacion"]

class TiendaModificar(UpdateView):
    model = Tiendas
    success_url= "/tiendapp/tienda/lista"
    fields =["sucursal","ubicacion"]

class TiendaBorrar(DeleteView):
    model = Tiendas
    success_url= "/tiendapp/tienda/lista"
   


# Create your views here.
def inicio(request):
     return render(request, "tiendapp/index.html")

def tiendas(request):

     if request.method == "POST":

        mi_formulario1 =AgregarTiendas(request.POST)
        print(mi_formulario1)

        if mi_formulario1.is_valid:
            info=mi_formulario1.cleaned_data
            tiendas= Tiendas(sucursal=info['sucursales'], ubicacion=info['ubicaciones'])
            tiendas.save()
            return render(request, "tiendapp/index.html")
     else:
        mi_formulario1 =AgregarTiendas()

        return render(request, "tiendapp/tiendas.html", {"mi_formulario1": mi_formulario1})


def agenda(request):
    
    if request.method == "POST":

        mi_form =AgregarAgenda(request.POST)
        print(mi_form)

        if mi_form.is_valid:
            info=mi_form.cleaned_data
            contacto= Contacto(telefono=info['telefonos'], email=info['emails'])
            contacto.save()
            return render(request, "tiendapp/index.html")
    else:
        mi_form =AgregarAgenda()
        return render(request, "tiendapp/contactos.html", {"mi_form": mi_form})
    

def staff(request):
#el empleados lo uso para obtener los datos de Staff
     empleados=Staff.objects.all()

     if request.method == "POST":

        mi_form2 =AgregarEmpleado(request.POST)
        print(mi_form2)
        if mi_form2.is_valid:
            info=mi_form2.cleaned_data
            empleado= Staff(nombre=info['nombre'], apellido=info['apellido'], puesto=info['puesto'],dni=info['dni'], telefono=info['telefono'], email=info['email'])
            empleado.save()
            #return render(request, "tiendapp/index.html")

            mi_form2 =AgregarEmpleado()
            return render(request, "tiendapp/staff.html", {"empleado":empleados, "mi_form2":mi_form2})
             #debo fijarme que en el contexto tuve que usar empleado y mi_form2, pero en "empleado":empleados
     else:
        mi_form2 =AgregarEmpleado()
        return render(request, "tiendapp/staff.html", {"empleado":empleados, "mi_form2":mi_form2})
       
def ventas(request):
     return render(request, "tiendapp/ventas.html")

def entrar(request):
    # method = request.method 
    # print(method)

    # data=request.POST
    # print(data)    
    # return render (request, "tiendapp/formulario.html")  
  
    if request.method == "POST":

        mi_formulario =Productos(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid:
            info=mi_formulario.cleaned_data
            ventas= Ventas(id=info['ids'], productos=info['productos'], precio=info['precios'])
            ventas.save()
            return render(request, "tiendapp/index.html")
    else:
        mi_formulario =Productos()

        return render(request, "tiendapp/formulario.html", {"mi_formulario": mi_formulario})

def buscarProducto(request):
    return render(request, "tiendapp/buscarProducto.html")


def buscar(request):
#esta vista es maravillosa. primero si encontramos 'productos' (que practicamente lo generamos con la vista
#buscarProducto, que nos manda al template donde ingresamos los datos, y el a su vez, nos devuelve 'productos'
    if request.GET['productos']:
#fijarme bien en los querys y las variables
        elproducto = request.GET['productos']
        articulos=Ventas.objects.filter(productos__icontains= elproducto)
        return render(request, "tiendapp/resultadoBusqueda.html", {"articulos":articulos, "productos": elproducto})
    else:
        respuesta="No has introducido nada o no esta en existencia"
    return HttpResponse(respuesta)

def eliminarStaff (request, empleados_dni):
    try:
        #el dni es porque es uno de los atributos del modelo Staff y empleados_dn es para diferenciarlo
        staff=Staff.objects.get(dni=empleados_dni)
        staff.delete()
        return render(request, "tiendapp/index.html") 

    except Exception as exc:
        return render(request, "tiendapp/index.html") 

def actualizar (request, empleados_dni):

    empleado=Staff.objects.get(dni=empleados_dni)

    if request.method == "POST":

        mi_form2 =AgregarEmpleado(request.POST)
        print(mi_form2)
        if mi_form2.is_valid:
            info=mi_form2.cleaned_data
            empleado.nombre=info['nombre']
            empleado.apellido=info['apellido']
            empleado.puesto=info['puesto']
            empleado.dni=info['dni']
            empleado.telefono=info['telefono']
            empleado.email=info['email']
            empleado.save()
            return render(request, "tiendapp/index.html")        
    else:
        mi_form2= AgregarEmpleado(initial={"nombre":empleado.nombre,"apellido":empleado.apellido, "puesto":empleado.puesto, "dni":empleado.dni, "email":empleado.email, "telefono":empleado.telefono} )
        return render(request, "tiendapp/editarEmpleado.html", {"mi_form2":mi_form2, "empleados_dni":empleados_dni})
       


  

    
       

