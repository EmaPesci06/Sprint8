from django.db import models

class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.CharField(max_length=50)
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'