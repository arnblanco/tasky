"""Tareas api views"""
from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    """"Tareas views set"""
    serializer_class = TareaSerializer

    def get_queryset(self):
        """Custom filter for tareas if user is authenticated"""
        if self.request.user.is_authenticated:
            return Tarea.objects.filter(user=self.request.user)
        return Tarea.objects.filter(user=None)
