from django.db import models

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    customer_surname = models.CharField(max_length=50)  # This field type is a guess.
    customer_dni = models.CharField(db_column='customer_DNI', max_length=50)  # Field name made lowercase.
    dob = models.CharField(max_length=50, blank=True, null=True)  # This field type is a guess.
    branch_id = models.DateField()
    tipo_cliente = models.CharField(max_length=50, blank=True, null=True)
    # user= models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) 