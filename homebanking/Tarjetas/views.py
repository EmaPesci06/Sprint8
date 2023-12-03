from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Tarjeta
from .serializer import TarjetasSerializer

# Create your views here.
class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetasSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
