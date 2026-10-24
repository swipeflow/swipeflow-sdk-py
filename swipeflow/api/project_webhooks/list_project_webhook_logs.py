from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_project_webhook_logs_status import ListProjectWebhookLogsStatus
from ...models.webhook_log_page import WebhookLogPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    status: ListProjectWebhookLogsStatus | Unset = UNSET,
    event_type: str | Unset = UNSET,
    delivery_id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["eventType"] = event_type

    params["deliveryId"] = delivery_id

    params["search"] = search

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/webhook-logs".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | WebhookLogPage | None:
    if response.status_code == 200:
        response_200 = WebhookLogPage.from_dict(response.json())

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
) -> Response[ErrorResponse | WebhookLogPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    status: ListProjectWebhookLogsStatus | Unset = UNSET,
    event_type: str | Unset = UNSET,
    delivery_id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorResponse | WebhookLogPage]:
    """Get project webhook logs

     Paginated webhook delivery logs across the project, newest-first.

    Args:
        project_id (str):
        status (ListProjectWebhookLogsStatus | Unset):
        event_type (str | Unset):
        delivery_id (str | Unset):
        search (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookLogPage]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        status=status,
        event_type=event_type,
        delivery_id=delivery_id,
        search=search,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    status: ListProjectWebhookLogsStatus | Unset = UNSET,
    event_type: str | Unset = UNSET,
    delivery_id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorResponse | WebhookLogPage | None:
    """Get project webhook logs

     Paginated webhook delivery logs across the project, newest-first.

    Args:
        project_id (str):
        status (ListProjectWebhookLogsStatus | Unset):
        event_type (str | Unset):
        delivery_id (str | Unset):
        search (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookLogPage
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        status=status,
        event_type=event_type,
        delivery_id=delivery_id,
        search=search,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    status: ListProjectWebhookLogsStatus | Unset = UNSET,
    event_type: str | Unset = UNSET,
    delivery_id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[ErrorResponse | WebhookLogPage]:
    """Get project webhook logs

     Paginated webhook delivery logs across the project, newest-first.

    Args:
        project_id (str):
        status (ListProjectWebhookLogsStatus | Unset):
        event_type (str | Unset):
        delivery_id (str | Unset):
        search (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookLogPage]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        status=status,
        event_type=event_type,
        delivery_id=delivery_id,
        search=search,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    status: ListProjectWebhookLogsStatus | Unset = UNSET,
    event_type: str | Unset = UNSET,
    delivery_id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> ErrorResponse | WebhookLogPage | None:
    """Get project webhook logs

     Paginated webhook delivery logs across the project, newest-first.

    Args:
        project_id (str):
        status (ListProjectWebhookLogsStatus | Unset):
        event_type (str | Unset):
        delivery_id (str | Unset):
        search (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookLogPage
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            status=status,
            event_type=event_type,
            delivery_id=delivery_id,
            search=search,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
