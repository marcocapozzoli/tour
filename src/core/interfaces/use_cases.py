from abc import abstractmethod
from typing import Any, Dict, Protocol
from uuid import UUID

from core.entities.company import Company
from core.entities.department import Department
from core.entities.employee import Employee


class ICompanyUseCases(Protocol):
    @abstractmethod
    def create(self, params: Dict[str, Any]) -> Company:
        pass

    @abstractmethod
    def update(self, params: Dict[str, Any]) -> Company:
        pass

    @abstractmethod
    def detail(self, company_id: UUID) -> Company:
        pass


class IDepartmentUseCases(Protocol):
    @abstractmethod
    def create(self, params: Dict[str, Any]) -> Department:
        pass

    @abstractmethod
    def update(self, params: Dict[str, Any]) -> Department:
        pass

    @abstractmethod
    def detail(self, department_id: UUID) -> Department:
        pass


class IEmployeeUseCases(Protocol):
    @abstractmethod
    def create(self, params: Dict[str, Any]) -> Employee:
        pass

    @abstractmethod
    def update(self, params: Dict[str, Any]) -> Employee:
        pass

    @abstractmethod
    def detail(self, employee_id: UUID) -> Employee:
        pass
