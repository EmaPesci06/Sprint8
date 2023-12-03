from rest_framework import viewsets, permissions
from .serializer import DireccionesSerializer
from .models import Direcciones
# Create your views here.
class DireccionesView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Direcciones.objects.all()
    serializer_class = DireccionesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
