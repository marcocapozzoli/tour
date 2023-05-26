import unittest
from unittest.mock import MagicMock, patch
from uuid import UUID, uuid4

from core.entities.company import CompanyEntity
from core.exceptions import (
    EntityAlreadyExistsException,
    EntityDoesNotExistsException,
    EntityUpdateException,
)
from core.interfaces.repo import ICompanyRepo
from core.usecases.company import CompanyUseCases


class MockCompanyRepo(ICompanyRepo):
    def create(self, company: CompanyEntity) -> CompanyEntity:
        return company

    def update(self, company: CompanyEntity) -> CompanyEntity:
        return company

    def detail(self, company_id: UUID) -> CompanyEntity:
        return CompanyEntity(
            street="Street",
            city="City",
            country="Country",
            cnpj="11111111111111",
            is_active=True,
            id=str(company_id),
        )

    def is_exist(self, cnpj: str) -> bool:
        return False


class CompanyUseCasesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.company_repo = MockCompanyRepo()
        self.use_cases = CompanyUseCases(company_repo=self.company_repo)

    def test_create(self):
        params = {
            "street": "Street",
            "city": "City",
            "country": "Country",
            "cnpj": "11111111111111",
            "is_active": True,
            "id": "123",
        }

        with patch(
            "core.validators.CnpjValidator.validate", return_value=True
        ):
            result = self.use_cases.create(params)

        self.assertIsInstance(result, CompanyEntity)
        self.assertEqual(result.street, "Street")
        self.assertEqual(result.city, "City")
        self.assertEqual(result.country, "Country")
        self.assertEqual(result.cnpj, "11111111111111")
        self.assertEqual(result.is_active, True)
        self.assertEqual(result.id, "123")

    def test_create_already_exists(self):
        self.company_repo.is_exist = MagicMock(return_value=True)

        params = {
            "street": "Street",
            "city": "City",
            "country": "Country",
            "cnpj": "11111111111111",
            "is_active": True,
            "id": "123",
        }

        with patch(
            "core.validators.CnpjValidator.validate", return_value=True
        ):
            with self.assertRaises(EntityAlreadyExistsException) as e:
                self.use_cases.create(params)

        exception = e.exception
        self.assertEqual(exception.code, "CCUC")
        self.assertEqual(exception.message, "Erro registro da empresa")
        self.assertEqual(
            exception.details,
            'Já existe uma empresa cadastrada com esse cnpj `11111111111111`',
        )

    def test_update(self):
        params = {
            "street": "Updated Street",
            "city": "Updated City",
            "country": "Updated Country",
            "cnpj": "11111111111111",
            "is_active": True,
            "id": "123",
        }

        with patch(
            "core.validators.CnpjValidator.validate", return_value=True
        ):
            result = self.use_cases.update(params)

        self.assertIsInstance(result, CompanyEntity)
        self.assertEqual(result.street, "Updated Street")
        self.assertEqual(result.city, "Updated City")
        self.assertEqual(result.country, "Updated Country")
        self.assertEqual(result.cnpj, "11111111111111")
        self.assertEqual(result.is_active, True)
        self.assertEqual(result.id, "123")

    def test_update_exception(self):
        self.company_repo.update = MagicMock(
            side_effect=Exception("Update error")
        )

        params = {
            "street": "Updated Street",
            "city": "Updated City",
            "country": "Updated Country",
            "cnpj": "11111111111111",
            "is_active": True,
            "id": "123",
        }
        with patch(
            "core.validators.CnpjValidator.validate", return_value=True
        ):
            with self.assertRaises(EntityUpdateException) as e:
                self.use_cases.update(params)

        exception = e.exception
        self.assertEqual(exception.code, "UCUC")
        self.assertEqual(exception.message, "Erro na atualização da empresa")
        self.assertEqual(exception.details, "Update error")

    def test_detail(self):
        company_id = str(uuid4())

        with patch(
            "core.validators.CnpjValidator.validate", return_value=True
        ):
            result = self.use_cases.detail(company_id)

        self.assertIsInstance(result, CompanyEntity)
        self.assertEqual(result.street, "Street")
        self.assertEqual(result.city, "City")
        self.assertEqual(result.country, "Country")
        self.assertEqual(result.cnpj, "11111111111111")
        self.assertEqual(result.is_active, True)
        self.assertEqual(result.id, company_id)

    def test_detail_exception(self):
        self.company_repo.detail = MagicMock(
            side_effect=Exception("Detail error")
        )

        company_id = str(uuid4())

        with self.assertRaises(EntityDoesNotExistsException) as e:
            self.use_cases.detail(company_id)

        exception = e.exception
        self.assertEqual(exception.code, "DCUC")
        self.assertEqual(
            exception.message, "Erro ao obter detalhes da empresa"
        )
        self.assertEqual(
            exception.details,
            f"Não existe empresa cadastrada com esse id `{company_id}`",
        )
