from rest_framework import serializers

from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    weekly_income = serializers.SerializerMethodField()
    weekly_hours = serializers.SerializerMethodField()

    def get_weekly_income(self, obj):
        print("context", self.context)
        return obj.weekly_income(
            restaurant=self.context.get('restaurant', None) if self.context else None,
            job=self.context.get('job', None) if self.context else None,
        )

    def get_weekly_hours(self, obj):
        return obj.weekly_hours(
            restaurant=self.context.get('restaurant', None) if self.context else None,
            job=self.context.get('job', None) if self.context else None,
        )

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'weekly_income', 'weekly_hours')
