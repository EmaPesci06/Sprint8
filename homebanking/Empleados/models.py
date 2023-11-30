from django.db import models
from Direcciones.models import Direccion

# Create your models here.
class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    email = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
