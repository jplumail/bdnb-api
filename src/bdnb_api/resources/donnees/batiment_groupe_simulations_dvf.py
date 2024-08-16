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
from ...types.donnees import batiment_groupe_simulations_dvf_list_params
from ...types.donnees.batiment_groupe_simulations_dvf_list_response import BatimentGroupeSimulationsDvfListResponse

__all__ = ["BatimentGroupeSimulationsDvfResource", "AsyncBatimentGroupeSimulationsDvfResource"]


class BatimentGroupeSimulationsDvfResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatimentGroupeSimulationsDvfResourceWithRawResponse:
        return BatimentGroupeSimulationsDvfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatimentGroupeSimulationsDvfResourceWithStreamingResponse:
        return BatimentGroupeSimulationsDvfResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        classe_dpe_conso_initial: str | NotGiven = NOT_GIVEN,
        classe_dpe_conso_renove: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        difference_abs_valeur_fonciere_etat_initial_renove: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_etat_initial_renove: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_etat_initial_renove_categorie: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_initial_mean_iris: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_renove_mean_iris: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        r2: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        usage_niveau_1_txt: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_estim_lower: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_estim_mean: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_estim_upper: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_incertitude: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_renove_estim_lower: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_renove_estim_mean: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_renove_estim_upper: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_renove_incertitude: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentGroupeSimulationsDvfListResponse:
        """
        Simulations des valeurs fonciÃ¨res des bÃ¢timents

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          classe_dpe_conso_initial: classe dpe a l'echelle bÃ¢timent predit dans son etat initial

          classe_dpe_conso_renove: classe dpe a l'echelle bÃ¢timent predit dans son etat renove

          code_departement_insee: Code dÃ©partement INSEE

          difference_abs_valeur_fonciere_etat_initial_renove: difference absolue entre la valeur fonciÃ¨re avant et apres renovation [â‚¬/mÂ²]

          difference_rel_valeur_fonciere_etat_initial_renove: difference relative de valeur fonciere avant et apres renovation

          difference_rel_valeur_fonciere_etat_initial_renove_categorie: categorie de la difference relative de valeur fonciere avant et apres renovation
              (verbose)

          difference_rel_valeur_fonciere_initial_mean_iris: difference relative de la valeur fonciere avant renovation par rapport Ã la
              moyenne Ã l'iris predite sans renovation

          difference_rel_valeur_fonciere_renove_mean_iris: difference relative de la valeur fonciere apres renovation par rapport Ã la
              moyenne Ã l'iris predite sans renovation

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          r2: r2 du modele de simulation

          select: Filtering Columns

          usage_niveau_1_txt: indicateurs d'usage simplifiÃ© du bÃ¢timent (verbose)

          valeur_fonciere_etat_initial_estim_lower: Estimation basse de la valeur fonciere avant renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_initial_estim_mean: Estimation moyenne de la valeur fonciere avant renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_initial_estim_upper: Estimation haute de la valeur fonciere avant renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_initial_incertitude: incertitude de l'estimation de la valeur fonciere avant renovation

          valeur_fonciere_etat_renove_estim_lower: Estimation basse de la valeur fonciere apres renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_renove_estim_mean: Estimation moyenne de la valeur fonciere apres renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_renove_estim_upper: Estimation haute de la valeur fonciere apres renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_renove_incertitude: incertitude de l'estimation de la valeur fonciere apres renovation

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
            "/donnees/batiment_groupe_simulations_dvf",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "classe_dpe_conso_initial": classe_dpe_conso_initial,
                        "classe_dpe_conso_renove": classe_dpe_conso_renove,
                        "code_departement_insee": code_departement_insee,
                        "difference_abs_valeur_fonciere_etat_initial_renove": difference_abs_valeur_fonciere_etat_initial_renove,
                        "difference_rel_valeur_fonciere_etat_initial_renove": difference_rel_valeur_fonciere_etat_initial_renove,
                        "difference_rel_valeur_fonciere_etat_initial_renove_categorie": difference_rel_valeur_fonciere_etat_initial_renove_categorie,
                        "difference_rel_valeur_fonciere_initial_mean_iris": difference_rel_valeur_fonciere_initial_mean_iris,
                        "difference_rel_valeur_fonciere_renove_mean_iris": difference_rel_valeur_fonciere_renove_mean_iris,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "r2": r2,
                        "select": select,
                        "usage_niveau_1_txt": usage_niveau_1_txt,
                        "valeur_fonciere_etat_initial_estim_lower": valeur_fonciere_etat_initial_estim_lower,
                        "valeur_fonciere_etat_initial_estim_mean": valeur_fonciere_etat_initial_estim_mean,
                        "valeur_fonciere_etat_initial_estim_upper": valeur_fonciere_etat_initial_estim_upper,
                        "valeur_fonciere_etat_initial_incertitude": valeur_fonciere_etat_initial_incertitude,
                        "valeur_fonciere_etat_renove_estim_lower": valeur_fonciere_etat_renove_estim_lower,
                        "valeur_fonciere_etat_renove_estim_mean": valeur_fonciere_etat_renove_estim_mean,
                        "valeur_fonciere_etat_renove_estim_upper": valeur_fonciere_etat_renove_estim_upper,
                        "valeur_fonciere_etat_renove_incertitude": valeur_fonciere_etat_renove_incertitude,
                    },
                    batiment_groupe_simulations_dvf_list_params.BatimentGroupeSimulationsDvfListParams,
                ),
            ),
            cast_to=BatimentGroupeSimulationsDvfListResponse,
        )


class AsyncBatimentGroupeSimulationsDvfResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatimentGroupeSimulationsDvfResourceWithRawResponse:
        return AsyncBatimentGroupeSimulationsDvfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatimentGroupeSimulationsDvfResourceWithStreamingResponse:
        return AsyncBatimentGroupeSimulationsDvfResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        batiment_groupe_id: str | NotGiven = NOT_GIVEN,
        classe_dpe_conso_initial: str | NotGiven = NOT_GIVEN,
        classe_dpe_conso_renove: str | NotGiven = NOT_GIVEN,
        code_departement_insee: str | NotGiven = NOT_GIVEN,
        difference_abs_valeur_fonciere_etat_initial_renove: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_etat_initial_renove: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_etat_initial_renove_categorie: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_initial_mean_iris: str | NotGiven = NOT_GIVEN,
        difference_rel_valeur_fonciere_renove_mean_iris: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        offset: str | NotGiven = NOT_GIVEN,
        order: str | NotGiven = NOT_GIVEN,
        r2: str | NotGiven = NOT_GIVEN,
        select: str | NotGiven = NOT_GIVEN,
        usage_niveau_1_txt: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_estim_lower: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_estim_mean: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_estim_upper: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_initial_incertitude: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_renove_estim_lower: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_renove_estim_mean: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_renove_estim_upper: str | NotGiven = NOT_GIVEN,
        valeur_fonciere_etat_renove_incertitude: str | NotGiven = NOT_GIVEN,
        prefer: Literal["count=none"] | NotGiven = NOT_GIVEN,
        range: str | NotGiven = NOT_GIVEN,
        range_unit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatimentGroupeSimulationsDvfListResponse:
        """
        Simulations des valeurs fonciÃ¨res des bÃ¢timents

        Args:
          batiment_groupe_id: Identifiant du groupe de bÃ¢timent au sens de la BDNB

          classe_dpe_conso_initial: classe dpe a l'echelle bÃ¢timent predit dans son etat initial

          classe_dpe_conso_renove: classe dpe a l'echelle bÃ¢timent predit dans son etat renove

          code_departement_insee: Code dÃ©partement INSEE

          difference_abs_valeur_fonciere_etat_initial_renove: difference absolue entre la valeur fonciÃ¨re avant et apres renovation [â‚¬/mÂ²]

          difference_rel_valeur_fonciere_etat_initial_renove: difference relative de valeur fonciere avant et apres renovation

          difference_rel_valeur_fonciere_etat_initial_renove_categorie: categorie de la difference relative de valeur fonciere avant et apres renovation
              (verbose)

          difference_rel_valeur_fonciere_initial_mean_iris: difference relative de la valeur fonciere avant renovation par rapport Ã la
              moyenne Ã l'iris predite sans renovation

          difference_rel_valeur_fonciere_renove_mean_iris: difference relative de la valeur fonciere apres renovation par rapport Ã la
              moyenne Ã l'iris predite sans renovation

          limit: Limiting and Pagination

          offset: Limiting and Pagination

          order: Ordering

          r2: r2 du modele de simulation

          select: Filtering Columns

          usage_niveau_1_txt: indicateurs d'usage simplifiÃ© du bÃ¢timent (verbose)

          valeur_fonciere_etat_initial_estim_lower: Estimation basse de la valeur fonciere avant renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_initial_estim_mean: Estimation moyenne de la valeur fonciere avant renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_initial_estim_upper: Estimation haute de la valeur fonciere avant renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_initial_incertitude: incertitude de l'estimation de la valeur fonciere avant renovation

          valeur_fonciere_etat_renove_estim_lower: Estimation basse de la valeur fonciere apres renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_renove_estim_mean: Estimation moyenne de la valeur fonciere apres renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_renove_estim_upper: Estimation haute de la valeur fonciere apres renovation [â‚¬/mÂ²]

          valeur_fonciere_etat_renove_incertitude: incertitude de l'estimation de la valeur fonciere apres renovation

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
            "/donnees/batiment_groupe_simulations_dvf",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "batiment_groupe_id": batiment_groupe_id,
                        "classe_dpe_conso_initial": classe_dpe_conso_initial,
                        "classe_dpe_conso_renove": classe_dpe_conso_renove,
                        "code_departement_insee": code_departement_insee,
                        "difference_abs_valeur_fonciere_etat_initial_renove": difference_abs_valeur_fonciere_etat_initial_renove,
                        "difference_rel_valeur_fonciere_etat_initial_renove": difference_rel_valeur_fonciere_etat_initial_renove,
                        "difference_rel_valeur_fonciere_etat_initial_renove_categorie": difference_rel_valeur_fonciere_etat_initial_renove_categorie,
                        "difference_rel_valeur_fonciere_initial_mean_iris": difference_rel_valeur_fonciere_initial_mean_iris,
                        "difference_rel_valeur_fonciere_renove_mean_iris": difference_rel_valeur_fonciere_renove_mean_iris,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "r2": r2,
                        "select": select,
                        "usage_niveau_1_txt": usage_niveau_1_txt,
                        "valeur_fonciere_etat_initial_estim_lower": valeur_fonciere_etat_initial_estim_lower,
                        "valeur_fonciere_etat_initial_estim_mean": valeur_fonciere_etat_initial_estim_mean,
                        "valeur_fonciere_etat_initial_estim_upper": valeur_fonciere_etat_initial_estim_upper,
                        "valeur_fonciere_etat_initial_incertitude": valeur_fonciere_etat_initial_incertitude,
                        "valeur_fonciere_etat_renove_estim_lower": valeur_fonciere_etat_renove_estim_lower,
                        "valeur_fonciere_etat_renove_estim_mean": valeur_fonciere_etat_renove_estim_mean,
                        "valeur_fonciere_etat_renove_estim_upper": valeur_fonciere_etat_renove_estim_upper,
                        "valeur_fonciere_etat_renove_incertitude": valeur_fonciere_etat_renove_incertitude,
                    },
                    batiment_groupe_simulations_dvf_list_params.BatimentGroupeSimulationsDvfListParams,
                ),
            ),
            cast_to=BatimentGroupeSimulationsDvfListResponse,
        )


class BatimentGroupeSimulationsDvfResourceWithRawResponse:
    def __init__(self, batiment_groupe_simulations_dvf: BatimentGroupeSimulationsDvfResource) -> None:
        self._batiment_groupe_simulations_dvf = batiment_groupe_simulations_dvf

        self.list = to_raw_response_wrapper(
            batiment_groupe_simulations_dvf.list,
        )


class AsyncBatimentGroupeSimulationsDvfResourceWithRawResponse:
    def __init__(self, batiment_groupe_simulations_dvf: AsyncBatimentGroupeSimulationsDvfResource) -> None:
        self._batiment_groupe_simulations_dvf = batiment_groupe_simulations_dvf

        self.list = async_to_raw_response_wrapper(
            batiment_groupe_simulations_dvf.list,
        )


class BatimentGroupeSimulationsDvfResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_simulations_dvf: BatimentGroupeSimulationsDvfResource) -> None:
        self._batiment_groupe_simulations_dvf = batiment_groupe_simulations_dvf

        self.list = to_streamed_response_wrapper(
            batiment_groupe_simulations_dvf.list,
        )


class AsyncBatimentGroupeSimulationsDvfResourceWithStreamingResponse:
    def __init__(self, batiment_groupe_simulations_dvf: AsyncBatimentGroupeSimulationsDvfResource) -> None:
        self._batiment_groupe_simulations_dvf = batiment_groupe_simulations_dvf

        self.list = async_to_streamed_response_wrapper(
            batiment_groupe_simulations_dvf.list,
        )
