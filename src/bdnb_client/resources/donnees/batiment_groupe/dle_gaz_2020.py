# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.donnees.batiment_groupe import dle_gaz_2020_list_params
from ....types.donnees.batiment_groupe.dle_gaz_2020_list_response import DleGaz2020ListResponse

__all__ = ["DleGaz2020Resource", "AsyncDleGaz2020Resource"]


class DleGaz2020Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DleGaz2020ResourceWithRawResponse:
        return DleGaz2020ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DleGaz2020ResourceWithStreamingResponse:
        return DleGaz2020ResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        conso_pro: str | NotGiven = NOT_GIVEN,
        conso_pro_par_pdl: str | NotGiven = NOT_GIVEN,
        conso_res: str | NotGiven = NOT_GIVEN,
        conso_res_par_pdl: str | NotGiven = NOT_GIVEN,
        conso_tot: str | NotGiven = NOT_GIVEN,
        conso_tot_par_pdl: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_pdl_pro: str | NotGiven = NOT_GIVEN,
        nb_pdl_res: str | NotGiven = NOT_GIVEN,
        nb_pdl_tot: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DleGaz2020ListResponse:
        """
        [TABLE DEPRECIEE] Données de consommations des DLE agrégées à l'échelle du
        bâtiment

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          conso_pro: Consommation professionnelle [kWh/an]

          conso_pro_par_pdl: Consommation professionnelle par point de livraison [kWh/pdl.an]

          conso_res: Consommation résidentielle [kWh/an]

          conso_res_par_pdl: Consommation résidentielle par point de livraison [kWh/pdl.an]

          conso_tot: Consommation totale [kWh/an]

          conso_tot_par_pdl: Consommation totale par point de livraison [kWh/pdl.an]

          limit: Limiting and Pagination

          nb_pdl_pro: Nombre de points de livraisons professionel

          nb_pdl_res: Nombre de points de livraisons résidentiel

          nb_pdl_tot: Nombre total de points de livraisons

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/donnees/batiment_groupe_dle_gaz_2020",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "conso_pro": conso_pro,
                        "conso_pro_par_pdl": conso_pro_par_pdl,
                        "conso_res": conso_res,
                        "conso_res_par_pdl": conso_res_par_pdl,
                        "conso_tot": conso_tot,
                        "conso_tot_par_pdl": conso_tot_par_pdl,
                        "limit": limit,
                        "nb_pdl_pro": nb_pdl_pro,
                        "nb_pdl_res": nb_pdl_res,
                        "nb_pdl_tot": nb_pdl_tot,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    dle_gaz_2020_list_params.DleGaz2020ListParams,
                ),
            ),
            cast_to=DleGaz2020ListResponse,
        )


class AsyncDleGaz2020Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDleGaz2020ResourceWithRawResponse:
        return AsyncDleGaz2020ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDleGaz2020ResourceWithStreamingResponse:
        return AsyncDleGaz2020ResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        conso_pro: str | NotGiven = NOT_GIVEN,
        conso_pro_par_pdl: str | NotGiven = NOT_GIVEN,
        conso_res: str | NotGiven = NOT_GIVEN,
        conso_res_par_pdl: str | NotGiven = NOT_GIVEN,
        conso_tot: str | NotGiven = NOT_GIVEN,
        conso_tot_par_pdl: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_pdl_pro: str | NotGiven = NOT_GIVEN,
        nb_pdl_res: str | NotGiven = NOT_GIVEN,
        nb_pdl_tot: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DleGaz2020ListResponse:
        """
        [TABLE DEPRECIEE] Données de consommations des DLE agrégées à l'échelle du
        bâtiment

        Args:
          batiment_groupe_id: Identifiant du groupe de bâtiment au sens de la BDNB

          code_departement_insee: Code département INSEE

          conso_pro: Consommation professionnelle [kWh/an]

          conso_pro_par_pdl: Consommation professionnelle par point de livraison [kWh/pdl.an]

          conso_res: Consommation résidentielle [kWh/an]

          conso_res_par_pdl: Consommation résidentielle par point de livraison [kWh/pdl.an]

          conso_tot: Consommation totale [kWh/an]

          conso_tot_par_pdl: Consommation totale par point de livraison [kWh/pdl.an]

          limit: Limiting and Pagination

          nb_pdl_pro: Nombre de points de livraisons professionel

          nb_pdl_res: Nombre de points de livraisons résidentiel

          nb_pdl_tot: Nombre total de points de livraisons

          offset: Limiting and Pagination

          order: Ordering

          select: Filtering Columns

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Range": range,
                    "Range-Unit": range_unit,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/donnees/batiment_groupe_dle_gaz_2020",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "conso_pro": conso_pro,
                        "conso_pro_par_pdl": conso_pro_par_pdl,
                        "conso_res": conso_res,
                        "conso_res_par_pdl": conso_res_par_pdl,
                        "conso_tot": conso_tot,
                        "conso_tot_par_pdl": conso_tot_par_pdl,
                        "limit": limit,
                        "nb_pdl_pro": nb_pdl_pro,
                        "nb_pdl_res": nb_pdl_res,
                        "nb_pdl_tot": nb_pdl_tot,
                        "offset": offset,
                        "order": order,
                        "select": select,
                    },
                    dle_gaz_2020_list_params.DleGaz2020ListParams,
                ),
            ),
            cast_to=DleGaz2020ListResponse,
        )


class DleGaz2020ResourceWithRawResponse:
    def __init__(self, dle_gaz_2020: DleGaz2020Resource) -> None:
        self._dle_gaz_2020 = dle_gaz_2020

        self.list = to_raw_response_wrapper(
            dle_gaz_2020.list,
        )


class AsyncDleGaz2020ResourceWithRawResponse:
    def __init__(self, dle_gaz_2020: AsyncDleGaz2020Resource) -> None:
        self._dle_gaz_2020 = dle_gaz_2020

        self.list = async_to_raw_response_wrapper(
            dle_gaz_2020.list,
        )


class DleGaz2020ResourceWithStreamingResponse:
    def __init__(self, dle_gaz_2020: DleGaz2020Resource) -> None:
        self._dle_gaz_2020 = dle_gaz_2020

        self.list = to_streamed_response_wrapper(
            dle_gaz_2020.list,
        )


class AsyncDleGaz2020ResourceWithStreamingResponse:
    def __init__(self, dle_gaz_2020: AsyncDleGaz2020Resource) -> None:
        self._dle_gaz_2020 = dle_gaz_2020

        self.list = async_to_streamed_response_wrapper(
            dle_gaz_2020.list,
        )
