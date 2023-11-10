"""Tareas api serializers"""
from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    """Taras Serializer"""
    
    class Meta:
        model = Tarea
        fields = '__all__'

    def create(self, validated_data):
        """Verify if user is authenticated"""
        user = getattr(self.context.get('request'), 'user', None)
        validated_data['user'] = user
        return super(TareaSerializer, self).create(validated_data)
