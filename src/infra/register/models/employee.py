from django.db import models
from infra.register.models import Base, Department
from core.entities.employee import Employee as EmployeeEntity


class Employee(Base):
    full_name = models.CharField('Full name', max_length=128, help_text='Nome completo')
    email =  models.CharField('E-mail', max_length=64, unique=True, help_text='Email')
    phone =  models.CharField('Phone', max_length=14, help_text='Telefone')
    birthday = models.DateField('Birthday', help_text='Data de aniversário')
    entry_date =  models.DateField('Entry date', help_text='Data de ingresso')
    departure_date =  models.DateField('Departure date', help_text='Data de desligamento')
    city =  models.CharField('City', max_length=32, help_text='Cidade')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


    @classmethod
    def from_entity(cls, employee: EmployeeEntity):
        return cls(
            full_name=employee.full_name,
            email=employee.email,
            phone=employee.phone,
            birthday=employee.birthday,
            entry_date=employee.entry_date,
            departure_date=employee.departure_date,
            city=employee.city
        )
    
    def to_entity(self):
        return EmployeeEntity(
            id=str(self.id),
            full_name=self.full_name,
            email=self.email,
            phone=self.phone,
            birthday=self.birthday,
            entry_date=self.entry_date,
            departure_date=self.departure_date,
            city=self.city,
            department=str(self.department_id),
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at
        )