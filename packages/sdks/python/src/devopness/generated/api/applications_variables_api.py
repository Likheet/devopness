"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import List, Optional, Union

from .. import DevopnessBaseService, DevopnessBaseServiceAsync, DevopnessResponse
from ..models import (
    Variable,
    VariableApplicationCreate,
    VariableApplicationCreatePlain,
    VariableRelation,
)
from ..utils import parse_query_string


class ApplicationsVariablesApiService(DevopnessBaseService):
    """
    ApplicationsVariablesApiService - Auto Generated
    """

    def add_application_variable(
        self,
        application_id: int,
        variable_application_create: Union[
            VariableApplicationCreate,
            VariableApplicationCreatePlain,
        ],
    ) -> DevopnessResponse[Variable]:
        """
        Create a new variable linked to an application

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/applications/{application_id}/variables",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = self._post(endpoint, variable_application_create)

        return DevopnessResponse(response, Variable)

    def list_application_variables(
        self,
        application_id: int,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
    ) -> DevopnessResponse[List[VariableRelation]]:
        """
        Return a list of variables belonging to an application

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        query_string = parse_query_string(
            {
                "page": page,
                "per_page": per_page,
            }
        )

        endpoint_parts = [
            f"/applications/{application_id}/variables",
            f"?{query_string}",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = self._get(endpoint)

        return DevopnessResponse(response, List[VariableRelation])


class ApplicationsVariablesApiServiceAsync(DevopnessBaseServiceAsync):
    """
    ApplicationsVariablesApiServiceAsync - Auto Generated
    """

    async def add_application_variable(
        self,
        application_id: int,
        variable_application_create: Union[
            VariableApplicationCreate,
            VariableApplicationCreatePlain,
        ],
    ) -> DevopnessResponse[Variable]:
        """
        Create a new variable linked to an application

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/applications/{application_id}/variables",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = await self._post(endpoint, variable_application_create)

        return DevopnessResponse(response, Variable)

    async def list_application_variables(
        self,
        application_id: int,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
    ) -> DevopnessResponse[List[VariableRelation]]:
        """
        Return a list of variables belonging to an application

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        query_string = parse_query_string(
            {
                "page": page,
                "per_page": per_page,
            }
        )

        endpoint_parts = [
            f"/applications/{application_id}/variables",
            f"?{query_string}",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = await self._get(endpoint)

        return DevopnessResponse(response, List[VariableRelation])
