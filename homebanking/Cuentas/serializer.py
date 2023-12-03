from rest_framework import serializers
from .models import Cuentas

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuentas
        fields = '__all__'
