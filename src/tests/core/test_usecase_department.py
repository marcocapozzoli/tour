import unittest
from unittest.mock import MagicMock
from uuid import UUID, uuid4

from core.entities.department import DepartmentEntity
from core.exceptions import (
    EntityAlreadyExistsException,
    EntityDoesNotExistsException,
    EntityUpdateException,
)
from core.interfaces.repo import IDepartmentRepo
from core.usecases.department import DepartmentUseCases


class MockDepartmentRepo(IDepartmentRepo):
    def create(self, department: DepartmentEntity) -> DepartmentEntity:
        return department

    def update(self, department: DepartmentEntity) -> DepartmentEntity:
        return department

    def detail(self, department_id: UUID) -> DepartmentEntity:
        return DepartmentEntity(
            name="Department",
            cost_center="Cost Center",
            integration_code="Integration Code",
            company="Company",
            id=str(department_id),
            is_active=True,
        )

    def is_exist(self, name: str, company: str) -> bool:
        return False


class DepartmentUseCasesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.department_repo = MockDepartmentRepo()
        self.use_cases = DepartmentUseCases(
            department_repo=self.department_repo
        )

    def test_create(self):
        params = {
            "name": "Department",
            "company": "Company",
            "id": "123",
            "cost_center": "A0001",
            "integration_code": "0001",
        }

        result = self.use_cases.create(params)

        self.assertIsInstance(result, DepartmentEntity)
        self.assertEqual(result.name, "Department")
        self.assertEqual(result.company, "Company")
        self.assertEqual(result.id, "123")

    def test_create_already_exists(self):
        self.department_repo.is_exist = MagicMock(return_value=True)

        params = {
            "name": "Department",
            "company": "Company",
            "id": "123",
            "cost_center": "A0001",
            "integration_code": "0001",
        }

        with self.assertRaises(EntityAlreadyExistsException) as e:
            self.use_cases.create(params)

        exception = e.exception
        self.assertEqual(exception.code, "CDUC")
        self.assertEqual(exception.message, "Erro registro do departamento")
        self.assertEqual(
            exception.details,
            "Já existe um departamento com esse nome cadastrado para essa empresa",
        )

    def test_update(self):
        params = {
            "name": "Updated Department",
            "company": "Company",
            "id": "123",
            "cost_center": "A0001",
            "integration_code": "0001",
        }

        result = self.use_cases.update(params)

        self.assertIsInstance(result, DepartmentEntity)
        self.assertEqual(result.name, "Updated Department")
        self.assertEqual(result.company, "Company")
        self.assertEqual(result.id, "123")

    def test_update_exception(self):
        self.department_repo.update = MagicMock(
            side_effect=Exception("Update error")
        )

        params = {
            "name": "Updated Department",
            "company": "Company",
            "id": "123",
            "cost_center": "A0001",
            "integration_code": "0001",
        }

        with self.assertRaises(EntityUpdateException) as e:
            self.use_cases.update(params)

        exception = e.exception
        self.assertEqual(exception.code, "UDUC")
        self.assertEqual(exception.message, "Erro na atualização da empresa")
        self.assertEqual(exception.details, "Update error")

    def test_detail(self):
        department_id = str(uuid4())

        result = self.use_cases.detail(department_id)

        self.assertIsInstance(result, DepartmentEntity)
        self.assertEqual(result.name, "Department")
        self.assertEqual(result.company, "Company")
        self.assertEqual(result.cost_center, "Cost Center")
        self.assertEqual(result.integration_code, "Integration Code")
        self.assertEqual(result.id, str(department_id))

    def test_detail_exception(self):
        self.department_repo.detail = MagicMock(
            side_effect=Exception("Detail error")
        )

        department_id = str(uuid4())

        with self.assertRaises(EntityDoesNotExistsException) as e:
            self.use_cases.detail(department_id)

        exception = e.exception
        self.assertEqual(exception.code, "DDUC")
        self.assertEqual(
            exception.message, "Erro ao obter detalhes do departamento"
        )
        self.assertEqual(
            exception.details,
            f"Não existe departamento cadastrado com esse id `{department_id}`",
        )
