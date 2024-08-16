# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    is_given,
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
from ....types.tables_bdnb.donnees import rel_batiment_groupe_rnc_list_params
from ....types.tables_bdnb.donnees.rel_batiment_groupe_rnc_list_response import RelBatimentGroupeRncListResponse

__all__ = ["RelBatimentGroupeRncResource", "AsyncRelBatimentGroupeRncResource"]


class RelBatimentGroupeRncResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelBatimentGroupeRncResourceWithRawResponse:
        return RelBatimentGroupeRncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelBatimentGroupeRncResourceWithStreamingResponse:
        return RelBatimentGroupeRncResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        adresse_brut: str | NotGiven = NOT_GIVEN,
        adresse_geocodee: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        cle_interop_adr: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        fiabilite_geocodage: str | NotGiven = NOT_GIVEN,
        fiabilite_globale: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        numero_immat: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        parcelle_id: str | NotGiven = NOT_GIVEN,
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
    ) -> RelBatimentGroupeRncListResponse:
        """
        Table de relation entre les bÃ¢timents de la BDNB et les Ã©lÃ©ments de la table
        RNC

        Args:
          adresse_brut: adresse brute envoyÃ©e au gÃ©ocodeur

          adresse_geocodee: libelle de l'adresse retournÃ©e par le gÃ©ocodeur

          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          cle_interop_adr: ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale

          code_departement_insee: Code dÃ©partement INSEE

          fiabilite_geocodage: fiabilitÃ© du gÃ©ocodage

          fiabilite_globale: fiabilitÃ© du global du croisement

          limit: Limiting and Pagination

          numero_immat: identifiant de la table rnc

          offset: Limiting and Pagination

          order: Ordering

          parcelle_id: (ffo:idpar) Identifiant de parcelle (ConcatÃ©nation de ccodep, ccocom, ccopre,
              ccosec, dnupla)

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
            "/donnees/rel_batiment_groupe_rnc",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "adresse_brut": adresse_brut,
                        "adresse_geocodee": adresse_geocodee,
                        "batiment_groupe_id": batiment_groupe_id,
                        "cle_interop_adr": cle_interop_adr,
                        "code_departement_insee": code_departement_insee,
                        "fiabilite_geocodage": fiabilite_geocodage,
                        "fiabilite_globale": fiabilite_globale,
                        "limit": limit,
                        "numero_immat": numero_immat,
                        "offset": offset,
                        "order": order,
                        "parcelle_id": parcelle_id,
                        "select": select,
                    },
                    rel_batiment_groupe_rnc_list_params.RelBatimentGroupeRncListParams,
                ),
            ),
            cast_to=RelBatimentGroupeRncListResponse,
        )


class AsyncRelBatimentGroupeRncResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelBatimentGroupeRncResourceWithRawResponse:
        return AsyncRelBatimentGroupeRncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelBatimentGroupeRncResourceWithStreamingResponse:
        return AsyncRelBatimentGroupeRncResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        adresse_brut: str | NotGiven = NOT_GIVEN,
        adresse_geocodee: str | NotGiven = NOT_GIVEN,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        cle_interop_adr: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        fiabilite_geocodage: str | NotGiven = NOT_GIVEN,
        fiabilite_globale: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        numero_immat: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        parcelle_id: str | NotGiven = NOT_GIVEN,
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
    ) -> RelBatimentGroupeRncListResponse:
        """
        Table de relation entre les bÃ¢timents de la BDNB et les Ã©lÃ©ments de la table
        RNC

        Args:
          adresse_brut: adresse brute envoyÃ©e au gÃ©ocodeur

          adresse_geocodee: libelle de l'adresse retournÃ©e par le gÃ©ocodeur

          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          cle_interop_adr: ClÃ© d'interopÃ©rabilitÃ© de l'adresse postale

          code_departement_insee: Code dÃ©partement INSEE

          fiabilite_geocodage: fiabilitÃ© du gÃ©ocodage

          fiabilite_globale: fiabilitÃ© du global du croisement

          limit: Limiting and Pagination

          numero_immat: identifiant de la table rnc

          offset: Limiting and Pagination

          order: Ordering

          parcelle_id: (ffo:idpar) Identifiant de parcelle (ConcatÃ©nation de ccodep, ccocom, ccopre,
              ccosec, dnupla)

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
            "/donnees/rel_batiment_groupe_rnc",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "adresse_brut": adresse_brut,
                        "adresse_geocodee": adresse_geocodee,
                        "batiment_groupe_id": batiment_groupe_id,
                        "cle_interop_adr": cle_interop_adr,
                        "code_departement_insee": code_departement_insee,
                        "fiabilite_geocodage": fiabilite_geocodage,
                        "fiabilite_globale": fiabilite_globale,
                        "limit": limit,
                        "numero_immat": numero_immat,
                        "offset": offset,
                        "order": order,
                        "parcelle_id": parcelle_id,
                        "select": select,
                    },
                    rel_batiment_groupe_rnc_list_params.RelBatimentGroupeRncListParams,
                ),
            ),
            cast_to=RelBatimentGroupeRncListResponse,
        )


class RelBatimentGroupeRncResourceWithRawResponse:
    def __init__(self, rel_batiment_groupe_rnc: RelBatimentGroupeRncResource) -> None:
        self._rel_batiment_groupe_rnc = rel_batiment_groupe_rnc

        self.list = to_raw_response_wrapper(
            rel_batiment_groupe_rnc.list,
        )


class AsyncRelBatimentGroupeRncResourceWithRawResponse:
    def __init__(self, rel_batiment_groupe_rnc: AsyncRelBatimentGroupeRncResource) -> None:
        self._rel_batiment_groupe_rnc = rel_batiment_groupe_rnc

        self.list = async_to_raw_response_wrapper(
            rel_batiment_groupe_rnc.list,
        )


class RelBatimentGroupeRncResourceWithStreamingResponse:
    def __init__(self, rel_batiment_groupe_rnc: RelBatimentGroupeRncResource) -> None:
        self._rel_batiment_groupe_rnc = rel_batiment_groupe_rnc

        self.list = to_streamed_response_wrapper(
            rel_batiment_groupe_rnc.list,
        )


class AsyncRelBatimentGroupeRncResourceWithStreamingResponse:
    def __init__(self, rel_batiment_groupe_rnc: AsyncRelBatimentGroupeRncResource) -> None:
        self._rel_batiment_groupe_rnc = rel_batiment_groupe_rnc

        self.list = async_to_streamed_response_wrapper(
            rel_batiment_groupe_rnc.list,
        )
