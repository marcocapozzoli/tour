from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class EmployeeEntity:
    full_name: str
    email: str
    phone: str
    birthday: datetime
    entry_date: datetime
    departure_date: datetime
    city: str
    department: str
    is_active: Optional[bool] = True
    id: Optional[str] = None
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

    # def __post_init__(self):
    #     self.validate()

    # def validate(self):
    # self._validate_phone()

    # def _validate_phone(self):
    #     validator = ValidatorFactory.phone()
    #     is_valid = validator.validate(data=self.phone)

    #     if not is_valid:
    #         raise EntityValidationException(
    #             code='EV',
    #             message='Esse telefone é inválido',
    #             details=f'{self.phone}'
    #         )
