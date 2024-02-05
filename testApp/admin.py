from django.contrib import admin
from testApp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display= ['first_name','last_name','Emp_email','Emp_address','Emp_number','Emp_salary','Emp_Join_Date']
admin.site.register(Employee, EmployeeAdmin)
