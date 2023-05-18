from django.http import HttpResponse
from django.shortcuts import render
from biblioteca.models import models Empleado

def funcioGus(request):
    pass
#prueba  las 00.33 am
# Funcion de Kev
def desactivar_Registro_Empleado(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)
    empleado.activo = False
    empleado.save()
    return HttpResponse(f'El empleado con el ID: {empleado_id} fue ELIMINADO!')
