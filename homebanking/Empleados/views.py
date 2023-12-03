from rest_framework import viewsets, permissions
from .serializer import EmpleadoSerializer
from .models import Empleado


# Create your views here.
class EmpleadosView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]    