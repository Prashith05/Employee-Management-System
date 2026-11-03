from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(
        max_length=20,
        unique=True,
        error_messages={'unique': "An employee with this ID already exists."},
        )
    employee_name = models.CharField(max_length=100)
    employee_email = models.EmailField(
        unique=True,
        error_messages={'unique': "An employee with this email already exists."},
        )
    employee_contact = models.CharField(
        max_length=10,
        unique=True,
        validators=[RegexValidator(r'^\d{10}$', message="Contact number must be 10 digits.")],
        error_messages={'unique': "An employee with this contact number already exists."},
        )

    def __str__(self):
        return self.employee_name
