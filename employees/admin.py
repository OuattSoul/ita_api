from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'nationality',
        'birth_date',
        'birth_place',
        'full_address',              
        'phone', 
        'email',           
        'emergency_contact_name',
        'emergency_contact_phone',
        'job_type',
        'diploma',  
        'certificate_file',            
        'additional_training', 
        'professional_certificate',           
        'spoken_languages',
        'language_level',
        'current_position',              
        'company', 
        'start_date',           
        'end_date',
        'moral_reference',
        'portfolio_file',
        'employment_type_field',
        'hire_date',              
        'rattached_service', 
        'occupied_role',
        'base_salary',           
        'bonuses',
        'probation_period'
    )
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('job_type', 'employment_type_field')
