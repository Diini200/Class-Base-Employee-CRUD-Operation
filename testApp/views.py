from django.shortcuts import render
from testApp.models import Employee
from django.views.generic import ListView, UpdateView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class EmployeeListView(ListView):
    model= Employee
# template_name= Employee_list.html
# context_object_name= object or Employee

class EmployeeDetailView(DetailView):
    model= Employee
    
class EmployeeUpdateView(UpdateView):
    model = Employee
    fields= '__all__'
    # template_name = 'employee_update.html'  
    # success_url = reverse_lazy('employee-list')
  
    
class EmployeeCreateView(CreateView):
    model = Employee
    fields= '__all__'
    
    
class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url= reverse_lazy('employee_list')
