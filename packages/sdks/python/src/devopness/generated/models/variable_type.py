"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

import json
from enum import Enum
from typing import Literal, Self


class VariableType(str, Enum):
    """
    The type of the key/value pair
    """

    FILE = "file"
    VARIABLE = "variable"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VariableType from a JSON string"""
        return cls(json.loads(json_str))


# The plain version of VariableType
VariableTypePlain = Literal[
    "file",
    "variable",
]
