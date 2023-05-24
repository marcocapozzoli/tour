import re
from itertools import cycle


class CnpjValidator:
    def validate(self, data: str) -> bool:
    
        cnpj = re.sub(r'[^0-9]', '', data)

        if len(cnpj) != 14:
            return False

        if len(set(cnpj)) == 1:
            return False
        
        cnpj_r = cnpj[::-1]
        for i in range(2, 0, -1):
            cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
            dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
            if cnpj_r[i - 1:i] != str(dv % 10):
                return False

        return True


class EmailValidator:
    def validate(self, data: str) -> bool:
        return True


class PhoneValidator:
    def validate(self, data: str) -> bool:
        return True


class ValidatorFactory:
    
    @staticmethod
    def cnpj():
        return CnpjValidator()

    @staticmethod
    def email():
        return EmailValidator()

    @staticmethod
    def phone():
        return PhoneValidator()