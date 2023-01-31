from django.db import models


# Create your models here.
class Employee(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	phone = models.CharField(max_length=14)
	email = models.EmailField(max_length=50)
	department = models.CharField(max_length=50)
	salary = models.DecimalField(max_digits=10, decimal_places=2)
	employment_date = models.DateField()


# class Meta:
# 	verbose_name = 'employee'
# 	verbose_name_plural = 'employees'

def __str__(self):
    return "{self.firstname} {self.lastname}"
