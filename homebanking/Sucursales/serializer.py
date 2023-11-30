
from rest_framework import serializers
from .models import Sucursales

class SucursalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursales
        fields = '__all__'
