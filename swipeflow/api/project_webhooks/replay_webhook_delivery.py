from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.webhook_delivery import WebhookDelivery
from ...types import Response


def _get_kwargs(
    project_id: str,
    webhook_id: str,
    delivery_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/webhooks/{webhook_id}/deliveries/{delivery_id}/replay".format(
            project_id=quote(str(project_id), safe=""),
            webhook_id=quote(str(webhook_id), safe=""),
            delivery_id=quote(str(delivery_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | WebhookDelivery | None:
    if response.status_code == 201:
        response_201 = WebhookDelivery.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

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
) -> Response[ErrorResponse | WebhookDelivery]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    webhook_id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | WebhookDelivery]:
    """Replay a delivery

     Re-queues the delivery as a new row (`replayOf` the original), leaving the original's own history
    untouched.

    Args:
        project_id (str):
        webhook_id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookDelivery]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        webhook_id=webhook_id,
        delivery_id=delivery_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    webhook_id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | WebhookDelivery | None:
    """Replay a delivery

     Re-queues the delivery as a new row (`replayOf` the original), leaving the original's own history
    untouched.

    Args:
        project_id (str):
        webhook_id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookDelivery
    """

    return sync_detailed(
        project_id=project_id,
        webhook_id=webhook_id,
        delivery_id=delivery_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    webhook_id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | WebhookDelivery]:
    """Replay a delivery

     Re-queues the delivery as a new row (`replayOf` the original), leaving the original's own history
    untouched.

    Args:
        project_id (str):
        webhook_id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookDelivery]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        webhook_id=webhook_id,
        delivery_id=delivery_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    webhook_id: str,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | WebhookDelivery | None:
    """Replay a delivery

     Re-queues the delivery as a new row (`replayOf` the original), leaving the original's own history
    untouched.

    Args:
        project_id (str):
        webhook_id (str):
        delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookDelivery
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            webhook_id=webhook_id,
            delivery_id=delivery_id,
            client=client,
        )
    ).parsed
