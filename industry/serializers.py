from rest_framework import serializers

from industry.models import Employee


class EmployeeListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("__all__",)
