from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user if self.context['request'].user.is_authenticated else None
        validated_data['user'] = user
        return super(TareaSerializer, self).create(validated_data)