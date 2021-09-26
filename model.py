"""
Include API Models
"""
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from dataclass_type_validator import dataclass_type_validator


@dataclass_json
@dataclass
class UserRequest:
    """
    Model to request including userId
    """
    idUser: int

    def __post_init__(self):
        """Execute type validator after class initialization
        """
        dataclass_type_validator(self)


@dataclass_json
@dataclass
class Response:
    """
    Model to response including a list of data
    """
    message: str
    data: list
    total: int


@dataclass_json
@dataclass
class Error:
    """
    Model to error response
    """
    message: str
    detail: str