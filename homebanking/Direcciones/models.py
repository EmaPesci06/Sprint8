from django.db import models
from Clientes.models import Cliente
from Empleados.models import Empleado
from Sucursales.models import Sucursal
class Direcciones(models.Model):
    address = models.OneToOneField(Sucursal, models.CASCADE, primary_key=True)
    customer = models.ForeignKey(Cliente, models.CASCADE)
    employee = models.ForeignKey(Empleado, models.CASCADE)
    address_0 = models.TextField(db_column='address')  # Field renamed because of name conflict.
    country = models.TextField()
