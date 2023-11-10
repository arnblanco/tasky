"""Tareas app urls"""
from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import TareaView, editar_tarea, eliminar_tarea

urlpatterns = [
    path('', login_required(TareaView.as_view()), name='home'),
    path('<int:pk>/editar/', editar_tarea, name='editar'),
    path('<int:pk>/eliminar/', eliminar_tarea, name='eliminar'),
]
