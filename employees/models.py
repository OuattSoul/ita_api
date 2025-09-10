# employees/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random



class AppUserManager(BaseUserManager):
    def create_user(self, user_email, password=None, **extra_fields):
        if not user_email:
            raise ValueError('Email requis')
        user = self.model(user_email=self.normalize_email(user_email), **extra_fields)
        user.set_password(password)
        user.access_code = "{:04d}".format(random.randint(0, 9999))  # 4 chiffres
        user.save(using=self._db)
        return user

class AppUser(AbstractBaseUser):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    user_email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)
    access_code = models.CharField(max_length=4, blank=True)
    
    objects = AppUserManager()

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['fname', 'lname', 'role']

    def __str__(self):
        return self.user_email


class ITAEmployeeModel(models.Model):
    # --- Champs personnels ---
    first_name = models.CharField(max_length=100,default="")
    last_name = models.CharField(max_length=100,default="")
    nationality = models.CharField(max_length=100,default="")
    birth_date = models.DateField(null=True)
    birth_place = models.CharField(max_length=150,default="")
    full_address = models.TextField(default="")
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(unique=True, default="")
    emergency_contact_name = models.CharField(max_length=150, default="")
    emergency_contact_phone = models.CharField(max_length=20, default="")

    # --- Champs professionnels ---
    JOB_TYPE_CHOICES = [
        ('CDD', 'CDD'),
        ('CDI', 'CDI'),
        ('Interim', 'Interim'),
    ]
    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES, default="")
    diploma = models.CharField(max_length=255, blank=True, null=True)
    certificate_file = models.FileField(upload_to="certificates/", blank=True, null=True)
    additional_training = models.TextField(blank=True, null=True)
    professional_certificate = models.CharField(max_length=255, blank=True, null=True)
    spoken_languages = models.TextField(blank=True, null=True)

    LANGUAGE_LEVEL_CHOICES = [
        ('A1', 'A1'),
        ('B1', 'B1'),
        ('B2', 'B2'),
    ]
    language_level = models.CharField(max_length=2, choices=LANGUAGE_LEVEL_CHOICES, blank=True, null=True)

    # --- Job actuel ---
    current_position = models.CharField(max_length=150, blank=True, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    moral_reference = models.CharField(max_length=150, blank=True, null=True)
    portfolio_file = models.FileField(upload_to="portfolios/", blank=True, null=True)

    # --- Informations contractuelles ---
    employment_type_field = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES, default="")
    hire_date = models.DateField(null=True)
    rattached_service = models.CharField(max_length=150, null=True)
    occupied_role = models.CharField(max_length=150, null=True)
    base_salary = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    bonuses = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    probation_period = models.DateField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "ita_employees_list"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.job_type})"

class TestModel(models.Model):
    
    nom = models.TextField()
    prenom = models.TextField()
    email = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "test_requests"

    def __str__(self):
        return f"{self.type_conge} - {self.date_debut} → {self.date_fin}"


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


class EmployeeList(models.Model):
    # --- Champs personnels ---
    first_name = models.CharField(max_length=100,default="")
    last_name = models.CharField(max_length=100,default="")
    nationality = models.CharField(max_length=100,default="")
    birth_date = models.DateField(null=True)
    birth_place = models.CharField(max_length=150,default="")
    full_address = models.TextField(default="")
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(unique=True, default="")
    emergency_contact_name = models.CharField(max_length=150, default="")
    emergency_contact_phone = models.CharField(max_length=20, default="")

    # --- Champs professionnels ---
    JOB_TYPE_CHOICES = [
        ('CDD', 'CDD'),
        ('CDI', 'CDI'),
        ('Interim', 'Interim'),
    ]
    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES, default="")
    diploma = models.CharField(max_length=255, blank=True, null=True)
    certificate_file = models.FileField(upload_to="certificates/", blank=True, null=True)
    additional_training = models.TextField(blank=True, null=True)
    professional_certificate = models.CharField(max_length=255, blank=True, null=True)
    spoken_languages = models.TextField(blank=True, null=True)

    LANGUAGE_LEVEL_CHOICES = [
        ('A1', 'A1'),
        ('B1', 'B1'),
        ('B2', 'B2'),
    ]
    language_level = models.CharField(max_length=2, choices=LANGUAGE_LEVEL_CHOICES, blank=True, null=True)

    # --- Job actuel ---
    current_position = models.CharField(max_length=150, blank=True, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    moral_reference = models.CharField(max_length=150, blank=True, null=True)
    portfolio_file = models.FileField(upload_to="portfolios/", blank=True, null=True)

    # --- Informations contractuelles ---
    employment_type_field = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES, default="")
    hire_date = models.DateField(null=True)
    rattached_service = models.CharField(max_length=150, null=True)
    occupied_role = models.CharField(max_length=150, null=True)
    base_salary = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    bonuses = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    probation_period = models.DateField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "employees-list"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.job_type})"


class AppUserProfile(models.Model):
    # Lien vers le User principal
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

    # Rôles ou permissions spécifiques
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
        ('guest', 'Guest')
    ], default='employee')

    department = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    phone_alternate = models.CharField(max_length=20, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_profiles"

    def __str__(self):
        return f"{self.user.email} - {self.role}"


