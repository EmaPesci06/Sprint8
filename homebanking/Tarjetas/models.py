from django.db import models

from Clientes.models import Cliente    

class Tarjeta(models.Model):
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
    tarjeta_number = models.CharField(max_length=50)
    cvv = models.CharField(max_length=50)
    issuance_date = models.CharField(max_length=50)
    expiration_date = models.CharField(max_length=50)
    type = models.CharField(max_length=50)