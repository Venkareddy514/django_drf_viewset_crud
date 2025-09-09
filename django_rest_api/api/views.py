from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from api.models import Employee
from api.serializers import EmployeeSerailer
from rest_framework.response import Response
# Create your views here.
@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerailer(employee, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeeSerailer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, {'messgage':'Employeee Record Created Successfully'} ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, {'message': 'Invalid Employee input provided.'},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def employee_details(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)      

    if request.method == 'GET':
        serializer = EmployeeSerailer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    elif request.method == 'PUT':
        serializer = EmployeeSerailer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, {'message': 'Employee data Updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return Response({'message': 'Employee Record Deleted successfully.'},status=status.HTTP_204_NO_CONTENT)