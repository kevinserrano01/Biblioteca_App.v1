from django.http import HttpResponse
from django.shortcuts import render, redirect
from biblioteca.models import models Empleado
from biblioteca.forms import CrearNuevoEmpleado


# Funcion de Kev
def desactivar_Registro_Empleado(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)
    empleado.activo = False
    empleado.save()
    return HttpResponse(f'El empleado con el ID: {empleado_id} fue ELIMINADO!')


def listado_empleados(request):
    empleados=Empleado.objects.all()
    context={
        "empleados":empleados,
    }
    return render(request, "Empleados_lista.html", context)

def activar_Registro_Empleado(request, empleado_id):
    """Funcion que activa un registro de empleado"""
    empleado = Empleado.objects.get(id=empleado_id)
    empleado.activo = True
    empleado.save()
    return HttpResponse(f'El empleado con el ID: {empleado_id} fue ELIMINADO!')

def nuevo_empleado(request):
    """CREA NUEVO EMPLEADO"""
    if request.method == 'GET':
        return render(request, 'nuevo_proveedor.html', {
            'formularioEmpleado': CrearNuevoEmpleado()
        })
    else:
        nombreEmpleado = request.POST['nombre']
        apellidoEmpleado = request.POST['apellido']
        legajoEmpleado = request.POST['nro_legajo']
        Empleado.objects.create(nombre=nombreEmpleado, apellido=apellidoEmpleado, nro_legajo=legajoEmpleado)
        return redirect('listado_empleados')  # redirecciona a la url con el name='listado_empleados' en urls.py