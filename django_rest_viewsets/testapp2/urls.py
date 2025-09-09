from django.urls import path, include
from rest_framework.routers import DefaultRouter
from testapp2.views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]