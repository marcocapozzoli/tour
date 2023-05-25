from typing import Any, Dict
from uuid import UUID

from app.schemas import (
    CreateCompanySchema,
    CreateDepartmentSchema,
    CreateEmployeeSchema,
    UpdateCompanySchema,
    UpdateDepartmentSchema,
    UpdateEmployeeSchema,
)
from core.entities.company import CompanyEntity
from core.entities.department import DepartmentEntity
from core.entities.employee import EmployeeEntity
from core.interfaces.use_cases import (
    ICompanyUseCases,
    IDepartmentUseCases,
    IEmployeeUseCases,
)


class CompanyController:
    def __init__(self, use_case: ICompanyUseCases) -> None:
        self.usecase = use_case

    def create_object(self, params: Dict[str, Any]) -> CompanyEntity:
        try:
            data = self._validate(CreateCompanySchema, params)
            return self.usecase.create(data.dict())
        except Exception as error:
            raise error

    def update_object(self, params: Dict[str, Any]) -> CompanyEntity:
        try:
            data = self._validate(UpdateCompanySchema, params)
            return self.usecase.update(data.dict())
        except Exception as error:
            raise error

    def detail_object(self, company_id: UUID) -> CompanyEntity:
        return self.usecase.detail(company_id)

    def _validate(
        self,
        schema: CreateCompanySchema | UpdateCompanySchema,
        params: Dict[str, Any],
    ) -> None:
        try:
            return schema.validate_data(params)
        except Exception as error:
            raise error


class DepartmentController:
    def __init__(self, use_case: IDepartmentUseCases) -> None:
        self.usecase = use_case

    def create_object(self, params: Dict[str, Any]) -> DepartmentEntity:
        try:
            data = self._validate(CreateDepartmentSchema, params)
            return self.usecase.create(data.dict())
        except Exception as error:
            raise error

    def update_object(self, params: Dict[str, Any]) -> DepartmentEntity:
        try:
            data = self._validate(UpdateDepartmentSchema, params)
            return self.usecase.update(data.dict())
        except Exception as error:
            raise error

    def detail_object(self, department_id: UUID) -> DepartmentEntity:
        return self.usecase.detail(department_id)

    def _validate(
        self,
        schema: CreateDepartmentSchema | UpdateDepartmentSchema,
        params: Dict[str, Any],
    ) -> None:
        try:
            return schema.validate_data(params)
        except Exception as error:
            raise error


class EmployeeController:
    def __init__(self, use_case: IEmployeeUseCases) -> None:
        self.usecase = use_case

    def create_object(self, params: Dict[str, Any]) -> EmployeeEntity:
        try:
            data = self._validate(CreateEmployeeSchema, params)
            return self.usecase.create(data.dict())
        except Exception as error:
            raise error

    def update_object(self, params: Dict[str, Any]) -> EmployeeEntity:
        try:
            data = self._validate(UpdateEmployeeSchema, params)
            return self.usecase.update(data.dict())
        except Exception as error:
            raise error

    def detail_object(self, employee_id: UUID) -> EmployeeEntity:
        return self.usecase.detail(employee_id)

    def _validate(
        self,
        schema: CreateEmployeeSchema | UpdateEmployeeSchema,
        params: Dict[str, Any],
    ) -> None:
        try:
            return schema.validate_data(params)
        except Exception as error:
            raise error
