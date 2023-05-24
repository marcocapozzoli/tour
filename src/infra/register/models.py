# import uuid
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
# from core.entities.company import Company as CompanyEntity


# class Base(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     is_active =  models.BooleanField('Is active', default=True)
#     created_at = models.DateTimeField("Created at", auto_now_add=True)
#     updated_at = models.DateTimeField("Updated at", auto_now=True)
    
#     class Meta:
#         abstract = True

# class Company(Base):
#     cnpj = models.CharField('CNPJ', max_length=14, unique=True, help_text='Numero do CNPJ')
#     street = models.CharField('Street', max_length=64, help_text='Logradouro,')
#     city = models.CharField('City', max_length=64, help_text='Cidade')
#     country = models.CharField('Country', max_length=32, help_text='Pais')
    
#     @staticmethod
#     def from_entity(company: CompanyEntity):
#         return Company(
#             cnpj=company.cnpj,
#             street=company.street,
#             city=company.city,
#             country=company.country,
#         )
    
#     def to_entity(self):
#         return CompanyEntity(
#             id=str(self.id),
#             cnpj=self.cnpj,
#             street=self.street,
#             city=self.city,
#             country=self.country,
#             is_active=self.is_active,
#             created_at=self.created_at,
#             updated_at=self.updated_at,
#         )

# class Department(Base):
#     name = models.CharField('Name', max_length=14, help_text='Nome')
#     cost_center = models.CharField('Cost center', max_length=64, help_text='Centro de custo')
#     integration_code = models.CharField('Integration code', max_length=64, help_text='Código de integração')
#     company = models.ForeignKey('company', on_delete=models.CASCADE)

# class Employee(Base):
#     full_name = models.CharField('Full name', max_length=14, help_text='Nome completo')
#     email =  models.CharField('E-mail', max_length=14, help_text='Email')
#     phone =  models.CharField('Phone', max_length=14, help_text='Telefone')
#     birthday = models.DateField('Birthday', help_text='Data de aniversário')
#     entry_date =  models.DateField('Entry date', help_text='Data de ingresso')
#     departure_date =  models.DateField('Departure date', help_text='Data de desligamento')
#     city =  models.CharField('City', max_length=14, help_text='Cidade')
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     # company = models.ForeignKey(Company, on_delete=models.CASCADE)
