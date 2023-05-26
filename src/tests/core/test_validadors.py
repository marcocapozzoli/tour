import unittest

from core.validators import CnpjValidator, ValidatorFactory


class CnpjValidatorTest(unittest.TestCase):
    def setUp(self):
        self.validator = CnpjValidator()

    def test_validate_valid_cnpj(self):
        self.assertTrue(self.validator.validate("36.503.283/0001-31"))
        self.assertTrue(self.validator.validate("36503283000131"))

    def test_validate_invalid_cnpj(self):
        self.assertFalse(self.validator.validate("12.345.678/0001-91"))
        self.assertFalse(self.validator.validate("12345678000191"))
        self.assertFalse(self.validator.validate("12345678"))
        self.assertFalse(self.validator.validate("123456789012345"))

    def test_validate_empty_cnpj(self):
        self.assertFalse(self.validator.validate(""))

    def test_validate_invalid_format(self):
        self.assertFalse(self.validator.validate("12.345.678/0001-9a"))
        self.assertFalse(self.validator.validate("12345678a00190"))
        self.assertFalse(self.validator.validate("12-345-678/0001-90"))


class ValidatorFactoryTest(unittest.TestCase):
    def test_cnpj_validator_instance(self):
        validator = ValidatorFactory.cnpj()
        self.assertIsInstance(validator, CnpjValidator)
