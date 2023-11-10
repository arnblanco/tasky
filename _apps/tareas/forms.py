"""Tareas forms"""
from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    """Tareas Form"""
    class Meta:
        """Tareas meta configuration"""
        model = Tarea
        fields = ['titulo', 'email', 'descripcion', 'fecha_vencimiento']
        widgets = {
            'titulo': forms.TextInput(attrs={'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'off'}),
            'descripcion': forms.Textarea(attrs={'autocomplete': 'off'}),
            'fecha_vencimiento': forms.DateTimeInput(attrs={'autocomplete': 'off', 'placeholder': 'YYYY-MM-DD HH:MM'}),
        }
