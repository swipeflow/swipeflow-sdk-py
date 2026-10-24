from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.webhook_cursor import WebhookCursor
from ...types import Response


def _get_kwargs(
    project_id: str,
    webhook_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/webhooks/{webhook_id}/cursor".format(
            project_id=quote(str(project_id), safe=""),
            webhook_id=quote(str(webhook_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | WebhookCursor | None:
    if response.status_code == 200:
        response_200 = WebhookCursor.from_dict(response.json())

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
) -> Response[ErrorResponse | WebhookCursor]:
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
) -> Response[ErrorResponse | WebhookCursor]:
    """Get the webhook's reconciliation cursor

     The event-id watermark a receiver can persist and resume from — everything at or before it is
    settled for this webhook.

    Args:
        project_id (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookCursor]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        webhook_id=webhook_id,
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
) -> ErrorResponse | WebhookCursor | None:
    """Get the webhook's reconciliation cursor

     The event-id watermark a receiver can persist and resume from — everything at or before it is
    settled for this webhook.

    Args:
        project_id (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookCursor
    """

    return sync_detailed(
        project_id=project_id,
        webhook_id=webhook_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | WebhookCursor]:
    """Get the webhook's reconciliation cursor

     The event-id watermark a receiver can persist and resume from — everything at or before it is
    settled for this webhook.

    Args:
        project_id (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookCursor]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        webhook_id=webhook_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | WebhookCursor | None:
    """Get the webhook's reconciliation cursor

     The event-id watermark a receiver can persist and resume from — everything at or before it is
    settled for this webhook.

    Args:
        project_id (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookCursor
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            webhook_id=webhook_id,
            client=client,
        )
    ).parsed
