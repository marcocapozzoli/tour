from rest_framework.serializers import ModelSerializer

from infra.tour.models.company import Company
from infra.tour.models.departmant import Department
from infra.tour.models.employee import Employee


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
