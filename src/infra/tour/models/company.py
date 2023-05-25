from django.db import models

from core.entities.company import CompanyEntity
from tour.models.base import Base


class Company(Base):
    cnpj = models.CharField(
        "CNPJ", max_length=14, unique=True, help_text="Numero do CNPJ"
    )
    street = models.CharField("Street", max_length=64, help_text="Logradouro,")
    city = models.CharField("City", max_length=64, help_text="Cidade")
    country = models.CharField("Country", max_length=32, help_text="Pais")

    class Meta:
        app_label = 'tour'

    @staticmethod
    def from_entity(company):
        return Company(
            cnpj=company.cnpj,
            street=company.street,
            city=company.city,
            country=company.country,
        )

    def to_entity(self):
        return CompanyEntity(
            id=str(self.id),
            cnpj=self.cnpj,
            street=self.street,
            city=self.city,
            country=self.country,
            is_active=self.is_active,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
