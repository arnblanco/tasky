from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from .forms import TareaForm

class TareaView(View):
    template_name = 'tareas/home.html'

    def get(self, request):
        user = request.user
        tareas = user.tarea_set.all()
        form = TareaForm()

        return render(request, self.template_name, {'tareas': tareas, 'form': form})

    def post(self, request):
        user = request.user
        form = TareaForm(request.POST)

        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.user = user
            tarea.save()
            return redirect(reverse('tareas:home'))
        
        tareas = user.tarea_set.all()

        return render(request, self.template_name, {'tareas': tareas, 'form': form})

@login_required
def editar_tarea(request, pk, template_name='tareas/editar.html'):
    user = request.user
    tarea = get_object_or_404(user.tarea_set, pk=pk)
    form = TareaForm(instance=tarea)

    if request.POST:
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect(reverse('tareas:home'))
    
    return render(request, template_name, {'form': form})

@login_required
def eliminar_tarea(request, pk):
    user = request.user
    tarea = get_object_or_404(user.tarea_set, pk=pk)
    tarea.delete()
    
    return redirect(reverse('tareas:home'))