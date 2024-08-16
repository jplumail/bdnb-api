# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
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
from ...types.donnees import batiment_groupe_dvf_open_representatif_list_params
from ...types.donnees.batiment_groupe_dvf_open_representatif_list_response import (
    BatimentGroupeDvfOpenRepresentatifListResponse,
)

__all__ = ["BatimentGroupeDvfOpenRepresentatifResource", "AsyncBatimentGroupeDvfOpenRepresentatifResource"]


class BatimentGroupeDvfOpenRepresentatifResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeDvfOpenRepresentatifResourceWithRawResponse:
        return BatimentGroupeDvfOpenRepresentatifResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeDvfOpenRepresentatifResourceWithStreamingResponse:
        return BatimentGroupeDvfOpenRepresentatifResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        date_mutation: Union[str, date] | NotGiven = NOT_GIVEN,
        id_opendata: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_appartement_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_dependance_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_locaux_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_locaux_tertiaire_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_maison_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_piece_principale: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        prix_m2_local: str | NotGiven = NOT_GIVEN,
        prix_m2_terrain: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        surface_bati_mutee_dependance: str | NotGiven = NOT_GIVEN,
        surface_bati_mutee_residencielle_collective: str | NotGiven = NOT_GIVEN,
        surface_bati_mutee_residencielle_individuelle: str | NotGiven = NOT_GIVEN,
        surface_bati_mutee_tertiaire: str | NotGiven = NOT_GIVEN,
        surface_terrain_mutee: str | NotGiven = NOT_GIVEN,
        valeur_fonciere: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentGroupeDvfOpenRepresentatifListResponse:
        """
        DonnÃ©es des mutations issues des valeurs DVF open data pour une mutation
        reprÃ©sentative du batiment_groupe

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          date_mutation: (dv3f) date de la mutation

          id_opendata: Identifiant open data de la mutation.

          limit: Limiting and Pagination

          nb_appartement_mutee_mutation: Nombre d'appartements ayant mutÃ©s lors de la mutation reprÃ©sentative.

          nb_dependance_mutee_mutation: Nombre de dÃ©pendances ayant mutÃ©es lors de la mutation reprÃ©sentative.

          nb_locaux_mutee_mutation: Nombre de locaux ayant mutÃ©s lors de la mutation reprÃ©sentative.

          nb_locaux_tertiaire_mutee_mutation: Nombre de locaux tertiaires ayant mutÃ©s lors de la mutation reprÃ©sentative.

          nb_maison_mutee_mutation: Nombre de maisons ayant mutÃ©es lors de la mutation reprÃ©sentative.

          nb_piece_principale: Nombre de piÃ¨ces principales de la rÃ©sidence individuelle ou collective ayant
              mutÃ©. Cet indicateur est disponible lorsqu'une unique rÃ©sidence individuelle
              ou collective a mutÃ©e.

          offset: Limiting and Pagination

          order: Ordering

          prix_m2_local: Prix au mÂ² de bÃ¢ti en euros lors de la mutation. Cet indicateur n'est
              disponible que pour des transactions dont uniquement les locaux (rÃ©sidences
              individuelles + dÃ©pendances) ou (rÃ©sidences collectives + dÃ©pendances) ont
              mutÃ©es [â‚¬]

          prix_m2_terrain: Prix au mÂ² du terrain en euros lors de la mutation. Cet indicateur n'est
              disponible que pour des transactions dont uniquement les locaux (rÃ©sidences
              individuelles + dÃ©pendances) ou (rÃ©sidences collectives + dÃ©pendances) ont
              mutÃ©es [â‚¬]

          select: Filtering Columns

          surface_bati_mutee_dependance: Surface de bÃ¢ti associÃ©e Ã des dÃ©pendances ayant mutÃ©es lors de la mutation
              reprÃ©sentative [mÂ²].

          surface_bati_mutee_residencielle_collective: Surface de bÃ¢ti associÃ©e Ã des rÃ©sidences collectives ayant mutÃ©es lors de
              la mutation reprÃ©sentative [mÂ²].

          surface_bati_mutee_residencielle_individuelle: Surface de bÃ¢ti associÃ©e Ã des rÃ©sidences individuelles ayant mutÃ©es lors de
              la mutation reprÃ©sentative [mÂ²].

          surface_bati_mutee_tertiaire: Surface de bÃ¢ti associÃ©e Ã du tertiaire ayant mutÃ©es lors de la mutation
              reprÃ©sentative [mÂ²].

          surface_terrain_mutee: Surface de terrain ayant mutÃ© lors de la mutation reprÃ©sentative [mÂ²].

          valeur_fonciere: Valeur fonciÃ¨re en euros de la mutation reprÃ©sentative. [â‚¬]

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
            "/donnees/batiment_groupe_dvf_open_representatif",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "date_mutation": date_mutation,
                        "id_opendata": id_opendata,
                        "limit": limit,
                        "nb_appartement_mutee_mutation": nb_appartement_mutee_mutation,
                        "nb_dependance_mutee_mutation": nb_dependance_mutee_mutation,
                        "nb_locaux_mutee_mutation": nb_locaux_mutee_mutation,
                        "nb_locaux_tertiaire_mutee_mutation": nb_locaux_tertiaire_mutee_mutation,
                        "nb_maison_mutee_mutation": nb_maison_mutee_mutation,
                        "nb_piece_principale": nb_piece_principale,
                        "offset": offset,
                        "order": order,
                        "prix_m2_local": prix_m2_local,
                        "prix_m2_terrain": prix_m2_terrain,
                        "select": select,
                        "surface_bati_mutee_dependance": surface_bati_mutee_dependance,
                        "surface_bati_mutee_residencielle_collective": surface_bati_mutee_residencielle_collective,
                        "surface_bati_mutee_residencielle_individuelle": surface_bati_mutee_residencielle_individuelle,
                        "surface_bati_mutee_tertiaire": surface_bati_mutee_tertiaire,
                        "surface_terrain_mutee": surface_terrain_mutee,
                        "valeur_fonciere": valeur_fonciere,
                    },
                    batiment_groupe_dvf_open_representatif_list_params.BatimentGroupeDvfOpenRepresentatifListParams,
                ),
            ),
            cast_to=BatimentGroupeDvfOpenRepresentatifListResponse,
        )


class AsyncBatimentGroupeDvfOpenRepresentatifResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeDvfOpenRepresentatifResourceWithRawResponse:
        return AsyncBatimentGroupeDvfOpenRepresentatifResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeDvfOpenRepresentatifResourceWithStreamingResponse:
        return AsyncBatimentGroupeDvfOpenRepresentatifResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        date_mutation: Union[str, date] | NotGiven = NOT_GIVEN,
        id_opendata: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        nb_appartement_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_dependance_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_locaux_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_locaux_tertiaire_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_maison_mutee_mutation: str | NotGiven = NOT_GIVEN,
        nb_piece_principale: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        prix_m2_local: str | NotGiven = NOT_GIVEN,
        prix_m2_terrain: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        surface_bati_mutee_dependance: str | NotGiven = NOT_GIVEN,
        surface_bati_mutee_residencielle_collective: str | NotGiven = NOT_GIVEN,
        surface_bati_mutee_residencielle_individuelle: str | NotGiven = NOT_GIVEN,
        surface_bati_mutee_tertiaire: str | NotGiven = NOT_GIVEN,
        surface_terrain_mutee: str | NotGiven = NOT_GIVEN,
        valeur_fonciere: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentGroupeDvfOpenRepresentatifListResponse:
        """
        DonnÃ©es des mutations issues des valeurs DVF open data pour une mutation
        reprÃ©sentative du batiment_groupe

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          code_departement_insee: Code dÃ©partement INSEE

          date_mutation: (dv3f) date de la mutation

          id_opendata: Identifiant open data de la mutation.

          limit: Limiting and Pagination

          nb_appartement_mutee_mutation: Nombre d'appartements ayant mutÃ©s lors de la mutation reprÃ©sentative.

          nb_dependance_mutee_mutation: Nombre de dÃ©pendances ayant mutÃ©es lors de la mutation reprÃ©sentative.

          nb_locaux_mutee_mutation: Nombre de locaux ayant mutÃ©s lors de la mutation reprÃ©sentative.

          nb_locaux_tertiaire_mutee_mutation: Nombre de locaux tertiaires ayant mutÃ©s lors de la mutation reprÃ©sentative.

          nb_maison_mutee_mutation: Nombre de maisons ayant mutÃ©es lors de la mutation reprÃ©sentative.

          nb_piece_principale: Nombre de piÃ¨ces principales de la rÃ©sidence individuelle ou collective ayant
              mutÃ©. Cet indicateur est disponible lorsqu'une unique rÃ©sidence individuelle
              ou collective a mutÃ©e.

          offset: Limiting and Pagination

          order: Ordering

          prix_m2_local: Prix au mÂ² de bÃ¢ti en euros lors de la mutation. Cet indicateur n'est
              disponible que pour des transactions dont uniquement les locaux (rÃ©sidences
              individuelles + dÃ©pendances) ou (rÃ©sidences collectives + dÃ©pendances) ont
              mutÃ©es [â‚¬]

          prix_m2_terrain: Prix au mÂ² du terrain en euros lors de la mutation. Cet indicateur n'est
              disponible que pour des transactions dont uniquement les locaux (rÃ©sidences
              individuelles + dÃ©pendances) ou (rÃ©sidences collectives + dÃ©pendances) ont
              mutÃ©es [â‚¬]

          select: Filtering Columns

          surface_bati_mutee_dependance: Surface de bÃ¢ti associÃ©e Ã des dÃ©pendances ayant mutÃ©es lors de la mutation
              reprÃ©sentative [mÂ²].

          surface_bati_mutee_residencielle_collective: Surface de bÃ¢ti associÃ©e Ã des rÃ©sidences collectives ayant mutÃ©es lors de
              la mutation reprÃ©sentative [mÂ²].

          surface_bati_mutee_residencielle_individuelle: Surface de bÃ¢ti associÃ©e Ã des rÃ©sidences individuelles ayant mutÃ©es lors de
              la mutation reprÃ©sentative [mÂ²].

          surface_bati_mutee_tertiaire: Surface de bÃ¢ti associÃ©e Ã du tertiaire ayant mutÃ©es lors de la mutation
              reprÃ©sentative [mÂ²].

          surface_terrain_mutee: Surface de terrain ayant mutÃ© lors de la mutation reprÃ©sentative [mÂ²].

          valeur_fonciere: Valeur fonciÃ¨re en euros de la mutation reprÃ©sentative. [â‚¬]

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
            "/donnees/batiment_groupe_dvf_open_representatif",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "code_departement_insee": code_departement_insee,
                        "date_mutation": date_mutation,
                        "id_opendata": id_opendata,
                        "limit": limit,
                        "nb_appartement_mutee_mutation": nb_appartement_mutee_mutation,
                        "nb_dependance_mutee_mutation": nb_dependance_mutee_mutation,
                        "nb_locaux_mutee_mutation": nb_locaux_mutee_mutation,
                        "nb_locaux_tertiaire_mutee_mutation": nb_locaux_tertiaire_mutee_mutation,
                        "nb_maison_mutee_mutation": nb_maison_mutee_mutation,
                        "nb_piece_principale": nb_piece_principale,
                        "offset": offset,
                        "order": order,
                        "prix_m2_local": prix_m2_local,
                        "prix_m2_terrain": prix_m2_terrain,
                        "select": select,
                        "surface_bati_mutee_dependance": surface_bati_mutee_dependance,
                        "surface_bati_mutee_residencielle_collective": surface_bati_mutee_residencielle_collective,
                        "surface_bati_mutee_residencielle_individuelle": surface_bati_mutee_residencielle_individuelle,
                        "surface_bati_mutee_tertiaire": surface_bati_mutee_tertiaire,
                        "surface_terrain_mutee": surface_terrain_mutee,
                        "valeur_fonciere": valeur_fonciere,
                    },
                    batiment_groupe_dvf_open_representatif_list_params.BatimentGroupeDvfOpenRepresentatifListParams,
                ),
            ),
            cast_to=BatimentGroupeDvfOpenRepresentatifListResponse,
        )


class BatimentGroupeDvfOpenRepresentatifResourceWithRawResponse:
    def __init__(self, batiment_groupe_dvf_open_representatif: BatimentGroupeDvfOpenRepresentatifResource) -> None:
        self._batiment_groupe_dvf_open_representatif = batiment_groupe_dvf_open_representatif

        self.list = to_raw_response_wrapper(
            batiment_groupe_dvf_open_representatif.list,
        )


class AsyncBatimentGroupeDvfOpenRepresentatifResourceWithRawResponse:
    def __init__(self, batiment_groupe_dvf_open_representatif: AsyncBatimentGroupeDvfOpenRepresentatifResource) -> None:
        self._batiment_groupe_dvf_open_representatif = batiment_groupe_dvf_open_representatif

        self.list = async_to_raw_response_wrapper(
            batiment_groupe_dvf_open_representatif.list,
        )


class BatimentGroupeDvfOpenRepresentatifResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_dvf_open_representatif: BatimentGroupeDvfOpenRepresentatifResource) -> None:
        self._batiment_groupe_dvf_open_representatif = batiment_groupe_dvf_open_representatif

        self.list = to_streamed_response_wrapper(
            batiment_groupe_dvf_open_representatif.list,
        )


class AsyncBatimentGroupeDvfOpenRepresentatifResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_dvf_open_representatif: AsyncBatimentGroupeDvfOpenRepresentatifResource) -> None:
        self._batiment_groupe_dvf_open_representatif = batiment_groupe_dvf_open_representatif

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe_dvf_open_representatif.list,
        )
