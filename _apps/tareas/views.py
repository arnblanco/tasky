from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Tarea
from .forms import TareaForm

@login_required
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

    def put(self, request, tarea_id):
        user = request.user
        tarea = get_object_or_404(Tarea, pk=tarea_id)
        form = TareaForm(request.POST, instance=tarea)

        if form.is_valid():
            form.save()
            return redirect(reverse('tareas:home'))
        
        tareas = user.tarea_set.all()
        
        return render(request, self.template_name, {'tareas': tareas, 'form': form})

    def delete(self, request, tarea_id):
        user = request.user
        tarea = get_object_or_404(user.tarea_set, pk=tarea_id)
        tarea.delete()
        
        return redirect(reverse('tareas:home'))