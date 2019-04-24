from rest_framework import viewsets

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
