class BaseException(Exception):
    """
    Base class to exceptions
    """

    def __init__(
        self,
        code: int,
        message: str,
        details: str = ""
    ):
        self.code = code
        self.message = message
        self.details = details

        super().__init__(self.details)

    def to_dict(self):
        return {
            'code': self.code,
            'message': self.message,
            'details': self.details,
        }


class EntityAlreadyExistsException(BaseException):
    ...

class EntityValidationException(BaseException):
    ...

class EntityDoesNotExistsException(BaseException):
    ...
    
class EntityUpdateException(BaseException):
    ...