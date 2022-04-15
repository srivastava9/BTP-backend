from http import server
from django.shortcuts import render
from rest_framework import generics
from industry.models import Employee

from industry.serializers import EmployeeListSerializers

# Create your views here.
class ListEmployeesView(generics.ListAPIView):
    serializer_class = EmployeeListSerializers

    def get_queryset(self):
        return Employee.objects.filter(factory_id=self.kwargs.get("factory_id"))
