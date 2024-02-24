from django.shortcuts import render, redirect, get_object_or_404
from .models import Trabajador
from .forms import TrabajadorForm
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse, HttpResponseForbidden
from django.urls import reverse

def listar_trabajadores(request):
    trabajadores = Trabajador.objects.all()
    return render(request, 'list_trab.html', {'trabajadores': trabajadores})

def crear_trabajador(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():

            Trabajador = form.save(commit=False)
            
            Trabajador.save()

            
            return HttpResponseRedirect(reverse('list_trab'))
        
    else:
        form = TrabajadorForm()
        context = {
           'form_trab': form,
           
       }
        
   
    return render(request, 'crear_trabajador.html',context )




def editar_trabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)

    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
           
            form.save()
               
            return HttpResponseRedirect(reverse('list_trab'))
    else:
        form = TrabajadorForm(instance= trabajador)
        context = {
            'form_trab': form,

        }
    return render(request, 'editar_trab.html', context)

def eliminar_trabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    trabajador.delete()
    return redirect('list_trab')
