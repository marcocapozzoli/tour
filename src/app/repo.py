from uuid import UUID

from core.entities.company import Company as CompanyEntity
from core.entities.department import Department as DepartmentEntity
from core.entities.employee import Employee as EmployeeEntity
from infra.register.models import Company as CompanyModel
from infra.register.models import Department as DepartmentModel
from infra.register.models import Employee as EmployeeModel


class CompanyRepo:
    def __init__(self):
        self.manager = CompanyModel.objects

    def create(self, company: CompanyEntity) -> CompanyEntity:
        instance = CompanyModel.from_entity(company)
        self._save(instance)
        return instance.to_entity()

    def update(self, company: CompanyEntity) -> CompanyEntity:
        filtered_data = {
            key: value
            for key, value in company.__dict__.items()
            if value is not None
        }
        current_company = self._get(filtered_data.pop('id'))

        current_company.update(**filtered_data)

        return current_company[0].to_entity()

    def detail(self, id: UUID) -> CompanyEntity:
        instance = self._get(id)
        return instance[0].to_entity()

    def is_exist(self, cnpj: str) -> bool:
        company = self.manager.filter(cnpj=cnpj)
        return company.exists()

    def _save(self, instance):
        try:
            instance.save()
        except Exception as e:
            raise e

    def _get(self, id: UUID) -> CompanyModel:
        try:
            return self.manager.filter(id=id)
        except Exception as error:
            raise error


class DepartmentRepo:
    def __init__(self):
        self.manager = DepartmentModel.objects
        self.company_manager = CompanyModel.objects

    def create(self, department: DepartmentEntity) -> DepartmentEntity:
        instance = DepartmentModel.from_entity(department)
        instance.company = self._get_company(department.company)
        self._save(instance)
        return instance.to_entity()

    def update(self, department: DepartmentEntity) -> DepartmentEntity:
        filtered_data = {
            key: value
            for key, value in department.__dict__.items()
            if value is not None
        }
        if 'company' in filtered_data:
            filtered_data['company'] = self._get_company(department.company)

        current_department = self._get(filtered_data.pop('id'))

        current_department.update(**filtered_data)

        return current_department[0].to_entity()

    def detail(self, id: UUID) -> DepartmentEntity:
        instance = self._get(id)
        return instance[0].to_entity()

    def is_exist(self, name: str, company: UUID) -> bool:
        self._get_company(company_id=company)
        department = self.manager.filter(name=name, company=company)
        return department.exists()

    def _save(self, instance):
        try:
            instance.save()
        except Exception as e:
            raise e

    def _get(self, id: UUID) -> DepartmentModel:
        try:
            return self.manager.filter(id=id)
        except Exception as error:
            raise error

    def _get_company(self, company_id: UUID) -> CompanyModel:
        try:
            return self.company_manager.get(id=company_id)
        except Exception as error:
            raise error


class EmployeeRepo:
    def __init__(self):
        self.manager = EmployeeModel.objects
        self.department_manager = DepartmentModel.objects

    def create(self, employee: EmployeeEntity) -> EmployeeEntity:
        instance = EmployeeModel.from_entity(employee)
        instance.department = self._get_department(employee.department)
        self._save(instance)
        return instance.to_entity()

    def update(self, employee: EmployeeEntity) -> EmployeeEntity:
        filtered_data = {
            key: value
            for key, value in employee.__dict__.items()
            if value is not None
        }
        if 'department' in filtered_data:
            filtered_data['department'] = self._get_department(
                employee.department
            )

        current_employee = self._get(filtered_data.pop('id'))

        current_employee.update(**filtered_data)

        return current_employee[0].to_entity()

    def detail(self, id: UUID) -> EmployeeEntity:
        instance = self._get(id)
        return instance[0].to_entity()

    def is_exist(self, email: str, department: UUID) -> bool:
        self._get_department(department_id=department)
        employee = self.manager.filter(email=email, department=department)
        return employee.exists()

    def _save(self, instance):
        try:
            instance.save()
        except Exception as e:
            raise e

    def _get(self, id: UUID) -> EmployeeModel:
        try:
            return self.manager.filter(id=id)
        except Exception as error:
            raise error

    def _get_department(self, department_id: UUID) -> DepartmentModel:
        try:
            return self.department_manager.get(id=department_id)
        except Exception as error:
            raise error
