from django.db import models

class Direcciones(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=100)
    customer = models.ForeignKey('Clientes.Cliente', on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey('Empleados.Empleado', on_delete=models.CASCADE, null=True)
    country = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'direcciones'


    def __str__(self) -> str:
        return self.address