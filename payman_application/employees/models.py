from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    EM_TYPE_CHOICES = [
        ('PT', 'Part Time'),
        ('FT', 'Full Time'),
        ('other', 'other')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sur_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    job_title = models.CharField(max_length=100)
    emp_type = models.CharField(max_length=100, choices= EM_TYPE_CHOICES)

    def __str__(self):
        return f"{self.first_name + self.sur_name } ({self.job_title})"

class SalaryDetails(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    monthly_gross = models.FloatField()
    months_worked = models.PositiveIntegerField()
    allowances_percent = models.FloatField()

    def monthly_gross_salary(self):
        return self.monthly_gross * self.months_worked

    def allowance_amount(self):
        return (self.allowances_percent / 100) * self.monthly_gross_salary()

    def total_salary(self):
        self.monthly_gross_salary() + self.allowance_amount()

class Deduction(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="deductions")
    name = models.CharField(max_length=200)
    amount = models.FloatField()