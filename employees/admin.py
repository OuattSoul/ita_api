from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','phone','hire_date','job_title','salary','department','created_at','updated_at')
    search_fields = ('first_name','last_name','email')
    list_filter = ('department','job_title')
