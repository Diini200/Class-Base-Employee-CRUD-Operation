from django.db import models

from django.urls import reverse

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)
    Emp_email= models.EmailField()
    Emp_address= models.CharField(max_length=162)
    Emp_number= models.IntegerField()
    Emp_salary= models.FloatField()
    Emp_Join_Date= models.DateField()
    
    id = models.AutoField(primary_key=True)
    
    def get_absolute_url(self):
        return reverse('details', kwargs={"pk": self.pk})
    
    
    
    