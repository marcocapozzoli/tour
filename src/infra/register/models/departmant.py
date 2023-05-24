from django.db import models
from infra.register.models import Base
from core.entities.department import Department as DepartmentEntity


class Department(Base):
    name = models.CharField('Name', max_length=64, help_text='Nome')
    cost_center = models.CharField('Cost center', max_length=64, help_text='Centro de custo')
    integration_code = models.CharField('Integration code', max_length=64, help_text='Código de integração')
    company = models.ForeignKey('company', on_delete=models.CASCADE)

    @staticmethod
    def from_entity(department: DepartmentEntity):
        return Department(
            name=department.name,
            integration_code=department.integration_code,
            cost_center=department.cost_center
        )
    
    def to_entity(self):
        return DepartmentEntity(
            id=str(self.id),
            name=self.name,
            integration_code=self.integration_code,
            cost_center=self.cost_center,
            company=str(self.company.id),
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )