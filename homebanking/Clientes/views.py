# Create your views here.
from rest_framework import generics, permissions
from .models import Cliente
from .serializer import ClienteSerializer
from Direcciones.models import Direcciones
from Direcciones.serializer import DireccionesSerializer
from Sucursales.models import Sucursal
from Sucursales.serializer import SucursalSerializer
from Cuentas.models import Cuentas
from Cuentas.serializer import CuentaSerializer
from Tarjetas.models import Tarjeta
from Tarjetas.serializer import TarjetasSerializer
from Prestamos.models import Prestamo
from Prestamos.serializer import PrestamoSerializer
from Empleados.models import Empleado
from Empleados.serializer import EmpleadoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'Clientes': reverse('clientes-list', request=request, format=format),
        'Sucursales': reverse('sucursales-list', request=request, format=format),
        'Cuentas': reverse('cuentas-list', request=request, format=format),
        'Tarjetas': reverse('tarjetas-list', request=request, format=format),
        'Prestamos': reverse('prestamos-list', request=request, format=format),
        'Direcciones': reverse('direcciones-list', request=request, format=format),
        'Empleados': reverse('empleados-list', request=request, format=format),
    })
class ClientesList(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class DireccionesList(generics.ListAPIView):
    queryset = Direcciones.objects.all()
    serializer_class = DireccionesSerializer

class SucursalesList(generics.ListAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class CuentasList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cuentas.objects.all()
    serializer_class = CuentaSerializer

class TarjetasList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetasSerializer

class PrestamosList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

class EmpleadosList(generics.ListAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

