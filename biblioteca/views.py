from django.http import HttpResponse
from django.shortcuts import render
from biblioteca.models import models Empleado


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
