from django.db import models
from django.contrib.auth.models import User
from Sucursales.models import Sucursal

class Cliente(models.Model):
    TIPO_CLIENTE = (
        ('CLASSIC', 'CLASSIC'),
        ('GOLD', 'GOLD'),
        ('BLACK', 'BLACK')
    )
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    customer_surname = models.CharField(max_length=50)  # This field type is a guess.
    customer_dni = models.CharField(db_column='customer_DNI', max_length=50)  # Field name made lowercase.
    dob = models.DateField(null=True, blank=True)
    branch = models.ForeignKey(Sucursal, on_delete=models.CASCADE ,null=True, blank=True)
    tipo_cliente = models.CharField(max_length=50, blank=True, null=True, choices=TIPO_CLIENTE)

    class Meta:
        managed = False
        db_table = 'cliente'


    def __str__(self):
        return self.customer_name + " " + self.customer_surname