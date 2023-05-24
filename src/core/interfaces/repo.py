from abc import abstractmethod
from typing import Protocol
from core.entities.company import Company as CompanyEntity
from core.entities.department import Department as DepartmentEntity
from core.entities.employee import Employee as EmployeeEntity
from uuid import UUID


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

    
    