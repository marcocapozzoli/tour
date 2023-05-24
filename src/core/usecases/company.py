from typing import Any, Dict
from uuid import UUID
from core.entities.company import Company
from core.exceptions import (
    EntityAlreadyExistsException,
    EntityDoesNotExistsException,
    EntityUpdateException
)
from core.interfaces.repo import ICompanyRepo


class CompanyUseCases:
    
    def __init__(self, company_repo: ICompanyRepo) -> None:
        self.repo = company_repo

    def create(self, params: Dict[str, Any]) -> Company:
        try:
            self._validate(params)
            company = Company(**params)
            return self.repo.create(company=company)
        except Exception as e:
            raise EntityAlreadyExistsException(
                code='CCUC',
                message='Erro registro da empresa',
                details=str(e)
            )
    
    def update(self, params: Dict[str, Any]) -> Company:
        try:
            company = Company(**params)
            return self.repo.update(company=company)
        except Exception as e:
            raise EntityUpdateException(
                code='UCUC',
                message='Erro na atualização da empresa',
                details=str(e)
            )
    
    def detail(self, company_id: UUID) -> Company:
        try:
            return self.repo.detail(company_id)
        except Exception:
            raise EntityDoesNotExistsException(
                code='DCUC',
                message='Erro ao obter detalhes da empresa',
                details=f'Não existe empresa cadastrada com esse id `{company_id}`'
            )

    def _validate(self, params: Dict[str, Any]):
        if self.repo.is_exist(cnpj=params['cnpj']):
            raise EntityAlreadyExistsException(
                code='CCUC',
                message='Erro registro da empresa',
                details=f'Já existe uma empresa cadastrada com esse cnpj `{params["cnpj"]}`'
            )