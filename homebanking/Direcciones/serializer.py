from rest_framework import serializers
from .models import Direcciones

class DireccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direcciones
        fields = '__all__'
