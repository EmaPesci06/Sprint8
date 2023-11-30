from django.db import models

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=50,)
    employee_surname = models.CharField(max_length=50,)
    employee_hire_date = models.CharField(max_length=50,)
    employee_dni = models.CharField(max_length=50,db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()
