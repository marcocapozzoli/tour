from typing import Any, Dict
from uuid import UUID
from core.entities.employee import Employee
from core.exceptions import (
    EntityAlreadyExistsException,
    EntityDoesNotExistsException,
    EntityUpdateException
)
from core.interfaces.repo import IEmployeeRepo


class EmployeeUseCases:
    
    def __init__(self, employee_repo: IEmployeeRepo) -> None:
        self.repo = employee_repo

    def create(self, params: Dict[str, Any]) -> Employee:
        try:
            self._validate(params)
            employee = Employee(**params)
            return self.repo.create(employee=employee)
        except Exception as e:
            raise EntityAlreadyExistsException(
                code='CDUC',
                message='Erro no cadastro do funcionário',
                details=str(e)
            )
    
    def update(self, params: Dict[str, Any]) -> Employee:
        try:
            employee = Employee(**params)
            return self.repo.update(employee=employee)
        except Exception as e:
            raise EntityUpdateException(
                code='UDUC',
                message='Erro na atualização do funcionário',
                details=str(e)
            )
    
    def detail(self, employee_id: UUID) -> Employee:
        try:
            return self.repo.detail(employee_id)
        except Exception:
            raise EntityDoesNotExistsException(
                code='DDUC',
                message='Erro ao obter detalhes do funcionário',
                details=f'Não existe funcionário cadastrado com esse id `{employee_id}`'
            )
    
    def _validate(self, params: Dict[str, Any]):
        if self.repo.is_exist(email=params['email'], department=params['department']):
            raise EntityAlreadyExistsException(
                code='CDUC',
                message='Erro registro do funcionário',
                details=f'Já existe um funcionário cadatrado com esse email nesse departamento'
            )