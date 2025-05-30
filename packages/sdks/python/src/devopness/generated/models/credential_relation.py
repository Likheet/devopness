"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import (
    Optional,
    Required,
    TypedDict,
    Union,
)

from pydantic import Field, StrictBool, StrictInt, StrictStr

from .. import DevopnessBaseModel
from .provider_relation import ProviderRelation, ProviderRelationPlain
from .provider_type import ProviderType, ProviderTypePlain
from .user_relation import UserRelation, UserRelationPlain


class CredentialRelation(DevopnessBaseModel):
    """
    CredentialRelation

    Attributes:
        id (int): The unique ID of the credential
        name (str): The name of the credential
        provider (ProviderRelation):
        provider_type (ProviderType):
        provider_type_human_readable (str): The human readable version of the type of the credential
        active (bool): If this credential is active or not
        created_by_user (UserRelation):
        created_at (str, optional): The date and time when the record was created
        updated_at (str, optional): The date and time when the record was last updated
    """

    id: StrictInt = Field(description="The unique ID of the credential")
    name: StrictStr = Field(description="The name of the credential")
    provider: ProviderRelation
    provider_type: ProviderType
    provider_type_human_readable: StrictStr = Field(
        description="The human readable version of the type of the credential"
    )
    active: StrictBool = Field(description="If this credential is active or not")
    created_by_user: UserRelation
    created_at: Optional[StrictStr] = Field(
        default=None, description="The date and time when the record was created"
    )
    updated_at: Optional[StrictStr] = Field(
        default=None, description="The date and time when the record was last updated"
    )


class CredentialRelationPlain(TypedDict, total=False):
    """
    Plain version of CredentialRelation.
    """

    id: Required[int]
    name: Required[str]
    provider: Required[
        Union[
            ProviderRelation,
            ProviderRelationPlain,
        ]
    ]
    provider_type: Required[
        Union[
            ProviderType,
            ProviderTypePlain,
        ]
    ]
    provider_type_human_readable: Required[str]
    active: Required[bool]
    created_by_user: Required[
        Union[
            UserRelation,
            UserRelationPlain,
        ]
    ]
    created_at: Optional[str]
    updated_at: Optional[str]
