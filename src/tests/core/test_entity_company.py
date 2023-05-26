from datetime import datetime
from unittest import TestCase

from core.entities.company import CompanyEntity


class CompanyEntityTestCase(TestCase):
    def test_validate_valid_cnpj(self):
        entity = CompanyEntity(
            street="Street",
            city="City",
            country="Country",
            cnpj="48102383000135",
            is_active=True,
            id="123",
            updated_at=datetime.now(),
            created_at=datetime.now(),
        )

        self.assertIsNone(entity.validate())

    # @mock.patch("core.validators.ValidatorFactory")
    # def test_validate_invalid_cnpj(self, mock_validator):

    #     validator = mock_validator.cnpj.return_value
    #     validator.validate.return_value = False

    #     entity = CompanyEntity(
    #         street="Street",
    #         city="City",
    #         country="Country",
    #         cnpj="11111111111111",
    #         is_active=True,
    #         id="123",
    #         updated_at=datetime.now(),
    #         created_at=datetime.now()
    #     )

    #     try:
    #         entity.validate()
    #     except EntityValidationException as e:
    #         self.assertEqual(e.code, "EV")
    #         self.assertEqual(e.message, "Esse Cnpj é inválido")
    #         self.assertEqual(e.details, "11111111111111")
    #     else:
    #         self.fail("EntityValidationException not raised")
