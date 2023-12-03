from rest_framework import viewsets, permissions
from .serializer import CuentaSerializer
from .models import Cuentas

# Create your views here.
class CuentaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cuentas.objects.all()
    serializer_class = CuentaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]