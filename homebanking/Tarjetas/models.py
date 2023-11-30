from django.db import models
# Create your models here.

class TipoTarjeta(models.Model):
    tipo_tarjeta = models.CharField(max_length=50)


class Tarjeta(models.Model):
    id_tarjeta = models.AutoField(primary_key=True)
    id_cuenta = models.ForeignKey("Cuentas.Cuenta" , on_delete=models.CASCADE, db_column='id_cuenta')
    id_tipo_tarjeta = models.ForeignKey("Tarjetas.TipoTarjeta", on_delete=models.CASCADE, db_column='id_tipo_tarjeta')
    numero = models.IntegerField()
    fecha_vencimiento = models.DateField()
    codigo_seguridad = models.IntegerField()
    estado = models.CharField(max_length=50)
