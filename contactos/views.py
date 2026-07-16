from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import ContactoForm


def inicio(request):
    formulario = ContactoForm()
    contactos = Contacto.objects.all().order_by('nombre')

    return render(request, 'agenda.html', {
        'formulario': formulario,
        'contactos': contactos
    })


def guardar_contacto(request):
    contactos = Contacto.objects.all().order_by('nombre')

    if request.method == 'POST':
        formulario = ContactoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')

        return render(request, 'agenda.html', {
            'formulario': formulario,
            'contactos': contactos
        })

    return redirect('inicio')


def editar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    contactos = Contacto.objects.all().order_by('nombre')

    if request.method == 'POST':
        formulario = ContactoForm(request.POST, instance=contacto)

        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')

    else:
        formulario = ContactoForm(instance=contacto)

    return render(request, 'agenda.html', {
        'formulario': formulario,
        'contactos': contactos,
        'editando': True,
        'contacto': contacto
    })


def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    contacto.delete()
    return redirect('inicio')