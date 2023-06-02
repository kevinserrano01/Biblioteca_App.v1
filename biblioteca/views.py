from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from biblioteca.models import Autor, Empleado, Socio, Libro, PrestamoLibro
from django.shortcuts import render, redirect
from biblioteca.forms import CrearNuevoEmpleado, ActualizarAutor, CrearNuevoAutor, CrearNuevoSocio, ActualizarSocio, CrearNuevoPrestamo, ActualizarLibro, ActualizarPrestamo, CrearNuevoLibro
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta


#Nai
def home(request):
    
    return render(request, "home.html")

# Kev
def desactivar_Registro_Empleado(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)
    empleado.activo = False
    empleado.save()
    return redirect("listado_empleados")

# funcion de Luis
def actualizar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)   
    if request.method == "POST":
        empleado.nombre = request.POST["nombre"]
        empleado.apellido = request.POST["apellido"]
        empleado.nro_legajo = request.POST["numero_legajo"]
        empleado.activo = True if request.POST.get("activo") == "on" else False
        empleado.save()

    context = {
            'empleado': empleado,
        }
    return render(request, "formulario_actualizar_empleado.html", context)


def listado_empleados(request):
    empleados=Empleado.objects.all()
    context={
        "empleados":empleados,
    }
    return render(request, "Empleados_lista.html", context)

# Kev
def activar_Registro_Empleado(request, empleado_id):
    """Funcion que activa un registro de empleado"""
    empleado = Empleado.objects.get(id=empleado_id)
    empleado.activo = True
    empleado.save()
    return redirect("listado_empleados")

# Kev
def nuevo_empleado(request):
    """CREA NUEVO EMPLEADO"""
    if request.method == 'GET':
        return render(request, 'nuevo_empleado.html', {
            'formularioEmpleado': CrearNuevoEmpleado()
        })
    else:
        nombreEmpleado = request.POST['nombre']
        apellidoEmpleado = request.POST['apellido']
        legajoEmpleado = request.POST['nro_legajo']
        activos = True
        Empleado.objects.create(nombre=nombreEmpleado, apellido=apellidoEmpleado, nro_legajo=legajoEmpleado, activo=activos)
        return redirect('listado_empleados')  # redirecciona a la url con el name='listado_empleados' en urls.py

# Funcion de Gus (desactivar autor)
def desactivar_Registro_Autor(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    autor.activo = False
    autor.save()
    return redirect("listado_autores")

# Funcion de Gus (modificar datos socio)
def actualizar_socios(request, socio_id):
    socio = get_object_or_404(Socio, id=socio_id)
    if request.method == "POST":
        form = ActualizarSocio(request.POST, instance = socio)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/biblioteca/socios/listado')
    else:
        form = ActualizarSocio(instance = socio)
    return render(request, 'actualizar_socio.html', {"formularioActualizarSocio": form})

# Kev
def listado_autores(request):
    autores = Autor.objects.all()
    context={
        "autores":autores,
    }
    return render(request, "autores_lista.html", context)

# Kev
def activar_Registro_Socio(request, socio_id):
    """Funcion que activa un registro de socio"""
    socio = Socio.objects.get(id=socio_id)
    socio.activo = True
    socio.save()
    return redirect("listado_socios")

#Nai
def listado_socios(request):
    socios = Socio.objects.all()
    context = {
        "socios": socios,
    }
    return render(request, "Socios_lista.html", context)

#Nai
def actualizar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    if request.method == "POST":
        form = ActualizarAutor(request.POST, instance = autor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/biblioteca/autores/listado')
    else:
        form = ActualizarAutor(instance = autor)
    return render(request, 'actualizar_autor.html', {"form": form})

# funcion de Luis
def activar_registro_autor(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    autor.activo = True
    autor.save()
    return redirect("listado_autores")


# funcion de Luis Alberto
def desactivar_registro_socio(request, socio_id):
    socio = Socio.objects.get(id=socio_id)
    socio.activo = False
    socio.save()
    return redirect("listado_socios")

# Andrea
def reg_nuevAutores(request):
    if request.method == 'GET':
        return render(request, 'nuevo_autor.html', {
            'formularioautor': CrearNuevoAutor()
        })
    else:
        #request.POST:
        nombre=request.POST['nombre']
        apellido=request.POST['apellido']
        nacionalidad=request.POST['nacionalidad']
        activo = True

        Autor.objects.create(
            nombre=nombre,
            apellido=apellido,
            nacionalidad=nacionalidad,
            activo = activo
        )
    return redirect('listado_autores')

# Andrea
def reg_nuevSocios(request):
    if request.method == 'GET':
        return render(request, 'nuevo_socio.html', {
            'formulario_socio': CrearNuevoSocio()
        })
    else:
        nombre=request.POST['nombre']
        apellido=request.POST['apellido']
        nacimiento=request.POST['fecha_nacimiento']
        activo = True

        Socio.objects.create(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=nacimiento,
            activo = activo
        )
    return redirect('listado_socios')

#Funcion Gus
def activar_registro_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    libro.activo = True
    libro.save()
    return redirect("libros_lista") #chequear nombre   

#Funcion Gus
def listado_prestamolibro(request):
    prestamos = PrestamoLibro.objects.all()
    context = {
        "prestamos": prestamos,
    }
    return render(request, "prestamos_lista.html", context) #chequear nombre


#Nai
def actualizar_libro(request, libro_id:int):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == "POST":
        form = ActualizarLibro(request.POST, instance = libro)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/biblioteca/libro/listado')
    else:
        form = ActualizarLibro(instance = libro)
    return render(request, 'actualizar_libro.html', {"form": form})

#Nai
def desactivar_libro(request, libro_id:int):
    libro = Libro.objects.get(id=libro_id)
    libro.activo = False
    libro.save()
    return redirect("libros_lista")

#Nai
def nuevo_prestamo_libro(request):
    if request.method == 'POST':
        form = CrearNuevoPrestamo(request.POST)
        if form.is_valid():
            fecha_prestamo = form.cleaned_data['fecha_prestamos']
            fecha_devolucion =fecha_prestamo + timedelta(days=2)
            socio = form.cleaned_data['socio']
            empleado = form.cleaned_data['empleado']
            libro = form.cleaned_data['libro']

            nuevo_prestamo = PrestamoLibro(
                fecha_prestamos=fecha_prestamo,
                fecha_devolucion=fecha_devolucion,
                socio=socio,
                empleado=empleado,
                libro=libro
            )
            nuevo_prestamo.save()

            return redirect('listado_prestamolibro')
    else:
        form = CrearNuevoPrestamo()

    return render(request, 'prestamo_libro.html',{"form": form})

# Kev
def actualizar_Prestamo_Libro(request, prestamoLibro_id:int):

    """Funcion que actualiza un registro de un prestamo de libro en el sistema.

    Args:
        prestamoLibro_id (int): id de un prestamo.
    """
    prestamo = get_object_or_404(PrestamoLibro, id=prestamoLibro_id)
    if request.method == "POST":
        form = ActualizarPrestamo(request.POST, instance = prestamo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/biblioteca/prestamos/listado')
    else:
        form = ActualizarPrestamo(instance = prestamo)
    return render(request, 'actualiza_prestamo.html', {"formularioActualizarPrestamo": form})

# Kev
def nuevo_libro(request):
    """Funcion que crea un nuevo libro y lo guarda en la base de datos.

    Args:
        request (_type_): _description_

    Returns:
        redirec: Redirecciona al template listado_libros una vez creado el libro.
    """
    if request.method == 'POST':
        form = CrearNuevoLibro(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            descripcion = form.cleaned_data['descripcion']
            isbn = form.cleaned_data['isbn']
            autor = form.cleaned_data['autor']

            nuevo_libro = Libro(
                titulo=titulo,
                descripcion=descripcion,
                isbn=isbn,
                autor=autor
            )
            nuevo_libro.save()

            return redirect('libros_lista')
    else:
        form = CrearNuevoLibro()

    return render(request, 'nuevo_libro.html', {"form": form})

#Andrea
def eliminar_regPrestamo(request, prestamoLibro_id):
    regPrestamp= PrestamoLibro.objects.get(id=prestamoLibro_id)
    regPrestamp.delete()
    return redirect('listado_prestamolibro')


def listado_libro(request):
    libros = Libro.objects.all()
    context = {
        "libros": libros,
    }
    return render(request, "libros_lista.html", context) 



