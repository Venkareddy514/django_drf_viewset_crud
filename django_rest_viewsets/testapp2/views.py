from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = PageNumberPagination
    #pagination_class = LimitOffsetPagination
   # pagination_class = CursorPagination
    # cursor_order = '- employee_id'