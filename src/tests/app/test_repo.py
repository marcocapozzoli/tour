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


# +====================


class DepartmentRepoTests(unittest.TestCase):
    def setUp(self):
        self.department_repo = DepartmentRepo()

    # def test_create(self):

    #     department_entity = DepartmentEntity(
    #         name="Test Department",
    #         cost_center="123",
    #         integration_code="456",
    #         company="company_id"
    #     )
    #     mock_department = MagicMock(spec=Department)
    #     mock_department.to_entity.return_value = department_entity
    #     mock_department.save.return_value = None
    #     self.department_repo._get_company = MagicMock(return_value=MagicMock(spec=Company))
    #     self.department_repo._save = MagicMock()

    #     result = self.department_repo.create(department_entity)

    #     self.assertEqual(result, department_entity)
    #     self.department_repo._get_company.assert_called_once_with("company_id")
    #     self.department_repo._save.assert_called_once_with(mock_department)
    #     mock_department.save.assert_called_once()

    # def test_update(self):
    #     # Arrange
    #     department_entity = DepartmentEntity(
    #         id="department_id",
    #         name="Test Department",
    #         cost_center="123",
    #         integration_code="456",
    #         company="company_id"
    #     )
    #     filtered_data = {
    #         "name": "Updated Department",
    #         "cost_center": "789",
    #         "integration_code": "012",
    #         "company": "updated_company_id"
    #     }
    #     mock_department = MagicMock(spec=Department)
    #     mock_department.to_entity.return_value = department_entity
    #     self.department_repo._get = MagicMock(return_value=QuerySet([mock_department]))
    #     self.department_repo._get_company = MagicMock(return_value=MagicMock(spec=Company))
    #     mock_department.update = MagicMock()

    #     # Act
    #     result = self.department_repo.update(department_entity)

    #     # Assert
    #     self.assertEqual(result, department_entity)
    #     self.department_repo._get.assert_called_once_with("department_id")
    #     self.department_repo._get_company.assert_called_once_with("updated_company_id")
    #     mock_department.update.assert_called_once_with(**filtered_data)

    # def test_detail(self):
    #     # Arrange
    #     department_entity = DepartmentEntity(
    #         id="department_id",
    #         name="Test Department",
    #         cost_center="123",
    #         integration_code="456",
    #         company="company_id"
    #     )
    #     mock_department = MagicMock(spec=Department)
    #     mock_department.to_entity.return_value = department_entity
    #     self.department_repo._get = MagicMock(return_value=QuerySet([mock_department]))

    #     # Act
    #     result = self.department_repo.detail("department_id")

    #     # Assert
    #     self.assertEqual(result, department_entity)
    #     self.department_repo._get.assert_called_once_with("department_id")

    # def test_is_exist_when_department_exists(self):
    #     # Arrange
    #     department_name = "Test Department"
    #     company_id = "company_id"
    #     mock_department = MagicMock(spec=Department)
    #     self.department_repo._get_company = MagicMock(return_value=MagicMock(spec=Company))
    #     self.department_repo.manager.filter.return_value.exists.return_value = True

    #     # Act
    #     result = self.department_repo.is_exist(department_name, company_id)

    #     # Assert
    #     self.assertTrue(result)
    #     self.department_repo._get_company.assert_called_once_with(company_id)
    #     self.department_repo.manager.filter.assert_called_once_with(name=department_name, company=company_id)
    #     self.department_repo.manager.filter.return_value.exists.assert_called_once()

    # def test_is_exist_when_department_does_not_exist(self):
    #     # Arrange
    #     department_name = "Test Department"
    #     company_id = "company_id"
    #     self.department_repo._get_company = MagicMock(return_value=MagicMock(spec=Company))
    #     self.department_repo.manager.filter.return_value.exists.return_value = False

    #     # Act
    #     result = self.department_repo.is_exist(department_name, company_id)

    #     # Assert
    #     self.assertFalse(result)
    #     self.department_repo._get_company.assert_called_once_with(company_id)
    #     self.department_repo.manager.filter.assert_called_once_with(name=department_name, company=company_id)
    #     self.department_repo.manager.filter.return_value.exists.assert_called_once()

    # def test_save(self):
    #     # Arrange
    #     instance = MagicMock()

    #     # Act
    #     self.department_repo._save(instance)

    #     # Assert
    #     instance.save.assert_called_once()

    # def test_save_raises_exception(self):
    #     # Arrange
    #     instance = MagicMock()
    #     instance.save.side_effect = Exception("Save failed")

    #     # Act & Assert
    #     with self.assertRaises(Exception):
    #         self.department_repo._save(instance)

    # def test_get(self):
    #     # Arrange
    #     department_id = "department_id"
    #     mock_department = MagicMock(spec=Department)
    #     self.department_repo.manager.filter.return_value = QuerySet([mock_department])

    #     # Act
    #     result = self.department_repo._get(department_id)

    #     # Assert
    #     self.assertEqual(result, QuerySet([mock_department]))
    #     self.department_repo.manager.filter.assert_called_once_with(id=department_id)

    # def test_get_raises_exception(self):
    #     # Arrange
    #     department_id = "department_id"
    #     self.department_repo.manager.filter.side_effect = Exception("Get failed")

    #     # Act & Assert
    #     with self.assertRaises(Exception):
    #         self.department_repo._get(department_id)

    # def test_get_company(self):
    #     # Arrange
    #     company_id = "company_id"
    #     mock_company = MagicMock(spec=Company)
    #     self.department_repo.company_manager.get.return_value = mock_company

    #     # Act
    #     result = self.department_repo._get_company(company_id)

    #     # Assert
    #     self.assertEqual(result, mock_company)
    #     self.department_repo.company_manager.get.assert_called_once_with(id=company_id)

    # def test_get_company_raises_exception(self):
    #     # Arrange
    #     company_id = "company_id"
    #     self.department_repo.company_manager.get.side_effect = ObjectDoesNotExist("Company does not exist")

    #     # Act & Assert
    #     with self.assertRaises(ObjectDoesNotExist):
    #         self.department_repo._get_company(company_id)
