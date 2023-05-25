from typing import Any, Dict
from uuid import UUID

from core.entities.department import DepartmentEntity
from core.exceptions import (
    EntityAlreadyExistsException,
    EntityDoesNotExistsException,
    EntityUpdateException,
)
from core.interfaces.repo import IDepartmentRepo


class DepartmentUseCases:
    def __init__(self, department_repo: IDepartmentRepo) -> None:
        self.repo = department_repo

    def create(self, params: Dict[str, Any]) -> DepartmentEntity:
        try:
            self._validate(params)
            department = DepartmentEntity(**params)
            return self.repo.create(department=department)
        except Exception as e:
            raise EntityAlreadyExistsException(
                code="CDUC",
                message="Erro registro do departamento",
                details=str(e),
            )

    def update(self, params: Dict[str, Any]) -> DepartmentEntity:
        try:
            department = DepartmentEntity(**params)
            return self.repo.update(department=department)
        except Exception as e:
            raise EntityUpdateException(
                code="UDUC",
                message="Erro na atualização da empresa",
                details=str(e),
            )

    def detail(self, department_id: UUID) -> DepartmentEntity:
        try:
            return self.repo.detail(department_id)
        except Exception:
            raise EntityDoesNotExistsException(
                code="DDUC",
                message="Erro ao obter detalhes do departamento",
                details=f"Não existe departamento cadastrado com esse id `{department_id}`",
            )

    def _validate(self, params: Dict[str, Any]):
        if self.repo.is_exist(name=params["name"], company=params["company"]):
            raise EntityAlreadyExistsException(
                code="CDUC",
                message="Erro registro do departamento",
                details="Já existe um departamento com esse nome cadastrado para essa empresa esse",
            )
