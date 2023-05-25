from abc import abstractmethod
from typing import Any, Dict, Protocol
from uuid import UUID

from core.entities.company import CompanyEntity
from core.entities.department import DepartmentEntity
from core.entities.employee import EmployeeEntity


class ICompanyUseCases(Protocol):
    @abstractmethod
    def create(self, params: Dict[str, Any]) -> CompanyEntity:
        pass

    @abstractmethod
    def update(self, params: Dict[str, Any]) -> CompanyEntity:
        pass

    @abstractmethod
    def detail(self, company_id: UUID) -> CompanyEntity:
        pass


class IDepartmentUseCases(Protocol):
    @abstractmethod
    def create(self, params: Dict[str, Any]) -> DepartmentEntity:
        pass

    @abstractmethod
    def update(self, params: Dict[str, Any]) -> DepartmentEntity:
        pass

    @abstractmethod
    def detail(self, department_id: UUID) -> DepartmentEntity:
        pass


class IEmployeeUseCases(Protocol):
    @abstractmethod
    def create(self, params: Dict[str, Any]) -> EmployeeEntity:
        pass

    @abstractmethod
    def update(self, params: Dict[str, Any]) -> EmployeeEntity:
        pass

    @abstractmethod
    def detail(self, employee_id: UUID) -> EmployeeEntity:
        pass
