from django.db import models
from Direcciones.models import Direccion
from Cuentas.models import Cuenta
from Empleados.models import Empleado

class TipoCliente(models.Model):
    tipo_cuenta = models.CharField(max_length=50)

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    email = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, db_column='id_direccion')
    id_cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, db_column='id_cuenta')
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, db_column='id_empleado')
    tipo_cliente = models.ForeignKey(TipoCliente, on_delete=models.CASCADE, db_column='tipo_cliente')

    def __str__(self):
        return f'{self.nombre} {self.apellido}'