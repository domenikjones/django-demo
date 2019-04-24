from rest_framework import serializers

from employees.serializers import EmployeeSerializer
from restaurants.models import Restaurant, Job


class JobSerializer(serializers.ModelSerializer):

    employee = serializers.SerializerMethodField()

    def get_employee(self, obj):
        self.context.update({"job": obj})
        return EmployeeSerializer(obj.employee, many=False, read_only=True, context=self.context).data

    class Meta:
        model = Job
        fields = ('id', 'name', 'salary', 'hours', 'employee')


class RestaurantSerializer(serializers.ModelSerializer):

    employees = serializers.SerializerMethodField()

    def get_employees(self, obj):
        return JobSerializer(
            Job.objects.filter(restaurant=obj), many=True, read_only=True, context={"restaurant": obj}
        ).data

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'zip', 'city', 'country', 'employees')
