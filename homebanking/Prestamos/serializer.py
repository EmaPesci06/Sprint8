
class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'
from rest_framework import serializers
from .models import Prestamo
