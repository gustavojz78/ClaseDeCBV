
from msilib.schema import ListView
from django.http import HttpResponse
from TiendApp.forms import *
from django.shortcuts import render, redirect
from TiendApp.models import *

#vistas basadas en clases
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#autenticación con django
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class TiendaLista(LoginRequiredMixin,ListView):
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
@login_required
def inicio(request):
    avatar=Avatar.objects.filter(user=request.user)
    if len(avatar) >0:
        imagen = avatar[0].imagen.url
        return render(request, "tiendapp/index.html",{"imagen_url":imagen})
    else:
        return render(request, "tiendapp/index.html")

@login_required
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

@login_required
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
    
@login_required
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
@login_required
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
            return redirect("Inicio")      
    else:
        mi_form2= AgregarEmpleado(initial={"nombre":empleado.nombre,"apellido":empleado.apellido, "puesto":empleado.puesto, "dni":empleado.dni, "email":empleado.email, "telefono":empleado.telefono} )
        return render(request, "tiendapp/editarEmpleado.html", {"mi_form2":mi_form2, "empleados_dni":empleados_dni})
       
def login_request(request):
    if request.method =="POST":

        form=AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")

            usuario=authenticate(username=usuario, password=contra)
        
            if usuario is not None:
                login(request,usuario)
                avatar=Avatar.objects.filter(user=request.user)
                if len(avatar) >0:
                    imagen = avatar[0].imagen.url
                return render(request, "tiendapp/index.html",{"mensaje":[f"Bienvenid@!!!"]})
            else:
                return render(request, "tiendapp/index.html",{"mensaje": ["Usuario no valido"]})
        else:
                return render(request, "tiendapp/index.html",{"mensaje": ["Error: Datos Incorrectos"]})
    form=AuthenticationForm()

    return render(request,"tiendapp/login.html", {"form":form})

def register_request(request):
    #Con esta view, podemos crear un registro practico,pero...
    #yo quiero el formulario en español. Debo Irme a forms.py e importar el UserCretionForm
    #luego ahí hago creo una clase para  querede de UserCreationForm
    #y esa clase la sustituyo por la clase form aquí

    if request.method == "POST":

        #form = UserCreationForm(request.POST)
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            print(username) 
            form.save()
            return render(request, "tiendapp/index.html", {"mensaje": [f"El usuario {username} fue creado con EXITO"]})
        else:
            return render(request, "tiendapp/index.html",{"mensaje": [" Password NO VALIDO"]} )
    else:
        #form = UserCreationForm()
        form= UsuarioRegistroForm()
    return render(request, "tiendapp/registro.html", {"form": form})


@login_required 
def actualizarUsuario(request):
    
    usuario= request.user
    if request.method == "POST":
            forms = UsuarioEditForm(request.POST)

            if forms.is_valid():
                data = forms.cleaned_data
                usuario.email = data["email"]
                usuario.password1 = data["password1"]
                usuario.password2 = data["password2"]
                usuario.save()

                return render(request, "tiendapp/index.html",{ "mensaje": [f"el correo nuevo es: {usuario.email}"]})
            else:
                forms = UsuarioEditForm(initial={"email": usuario.email})  
                return render(request,  "tiendapp/editarUsuario.html", {"forms": forms, "mensaje": ["Datos invalidos !!!"]})

    else:
        forms = UsuarioEditForm(initial={"email": usuario.email})  
        return render(request,  "tiendapp/editarUsuario.html", {"forms": forms, "mensaje": [f"Actualización del correo electronico de: {usuario}"]})

    
login_required
def cargar_imagen(request):

    if request.method == "POST":

        formulario = AvatarFormulario(request.POST,request.FILES)

        if formulario.is_valid():
            usuario = request.user
            avatar = Avatar.objects.filter(user=usuario)

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()
            else:
                avatar = Avatar(user=usuario, imagen=formulario.cleaned_data["imagen"])
                avatar.save()

        return redirect("Inicio")
    else:

        formulario = AvatarFormulario()
        return render(request, "tiendapp/cargarImagen.html", {"form": formulario})
        

        
        

