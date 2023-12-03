from rest_framework import viewsets, permissions
from .models import Sucursal
from .serializer import SucursalSerializer

# Create your views here.
class SucursalView(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]