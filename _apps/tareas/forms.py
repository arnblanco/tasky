"""Tareas forms"""
from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    """Tareas Form"""
    class Meta:
        """Tareas meta configuration"""
        model = Tarea
        fields = ['titulo', 'email', 'descripcion', 'fecha_vencimiento']
