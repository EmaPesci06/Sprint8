from django.db import models

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100,)
    employee_surname = models.CharField(max_length=100,)
    employee_hire_date = models.CharField(max_length=100,)
    employee_dni = models.CharField(max_length=100,db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'
