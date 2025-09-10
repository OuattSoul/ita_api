# employees/models.py
from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email      = models.EmailField(unique=True)
    phone      = models.CharField(max_length=30, blank=True, null=True)
    hire_date = models.DateField(auto_now_add=True)
    job_title   = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    #start_date = models.DateField(blank=True, null=True)
    salary     = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employees'   # force le nom de table à 'employees'
        #ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Conge(models.Model):
    TYPE_CONGE_CHOICES = [
        ('maladie', 'Congé Maladie'),
        ('annuel', 'Congé Annuel'),
        ('maternite', 'Congé Maternité'),
    ]

    employee_id = models.CharField(max_length=20)
    leave_type = models.CharField(max_length=20, choices=TYPE_CONGE_CHOICES)
    reason = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    address_during_leave = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "leave_requests"

    def __str__(self):
        return f"{self.type_conge} - {self.date_debut} → {self.date_fin}"
    

class AssignMission(models.Model):
    URGENCY_LEVEL_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    project = models.CharField(max_length=255)
    mission_type = models.CharField(max_length=100)
    people_count = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    urgency_level = models.CharField(max_length=10, choices=URGENCY_LEVEL_CHOICES)
    special_instructions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project} ({self.mission_type})"
    

class RecruitmentRequest(models.Model):
    JOB_TYPE_CHOICES = [
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('Interim', 'Interim'),
    ]

    STATUS_CHOICES = [
        ('Normal', 'Normal'),
        ('Urgent', 'Urgent'),
        ('Critique', 'Critique'),
    ]

    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES)
    job_title = models.CharField(max_length=255)
    proposed_salary = models.DecimalField(max_digits=12, decimal_places=2)
    requesting_service = models.CharField(max_length=255)
    start_date = models.DateField()
    message = models.TextField(blank=True, null=True)
    status_field = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_title} ({self.job_type})"

