from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Tarea.objects.filter(user=self.request.user)
        else:
            return Tarea.objects.filter(user=None)