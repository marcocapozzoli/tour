import unittest
from datetime import datetime
from unittest.mock import MagicMock
from uuid import UUID, uuid4

from core.entities.employee import EmployeeEntity
from core.exceptions import (
    EntityAlreadyExistsException,
    EntityDoesNotExistsException,
    EntityUpdateException,
)
from core.interfaces.repo import IEmployeeRepo
from core.usecases.employee import EmployeeUseCases


class MockEmployeeRepo(IEmployeeRepo):
    def create(self, employee: EmployeeEntity) -> EmployeeEntity:
        return employee

    def update(self, employee: EmployeeEntity) -> EmployeeEntity:
        return employee

    def detail(self, employee_id: UUID) -> EmployeeEntity:
        return EmployeeEntity(
            full_name="John Doe",
            email="johndoe@example.com",
            phone="11999999999",
            birthday=datetime.now(),
            entry_date=datetime.now(),
            departure_date=datetime.now(),
            department="HR",
            city="City",
            id=str(employee_id),
            is_active=True,
        )

    def is_exist(self, email: str, department: str) -> bool:
        return False


class EmployeeUseCasesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.employee_repo = MockEmployeeRepo()
        self.use_cases = EmployeeUseCases(employee_repo=self.employee_repo)

    def test_create(self):
        params = {
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "phone": "11999999999",
            "birthday": "11/06/1990",
            "entry_date": "10/10/2020",
            "departure_date": "10/12/2022",
            "department": "HR",
            "city": "City",
        }

        result = self.use_cases.create(params)

        self.assertIsInstance(result, EmployeeEntity)
        self.assertEqual(result.full_name, "John Doe")
        self.assertEqual(result.email, "johndoe@example.com")
        self.assertEqual(result.department, "HR")

    def test_create_already_exists(self):
        self.employee_repo.is_exist = MagicMock(return_value=True)

        params = {
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "phone": "11999999999",
            "birthday": "11/06/1990",
            "entry_date": "10/10/2020",
            "departure_date": "10/12/2022",
            "department": "HR",
            "city": "City",
        }

        with self.assertRaises(EntityAlreadyExistsException) as e:
            self.use_cases.create(params)

        exception = e.exception
        self.assertEqual(exception.code, "CDUC")
        self.assertEqual(exception.message, "Erro no cadastro do funcionário")
        self.assertEqual(
            exception.details,
            "Já existe um funcionário cadatrado com esse email nesse departamento",
        )

    def test_update(self):
        params = {
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "phone": "11999999999",
            "birthday": "11/06/1990",
            "entry_date": "10/10/2020",
            "departure_date": "10/12/2022",
            "department": "Update HR",
            "city": "City",
        }
        result = self.use_cases.update(params)

        self.assertIsInstance(result, EmployeeEntity)
        self.assertEqual(result.full_name, "John Doe")
        self.assertEqual(result.email, "johndoe@example.com")
        self.assertEqual(result.department, "Update HR")

    def test_update_exception(self):
        self.employee_repo.update = MagicMock(
            side_effect=Exception("Update error")
        )

        params = {
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "phone": "11999999999",
            "birthday": "11/06/1990",
            "entry_date": "10/10/2020",
            "departure_date": "10/12/2022",
            "department": "Update HR",
            "city": "City",
        }

        with self.assertRaises(EntityUpdateException) as e:
            self.use_cases.update(params)

        exception = e.exception
        self.assertEqual(exception.code, "UDUC")
        self.assertEqual(
            exception.message, "Erro na atualização do funcionário"
        )
        self.assertEqual(exception.details, "Update error")

    def test_detail(self):
        employee_id = str(uuid4())

        result = self.use_cases.detail(employee_id)

        self.assertIsInstance(result, EmployeeEntity)
        self.assertEqual(result.full_name, "John Doe")
        self.assertEqual(result.email, "johndoe@example.com")
        self.assertEqual(result.department, "HR")
        self.assertEqual(result.id, str(employee_id))

    def test_detail_exception(self):
        self.employee_repo.detail = MagicMock(
            side_effect=Exception("Detail error")
        )

        employee_id = str(uuid4())

        with self.assertRaises(EntityDoesNotExistsException) as e:
            self.use_cases.detail(employee_id)

        exception = e.exception
        self.assertEqual(exception.code, "DDUC")
        self.assertEqual(
            exception.message, "Erro ao obter detalhes do funcionário"
        )
        self.assertEqual(
            exception.details,
            f"Não existe funcionário cadastrado com esse id `{employee_id}`",
        )
