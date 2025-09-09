from django.contrib import admin
from api.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'designation',)

admin.site.register(Employee, EmployeeAdmin)    