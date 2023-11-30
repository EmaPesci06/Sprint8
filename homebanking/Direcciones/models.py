from django.db import models

# Create your models here.
class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    piso = models.IntegerField()
    departamento = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    codigo_postal = models.IntegerField()