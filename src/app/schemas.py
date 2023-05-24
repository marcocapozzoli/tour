from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field, ValidationError, root_validator, EmailStr


class BaseSchema(BaseModel):
    @classmethod
    def validate_data(cls, data: Dict[str, Any]) -> Union[List[Dict], None]:
        try:
            return cls(**data)
        except ValidationError as error:
            raise error


class CompanySchema(BaseSchema):
    street: str = Field(example='Street one')
    city: str = Field(example='Recife')
    country: str = Field(example='Brazil')
    cnpj: str = Field(example='12345678912345')


class DepartmentSchema(BaseSchema):
    company: str = Field(example='b9c25b82-0c1b-4db4-afb9-7ee375fd178e')
    name: str = Field(example='Department one')
    cost_center: str = Field(example='C0001')
    integration_code: str = Field(example='104A')


class EmployeeSchema(BaseSchema):
    full_name: str = Field(example='John Snow')
    email: EmailStr = Field(example='username@example.com')
    phone: str = Field(example='81999999999')
    birthday: str = Field(example='01/01/1985')
    entry_date: str = Field(example='01/01/1985')
    departure_date: str = Field(example='01/01/1985')
    city: str = Field(example='Recife')
    department: str = Field(example='b9c25b82-0c1b-4db4-afb9-7ee375fd178e')

    @root_validator(pre=True, allow_reuse=True)
    def parse_dates(cls, values):
        birthday = values.get('birthday')
        entry_date = values.get('entry_date')
        departure_date = values.get('departure_date')
        if birthday:
            values['birthday'] = cls.parse_date(birthday)
        if entry_date:
            values['entry_date'] = cls.parse_date(entry_date)
        if departure_date:
            values['departure_date'] = cls.parse_date(departure_date)
        return values

    @staticmethod
    def parse_date(value):
        date_object = datetime.strptime(value, '%d/%m/%Y')
        return date_object.strftime('%Y-%m-%d')


class UpdateSchema(BaseSchema):
    id: str
    is_active: Optional[bool] = None


class CreateCompanySchema(CompanySchema):
    ...


class UpdateCompanySchema(CompanySchema, UpdateSchema):
    street: Optional[str] = Field(example='Street one', default=None)
    city: Optional[str] = Field(example='Recife', default=None)
    country: Optional[str] = Field(example='Brazil', default=None)
    cnpj: Optional[str] = Field(example='12345678912345', default=None)


class CreateDepartmentSchema(DepartmentSchema):
    ...


class UpdateDepartmentSchema(DepartmentSchema, UpdateSchema):
    company: Optional[str] = Field(
        example='b9c25b82-0c1b-4db4-afb9-7ee375fd178e', default=None
    )
    name: Optional[str] = Field(example='Department one', default=None)
    cost_center: Optional[str] = Field(example='C0001', default=None)
    integration_code: Optional[str] = Field(example='104A', default=None)


class CreateEmployeeSchema(EmployeeSchema):
    ...


class UpdateEmployeeSchema(EmployeeSchema, UpdateSchema):
    full_name: Optional[EmailStr] = Field(example='John Snow', default=None)
    email: Optional[str] = Field(example='username@example.com', default=None)
    phone: Optional[str] = Field(example='81999999999', default=None)
    birthday: Optional[str] = Field(example='01/01/1985', default=None)
    entry_date: Optional[str] = Field(example='01/01/1985', default=None)
    departure_date: Optional[str] = Field(example='01/01/1985', default=None)
    city: Optional[str] = Field(example='Recife', default=None)
    department: Optional[str] = Field(
        example='b9c25b82-0c1b-4db4-afb9-7ee375fd178e', default=None
    )
