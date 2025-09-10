# employees/models.py
from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email      = models.EmailField(unique=True)
    phone      = models.CharField(max_length=30, blank=True, null=True)
    position   = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(blank=True, null=True)
    salary     = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employees'   # force le nom de table à 'employees'
        #ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
