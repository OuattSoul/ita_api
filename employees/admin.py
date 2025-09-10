from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'phone',
        'hire_date',
        'job_type',              
        'employment_type_field', 
        'base_salary',           
        'created_at'
    )
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('job_type', 'employment_type_field')
