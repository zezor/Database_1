from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee, Deduction, SalaryDetails
from .forms import EmployeeForms, SalaryForms, DeductionForms
from .serializers import EmployeesViewSerializer
from rest_framework import generics
from rest_framework.response import Response


# Create your views here.
@login_required
def create_employee(request):
    if request.method == "POST":
        em_form = EmployeeForms(request.POST)
        salary_form = SalaryForms(request.POST)

        if em_form.is_valid() and salary_form.is_valid():
            employee = em_form.save(commit=False)  # using commit = false not save to the database
            employee.user = request.user
            employee.save()

            salary = salary_form.save(commit=False)
            salary.employee = employee
            salary.save()

            return  redirect('employee_detail', employee.id)
    else:
        em_form = EmployeeForms()
        salary_form = SalaryForms()
    return render(request, 'employees/create_employee.html', {
        "em_form":em_form,
        "salary_forms":salary_form
        })

@login_required
def employee_details(request, pk):
    employee = Employee.object.get(pk=pk)
    salary = SalaryDetails.object.get(employee=employee)
    deductions = Deduction.object.filter(employee=employee)
    #serch for django aggregations
    total_deductions = sum(e.amount for e in deductions)
    net_pay = salary.total_salary() - total_deductions
    weekly_pay = net_pay // (salary.months_worked * 4)

    return render(
        request,
        'employees/employee_details.html',{
            'employee' : employee,
            'salary': salary,
            'net_pay': net_pay,
            'weekly_pay': weekly_pay,
            'deductions': deductions
        })

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html",{'form':form})

class MyModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeesViewSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'status': True,
            'message': 'Employee list retrieved successfully.',
            'data': serializer.data
        })