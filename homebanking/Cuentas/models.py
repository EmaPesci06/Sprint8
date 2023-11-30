from django.db import models
from Clientes.models import Cliente

# Create your models here.
class TipoCuenta(models.Model):
    tipo_cuenta = models.CharField(max_length=50)

class Cuenta(models.Model):
    id_cuenta = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='id_cliente')
    id_tipo_cuenta = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE, db_column='id_tipo_cuenta')
    saldo = models.FloatField()
    fecha_creacion = models.DateField()