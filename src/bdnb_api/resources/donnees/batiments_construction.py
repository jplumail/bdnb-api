# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.donnees import batiments_construction_list_params
from ...types.donnees.batiments_construction_list_response import BatimentsConstructionListResponse

__all__ = ["BatimentsConstructionResource", "AsyncBatimentsConstructionResource"]


class BatimentsConstructionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentsConstructionResourceWithRawResponse:
        return BatimentsConstructionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentsConstructionResourceWithStreamingResponse:
        return BatimentsConstructionResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        altitude_sol: str | NotGiven = NOT_GIVEN,
        batiment_construction_id: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_commune_insee: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_iris: str | NotGiven = NOT_GIVEN,
        fictive_geom_cstr: str | NotGiven = NOT_GIVEN,
        geom_cstr: str | NotGiven = NOT_GIVEN,
        hauteur: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        rnb_id: str | NotGiven = NOT_GIVEN,
        s_geom_cstr: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentsConstructionListResponse:
        """
        Enceinte physique des diffÃ©rentes gÃ©omÃ©tries qui composent le groupe de
        bÃ¢timent ainsi que l'identifiant rnb.

        Args:
          altitude_sol: (ign) Altitude moynne au pied du bÃ¢timent physique [m]

          batiment_construction_id: Identifiant unique de l'entrÃ©e batiment_construction.

          batiment_groupe_id: (bdnb) ClÃ© d'IntÃ©ropÃ©rabilitÃ© du bÃ¢timent dans la BDNB

          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code dÃ©partement INSEE

          code_iris: Code iris INSEE

          fictive_geom_cstr: (ign) BoolÃ©en. Si 'True', la gÃ©omÃ©trie est fictive (et la surface au sol
              n'est pas rÃ©elle), sinon elle correspond Ã une emprise au sol rÃ©elle

          geom_cstr: (ign) GÃ©omÃ©trie multipolygonale de l'enceinte du bÃ¢timent (Lambert-93)

          hauteur: (ign) Hauteur du bÃ¢timent physique [m]

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          rnb_id: Identifiant unique de l'entrÃ©e RNB. Dans le cas d'un double rnb_id pour un
              mÃªme bÃ¢timent construction, celui appartenant au bÃ¢timent construction avec
              le plus d'emprise au sol est pris en compte.

          s_geom_cstr: (ign) Surface au sol de la gÃ©omÃ©trie de la construction [mÂ²]

          select: Filtering Columns

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/donnees/batiment_construction",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "altitude_sol": altitude_sol,
                        "batiment_construction_id": batiment_construction_id,
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_commune_insee": code_commune_insee,
                        "code_departement_insee": code_departement_insee,
                        "code_iris": code_iris,
                        "fictive_geom_cstr": fictive_geom_cstr,
                        "geom_cstr": geom_cstr,
                        "hauteur": hauteur,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "rnb_id": rnb_id,
                        "s_geom_cstr": s_geom_cstr,
                        "select": select,
                    },
                    batiments_construction_list_params.BatimentsConstructionListParams,
                ),
            ),
            cast_to=BatimentsConstructionListResponse,
        )


class AsyncBatimentsConstructionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentsConstructionResourceWithRawResponse:
        return AsyncBatimentsConstructionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentsConstructionResourceWithStreamingResponse:
        return AsyncBatimentsConstructionResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        altitude_sol: str | NotGiven = NOT_GIVEN,
        batiment_construction_id: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_commune_insee: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        code_iris: str | NotGiven = NOT_GIVEN,
        fictive_geom_cstr: str | NotGiven = NOT_GIVEN,
        geom_cstr: str | NotGiven = NOT_GIVEN,
        hauteur: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        rnb_id: str | NotGiven = NOT_GIVEN,
        s_geom_cstr: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentsConstructionListResponse:
        """
        Enceinte physique des diffÃ©rentes gÃ©omÃ©tries qui composent le groupe de
        bÃ¢timent ainsi que l'identifiant rnb.

        Args:
          altitude_sol: (ign) Altitude moynne au pied du bÃ¢timent physique [m]

          batiment_construction_id: Identifiant unique de l'entrÃ©e batiment_construction.

          batiment_groupe_id: (bdnb) ClÃ© d'IntÃ©ropÃ©rabilitÃ© du bÃ¢timent dans la BDNB

          code_commune_insee: Code INSEE de la commune

          code_departement_insee: Code dÃ©partement INSEE

          code_iris: Code iris INSEE

          fictive_geom_cstr: (ign) BoolÃ©en. Si 'True', la gÃ©omÃ©trie est fictive (et la surface au sol
              n'est pas rÃ©elle), sinon elle correspond Ã une emprise au sol rÃ©elle

          geom_cstr: (ign) GÃ©omÃ©trie multipolygonale de l'enceinte du bÃ¢timent (Lambert-93)

          hauteur: (ign) Hauteur du bÃ¢timent physique [m]

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          rnb_id: Identifiant unique de l'entrÃ©e RNB. Dans le cas d'un double rnb_id pour un
              mÃªme bÃ¢timent construction, celui appartenant au bÃ¢timent construction avec
              le plus d'emprise au sol est pris en compte.

          s_geom_cstr: (ign) Surface au sol de la gÃ©omÃ©trie de la construction [mÂ²]

          select: Filtering Columns

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Prefer": str(prefer) if is_given(prefer) else NOT_GIVEN,
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/donnees/batiment_construction",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "altitude_sol": altitude_sol,
                        "batiment_construction_id": batiment_construction_id,
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_commune_insee": code_commune_insee,
                        "code_departement_insee": code_departement_insee,
                        "code_iris": code_iris,
                        "fictive_geom_cstr": fictive_geom_cstr,
                        "geom_cstr": geom_cstr,
                        "hauteur": hauteur,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "rnb_id": rnb_id,
                        "s_geom_cstr": s_geom_cstr,
                        "select": select,
                    },
                    batiments_construction_list_params.BatimentsConstructionListParams,
                ),
            ),
            cast_to=BatimentsConstructionListResponse,
        )


class BatimentsConstructionResourceWithRawResponse:
    def __init__(self, batiments_construction: BatimentsConstructionResource) -> None:
        self._batiments_construction = batiments_construction

        self.list = to_raw_response_wrapper(
            batiments_construction.list,
        )


class AsyncBatimentsConstructionResourceWithRawResponse:
    def __init__(self, batiments_construction: AsyncBatimentsConstructionResource) -> None:
        self._batiments_construction = batiments_construction

        self.list = async_to_raw_response_wrapper(
            batiments_construction.list,
        )


class BatimentsConstructionResourceWithStreamingResponse:
    def __init__(self, batiments_construction: BatimentsConstructionResource) -> None:
        self._batiments_construction = batiments_construction

        self.list = to_streamed_response_wrapper(
            batiments_construction.list,
        )


class AsyncBatimentsConstructionResourceWithStreamingResponse:
    def __init__(self, batiments_construction: AsyncBatimentsConstructionResource) -> None:
        self._batiments_construction = batiments_construction

        self.list = async_to_streamed_response_wrapper(
            batiments_construction.list,
        )
