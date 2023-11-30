from rest_framework import serializers
from .models import Tarjetas

class TarjetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjetas
        fields = '__all__'
