from django.db import models

class Direcciones(models.Model):
    address = models.OneToOneField('Sucursales.Sucursal', on_delete=models.CASCADE, primary_key=True)
    customer = models.ForeignKey('Clientes.Cliente', on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey('Empleados.Empleado', on_delete=models.CASCADE, null=True)
    country = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'direcciones'
