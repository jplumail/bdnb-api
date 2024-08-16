# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.tables_bdnb.donnees import (
    IrisSimulationsValeurVerteListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIrisSimulationsValeurVerte:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        iris_simulations_valeur_verte = client.tables_bdnb.donnees.iris_simulations_valeur_verte.list()
        assert_matches_type(IrisSimulationsValeurVerteListResponse, iris_simulations_valeur_verte, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        iris_simulations_valeur_verte = client.tables_bdnb.donnees.iris_simulations_valeur_verte.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            gain_classe_b_vers_a=0,
            gain_classe_c_vers_a={},
            gain_classe_c_vers_b={},
            gain_classe_d_vers_a={},
            gain_classe_d_vers_b={},
            gain_classe_d_vers_c={},
            gain_classe_e_vers_a={},
            gain_classe_e_vers_b={},
            gain_classe_e_vers_c={},
            gain_classe_e_vers_d={},
            gain_classe_f_vers_a={},
            gain_classe_f_vers_b={},
            gain_classe_f_vers_c={},
            gain_classe_f_vers_d={},
            gain_classe_f_vers_e={},
            gain_classe_g_vers_a={},
            gain_classe_g_vers_b={},
            gain_classe_g_vers_c={},
            gain_classe_g_vers_d={},
            gain_classe_g_vers_e={},
            gain_classe_g_vers_f={},
            limit="limit",
            offset="offset",
            order="order",
            renovation=0,
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(IrisSimulationsValeurVerteListResponse, iris_simulations_valeur_verte, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.tables_bdnb.donnees.iris_simulations_valeur_verte.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        iris_simulations_valeur_verte = response.parse()
        assert_matches_type(IrisSimulationsValeurVerteListResponse, iris_simulations_valeur_verte, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.tables_bdnb.donnees.iris_simulations_valeur_verte.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            iris_simulations_valeur_verte = response.parse()
            assert_matches_type(
                IrisSimulationsValeurVerteListResponse, iris_simulations_valeur_verte, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncIrisSimulationsValeurVerte:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        iris_simulations_valeur_verte = await async_client.tables_bdnb.donnees.iris_simulations_valeur_verte.list()
        assert_matches_type(IrisSimulationsValeurVerteListResponse, iris_simulations_valeur_verte, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        iris_simulations_valeur_verte = await async_client.tables_bdnb.donnees.iris_simulations_valeur_verte.list(
            batiment_groupe_id="batiment_groupe_id",
            code_departement_insee="code_departement_insee",
            gain_classe_b_vers_a=0,
            gain_classe_c_vers_a={},
            gain_classe_c_vers_b={},
            gain_classe_d_vers_a={},
            gain_classe_d_vers_b={},
            gain_classe_d_vers_c={},
            gain_classe_e_vers_a={},
            gain_classe_e_vers_b={},
            gain_classe_e_vers_c={},
            gain_classe_e_vers_d={},
            gain_classe_f_vers_a={},
            gain_classe_f_vers_b={},
            gain_classe_f_vers_c={},
            gain_classe_f_vers_d={},
            gain_classe_f_vers_e={},
            gain_classe_g_vers_a={},
            gain_classe_g_vers_b={},
            gain_classe_g_vers_c={},
            gain_classe_g_vers_d={},
            gain_classe_g_vers_e={},
            gain_classe_g_vers_f={},
            limit="limit",
            offset="offset",
            order="order",
            renovation=0,
            select="select",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(IrisSimulationsValeurVerteListResponse, iris_simulations_valeur_verte, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.tables_bdnb.donnees.iris_simulations_valeur_verte.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        iris_simulations_valeur_verte = await response.parse()
        assert_matches_type(IrisSimulationsValeurVerteListResponse, iris_simulations_valeur_verte, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.tables_bdnb.donnees.iris_simulations_valeur_verte.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            iris_simulations_valeur_verte = await response.parse()
            assert_matches_type(
                IrisSimulationsValeurVerteListResponse, iris_simulations_valeur_verte, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
