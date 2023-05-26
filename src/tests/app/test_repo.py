import unittest
from unittest.mock import MagicMock, patch
from uuid import UUID, uuid4

from app.repo import CompanyRepo, DepartmentRepo
from core.entities.company import CompanyEntity
from infra.tour.models.company import Company


class TestCompanyRepo(unittest.TestCase):
    def setUp(self):
        self.company_repo = CompanyRepo()

    def test_create(self):
        with patch(
            "core.validators.CnpjValidator.validate", return_value=True
        ):
            company_entity = CompanyEntity(
                street="Street",
                city="City",
                country="Country",
                cnpj="11111111111111",
                is_active=True,
                id="123456",
            )

        Company.from_entity = MagicMock(return_value=Company())

        Company.save = MagicMock()

        result = self.company_repo.create(company_entity)

        Company.from_entity.assert_called_once_with(company_entity)
        Company.save.assert_called_once()
        self.assertIsInstance(result, CompanyEntity)

    # def test_update(self):
    #     with patch(
    #         "core.validators.CnpjValidator.validate",
    #         return_value=True
    #     ):
    #         company_entity = CompanyEntity(
    #             street="Street",
    #             city="City",
    #             country="Country",
    #             cnpj="11111111111111",
    #             is_active=True,
    #             id="123456"
    #         )

    #     self.company_repo._get = MagicMock(return_value=[Company()])

    #     self.company_repo._save = MagicMock()

    #     with patch(
    #         "infra.tour.models.company.Company.objects.filter",
    #         return_value=[Company()]
    #     ):
    #         result = self.company_repo.update(company_entity)

    #     self.company_repo._get.assert_called_once_with(company_entity.id)
    #     self.company_repo._save.assert_called_once_with(Company())
    #     self.assertIsInstance(result, CompanyEntity)

    def test_detail(self):
        company_id = str(uuid4())

        self.company_repo._get = MagicMock(return_value=[Company()])

        result = self.company_repo.detail(company_id)

        self.company_repo._get.assert_called_once_with(company_id)
        self.assertIsInstance(result, CompanyEntity)

    def test_is_exist(self):
        cnpj = "123456789"

        filter_mock = MagicMock()
        filter_mock.is_exists = True

        with patch(
            "infra.tour.models.company.Company.objects.filter",
            return_value=filter_mock,
        ):
            result = self.company_repo.is_exist(cnpj)

        self.assertTrue(result)
