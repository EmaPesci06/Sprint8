from django.db import models


class Tarjeta(models.Model):
    customer = models.ForeignKey('Clientes.Cliente', models.DO_NOTHING)
    tarjeta_number = models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)
    issuance_date = models.CharField(max_length=100)
    expiration_date = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tarjeta'
