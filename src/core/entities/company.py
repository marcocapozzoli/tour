from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from core.exceptions import EntityValidationException
from core.validators import ValidatorFactory


@dataclass
class CompanyEntity:
    street: str
    city: str
    country: str
    cnpj: str
    is_active: Optional[bool] = True
    id: Optional[str] = None
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

    def __post_init__(self):
        self.validate()

    def validate(self):
        if self.cnpj:
            validator = ValidatorFactory.cnpj()
            is_valid = validator.validate(data=self.cnpj)

            if not is_valid:
                raise EntityValidationException(
                    code="EV",
                    message="Esse Cnpj é inválido",
                    details=f"{self.cnpj}",
                )
