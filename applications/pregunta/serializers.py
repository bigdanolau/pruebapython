from rest_framework import serializers
from .models import Pregunta
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pregunta
        fields = (
            'id',
            'titulo',
            'contenido'
        )