from rest_framework import viewsets, permissions
from .serializer import PrestamoSerializer
from .models import Prestamo
# Create your views here.
class PrestamosView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]    