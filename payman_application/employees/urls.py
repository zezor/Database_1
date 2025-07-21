from django.urls import  path
from . import views



urlpatterns = [
    path('create', views.create_employee, name = 'create_employees'),
    path('employee/<int:pk>/', views.employee_details, name = 'employee_details'),
    path('register', views.register, name='register')
]