from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.webhook_test import WebhookTest
from ...types import Response


def _get_kwargs(
    project_id: str,
    webhook_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/webhooks/{webhook_id}/test".format(
            project_id=quote(str(project_id), safe=""),
            webhook_id=quote(str(webhook_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | WebhookTest | None:
    if response.status_code == 202:
        response_202 = WebhookTest.from_dict(response.json())

        return response_202

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
) -> Response[ErrorResponse | WebhookTest]:
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
) -> Response[ErrorResponse | WebhookTest]:
    """Test webhook

     Queues one signed `test` request to the webhook's URL. It is sent once, without retries, and doesn't
    affect the webhook's health or suspension. Poll the returned test for the result; it also appears in
    the webhook's logs.

    Args:
        project_id (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookTest]
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
) -> ErrorResponse | WebhookTest | None:
    """Test webhook

     Queues one signed `test` request to the webhook's URL. It is sent once, without retries, and doesn't
    affect the webhook's health or suspension. Poll the returned test for the result; it also appears in
    the webhook's logs.

    Args:
        project_id (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookTest
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
) -> Response[ErrorResponse | WebhookTest]:
    """Test webhook

     Queues one signed `test` request to the webhook's URL. It is sent once, without retries, and doesn't
    affect the webhook's health or suspension. Poll the returned test for the result; it also appears in
    the webhook's logs.

    Args:
        project_id (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | WebhookTest]
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
) -> ErrorResponse | WebhookTest | None:
    """Test webhook

     Queues one signed `test` request to the webhook's URL. It is sent once, without retries, and doesn't
    affect the webhook's health or suspension. Poll the returned test for the result; it also appears in
    the webhook's logs.

    Args:
        project_id (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | WebhookTest
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            webhook_id=webhook_id,
            client=client,
        )
    ).parsed
