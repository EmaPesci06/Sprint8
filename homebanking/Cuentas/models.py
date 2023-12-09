from django.db import models

# Create your models here.

class Cuentas(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.CharField(max_length=50)
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'
    
    def __str__(self):
        return self.type