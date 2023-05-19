from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from biblioteca.models import models Empleado

# Funcion de Kev
def desactivar_Registro_Empleado(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)
    empleado.activo = False
    empleado.save()
    return HttpResponse(f'El empleado con el ID: {empleado_id} fue ELIMINADO!')


# funcion de Luis
def actualizar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)   
    if request.method == "POST":
        empleado.nombre = request.POST["nombre"]
        empleado.apellido = request.POST["apellido"]
        empleado.numero_legajo = request.POST["numero_legajo"]
        empleado.activo = True if request.POST.get("activo") == "on" else False
        empleado.save()

    context = {
            'empleado': empleado,
        }
    return render(request, "formulario_actualizar_empleado.html", context)