from django.urls import  path

from . import views
from ..payman_application.urls import urlpatterns

urlpatterns = [
    path('create', views.create_employee, name = 'create_employees'),
    path('employee/<int:pk/>', views.employee_details, name = 'employee_details')
]