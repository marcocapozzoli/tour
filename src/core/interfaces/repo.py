from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from core.entities.company import CompanyEntity
from core.entities.department import DepartmentEntity
from core.entities.employee import EmployeeEntity


class ICompanyRepo(Protocol):
    @abstractmethod
    def create(self, company: CompanyEntity) -> CompanyEntity:
        pass

    @abstractmethod
    def update(self, company: CompanyEntity) -> CompanyEntity:
        pass

    @abstractmethod
    def detail(self, id: UUID) -> CompanyEntity:
        pass


class IDepartmentRepo(Protocol):
    @abstractmethod
    def create(self, department: DepartmentEntity) -> DepartmentEntity:
        pass

    @abstractmethod
    def update(self, department: DepartmentEntity) -> DepartmentEntity:
        pass

    @abstractmethod
    def detail(self, id: UUID) -> DepartmentEntity:
        pass


class IEmployeeRepo(Protocol):
    @abstractmethod
    def create(self, employee: EmployeeEntity) -> EmployeeEntity:
        pass

    @abstractmethod
    def update(self, employee: EmployeeEntity) -> EmployeeEntity:
        pass

    @abstractmethod
    def detail(self, id: UUID) -> EmployeeEntity:
        pass
