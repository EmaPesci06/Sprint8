from django.db import models
from Direcciones.models import Direccion

# Create your models here.
class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.CharField(max_length=50)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, db_column='id_direccion')
