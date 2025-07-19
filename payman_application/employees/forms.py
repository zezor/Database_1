from django import forms
from .models import Employee, Deduction, SalaryDetails

class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['sur_name' 'first_name' 'other_name' 'date_of_birth' 
                  'phone_number' 'email' 'address' 'job_title' 'emp_type']

class SalaryForms(forms.ModelForm):
    class Meta:
        model = SalaryDetails
        fields = ['employee', 'monthly_gross', 'months_worked', 'allowances_percent']

class DeductionForms(forms.ModelForm):
    class Meta:
        model = Deduction
        fields = ['employee', 'name', 'amount']