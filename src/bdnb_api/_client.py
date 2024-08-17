# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import BdnbAPIError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "BdnbAPI",
    "AsyncBdnbAPI",
    "Client",
    "AsyncClient",
]


class BdnbAPI(SyncAPIClient):
    autocompletion: resources.AutocompletionResource
    geocodage: resources.GeocodageResource
    stats: resources.StatsResource
    donnees: resources.DonneesResource
    metadonnees: resources.MetadonneesResource
    tuiles: resources.TuilesResource
    with_raw_response: BdnbAPIWithRawResponse
    with_streaming_response: BdnbAPIWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous bdnb-api client instance.

        This automatically infers the `api_key` argument from the `BDNB_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BDNB_API_KEY")
        if api_key is None:
            raise BdnbAPIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BDNB_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BDNB_API_BASE_URL")
        if base_url is None:
            base_url = f"https://api.bdnb.io/v1/bdnb/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.autocompletion = resources.AutocompletionResource(self)
        self.geocodage = resources.GeocodageResource(self)
        self.stats = resources.StatsResource(self)
        self.donnees = resources.DonneesResource(self)
        self.metadonnees = resources.MetadonneesResource(self)
        self.tuiles = resources.TuilesResource(self)
        self.with_raw_response = BdnbAPIWithRawResponse(self)
        self.with_streaming_response = BdnbAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-Gravitee-Api-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncBdnbAPI(AsyncAPIClient):
    autocompletion: resources.AsyncAutocompletionResource
    geocodage: resources.AsyncGeocodageResource
    stats: resources.AsyncStatsResource
    donnees: resources.AsyncDonneesResource
    metadonnees: resources.AsyncMetadonneesResource
    tuiles: resources.AsyncTuilesResource
    with_raw_response: AsyncBdnbAPIWithRawResponse
    with_streaming_response: AsyncBdnbAPIWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async bdnb-api client instance.

        This automatically infers the `api_key` argument from the `BDNB_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BDNB_API_KEY")
        if api_key is None:
            raise BdnbAPIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the BDNB_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BDNB_API_BASE_URL")
        if base_url is None:
            base_url = f"https://api.bdnb.io/v1/bdnb/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.autocompletion = resources.AsyncAutocompletionResource(self)
        self.geocodage = resources.AsyncGeocodageResource(self)
        self.stats = resources.AsyncStatsResource(self)
        self.donnees = resources.AsyncDonneesResource(self)
        self.metadonnees = resources.AsyncMetadonneesResource(self)
        self.tuiles = resources.AsyncTuilesResource(self)
        self.with_raw_response = AsyncBdnbAPIWithRawResponse(self)
        self.with_streaming_response = AsyncBdnbAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-Gravitee-Api-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class BdnbAPIWithRawResponse:
    def __init__(self, client: BdnbAPI) -> None:
        self.autocompletion = resources.AutocompletionResourceWithRawResponse(client.autocompletion)
        self.geocodage = resources.GeocodageResourceWithRawResponse(client.geocodage)
        self.stats = resources.StatsResourceWithRawResponse(client.stats)
        self.donnees = resources.DonneesResourceWithRawResponse(client.donnees)
        self.metadonnees = resources.MetadonneesResourceWithRawResponse(client.metadonnees)
        self.tuiles = resources.TuilesResourceWithRawResponse(client.tuiles)


class AsyncBdnbAPIWithRawResponse:
    def __init__(self, client: AsyncBdnbAPI) -> None:
        self.autocompletion = resources.AsyncAutocompletionResourceWithRawResponse(client.autocompletion)
        self.geocodage = resources.AsyncGeocodageResourceWithRawResponse(client.geocodage)
        self.stats = resources.AsyncStatsResourceWithRawResponse(client.stats)
        self.donnees = resources.AsyncDonneesResourceWithRawResponse(client.donnees)
        self.metadonnees = resources.AsyncMetadonneesResourceWithRawResponse(client.metadonnees)
        self.tuiles = resources.AsyncTuilesResourceWithRawResponse(client.tuiles)


class BdnbAPIWithStreamedResponse:
    def __init__(self, client: BdnbAPI) -> None:
        self.autocompletion = resources.AutocompletionResourceWithStreamingResponse(client.autocompletion)
        self.geocodage = resources.GeocodageResourceWithStreamingResponse(client.geocodage)
        self.stats = resources.StatsResourceWithStreamingResponse(client.stats)
        self.donnees = resources.DonneesResourceWithStreamingResponse(client.donnees)
        self.metadonnees = resources.MetadonneesResourceWithStreamingResponse(client.metadonnees)
        self.tuiles = resources.TuilesResourceWithStreamingResponse(client.tuiles)


class AsyncBdnbAPIWithStreamedResponse:
    def __init__(self, client: AsyncBdnbAPI) -> None:
        self.autocompletion = resources.AsyncAutocompletionResourceWithStreamingResponse(client.autocompletion)
        self.geocodage = resources.AsyncGeocodageResourceWithStreamingResponse(client.geocodage)
        self.stats = resources.AsyncStatsResourceWithStreamingResponse(client.stats)
        self.donnees = resources.AsyncDonneesResourceWithStreamingResponse(client.donnees)
        self.metadonnees = resources.AsyncMetadonneesResourceWithStreamingResponse(client.metadonnees)
        self.tuiles = resources.AsyncTuilesResourceWithStreamingResponse(client.tuiles)


Client = BdnbAPI

AsyncClient = AsyncBdnbAPI
