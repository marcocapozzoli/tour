from app.controller import (
    CompanyController,
    DepartmentController,
    EmployeeController,
)
from app.repo import CompanyRepo, DepartmentRepo, EmployeeRepo
from core.usecases.company import CompanyUseCases
from core.usecases.department import DepartmentUseCases
from core.usecases.employee import EmployeeUseCases


class ControllerFactory:
    def __init__(self, name: str) -> None:
        self.name = name

    def company_controller(self):
        return CompanyController

    def company_usecase(self):
        return CompanyUseCases

    def company_repo(self):
        return CompanyRepo

    def department_controller(self):
        return DepartmentController

    def department_usecase(self):
        return DepartmentUseCases

    def department_repo(self):
        return DepartmentRepo

    def employee_controller(self):
        return EmployeeController

    def employee_usecase(self):
        return EmployeeUseCases

    def employee_repo(self):
        return EmployeeRepo


def controller_factory(
    factory,
) -> CompanyController | DepartmentController | EmployeeController:
    company_controller = factory.company_controller()
    company_usecase = factory.company_usecase()
    company_repo = factory.company_repo()

    department_controller = factory.department_controller()
    department_usecase = factory.department_usecase()
    department_repo = factory.department_repo()

    employee_controller = factory.employee_controller()
    employee_usecase = factory.employee_usecase()
    employee_repo = factory.employee_repo()

    if "company" in factory.name:
        return company_controller(
            use_case=company_usecase(company_repo=company_repo())
        )

    if "department" in factory.name:
        return department_controller(
            use_case=department_usecase(department_repo=department_repo())
        )

    if "employee" in factory.name:
        return employee_controller(
            use_case=employee_usecase(employee_repo=employee_repo())
        )
