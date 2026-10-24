from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.webhook_delivery_page import WebhookDeliveryPage
from ...models.webhook_delivery_status import WebhookDeliveryStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    webhook_id: str,
    *,
    status: list[WebhookDeliveryStatus] | Unset = UNSET,
    event_type: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    params["eventType"] = event_type

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/webhooks/{webhook_id}/deliveries".format(
            project_id=quote(str(project_id), safe=""),
            webhook_id=quote(str(webhook_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | WebhookDeliveryPage | None:
    if response.status_code == 200:
        response_200 = WebhookDeliveryPage.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | WebhookDeliveryPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient,
    status: list[WebhookDeliveryStatus] | Unset = UNSET,
    event_type: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorResponse | WebhookDeliveryPage]:
    """List a webhook's deliveries

     Paginated delivery history, newest-first.

    Args:
        project_id (str):
        webhook_id (str):
        status (list[WebhookDeliveryStatus] | Unset):
        event_type (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookDeliveryPage]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        webhook_id=webhook_id,
        status=status,
        event_type=event_type,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient,
    status: list[WebhookDeliveryStatus] | Unset = UNSET,
    event_type: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorResponse | WebhookDeliveryPage | None:
    """List a webhook's deliveries

     Paginated delivery history, newest-first.

    Args:
        project_id (str):
        webhook_id (str):
        status (list[WebhookDeliveryStatus] | Unset):
        event_type (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookDeliveryPage
    """

    return sync_detailed(
        project_id=project_id,
        webhook_id=webhook_id,
        client=client,
        status=status,
        event_type=event_type,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient,
    status: list[WebhookDeliveryStatus] | Unset = UNSET,
    event_type: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorResponse | WebhookDeliveryPage]:
    """List a webhook's deliveries

     Paginated delivery history, newest-first.

    Args:
        project_id (str):
        webhook_id (str):
        status (list[WebhookDeliveryStatus] | Unset):
        event_type (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookDeliveryPage]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        webhook_id=webhook_id,
        status=status,
        event_type=event_type,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient,
    status: list[WebhookDeliveryStatus] | Unset = UNSET,
    event_type: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorResponse | WebhookDeliveryPage | None:
    """List a webhook's deliveries

     Paginated delivery history, newest-first.

    Args:
        project_id (str):
        webhook_id (str):
        status (list[WebhookDeliveryStatus] | Unset):
        event_type (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookDeliveryPage
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            webhook_id=webhook_id,
            client=client,
            status=status,
            event_type=event_type,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
