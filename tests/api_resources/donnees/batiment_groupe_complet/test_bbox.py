# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.donnees.batiment_groupe_complet import BboxListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBbox:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        bbox = client.donnees.batiment_groupe_complet.bbox.list(
            xmax=989702,
            xmin=989701,
            ymax=6733740,
            ymin=6733739,
        )
        assert_matches_type(BboxListResponse, bbox, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        bbox = client.donnees.batiment_groupe_complet.bbox.list(
            xmax=989702,
            xmin=989701,
            ymax=6733740,
            ymin=6733739,
            srid=2154,
        )
        assert_matches_type(BboxListResponse, bbox, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.donnees.batiment_groupe_complet.bbox.with_raw_response.list(
            xmax=989702,
            xmin=989701,
            ymax=6733740,
            ymin=6733739,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bbox = response.parse()
        assert_matches_type(BboxListResponse, bbox, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.donnees.batiment_groupe_complet.bbox.with_streaming_response.list(
            xmax=989702,
            xmin=989701,
            ymax=6733740,
            ymin=6733739,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bbox = response.parse()
            assert_matches_type(BboxListResponse, bbox, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBbox:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        bbox = await async_client.donnees.batiment_groupe_complet.bbox.list(
            xmax=989702,
            xmin=989701,
            ymax=6733740,
            ymin=6733739,
        )
        assert_matches_type(BboxListResponse, bbox, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        bbox = await async_client.donnees.batiment_groupe_complet.bbox.list(
            xmax=989702,
            xmin=989701,
            ymax=6733740,
            ymin=6733739,
            srid=2154,
        )
        assert_matches_type(BboxListResponse, bbox, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.batiment_groupe_complet.bbox.with_raw_response.list(
            xmax=989702,
            xmin=989701,
            ymax=6733740,
            ymin=6733739,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bbox = await response.parse()
        assert_matches_type(BboxListResponse, bbox, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.batiment_groupe_complet.bbox.with_streaming_response.list(
            xmax=989702,
            xmin=989701,
            ymax=6733740,
            ymin=6733739,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bbox = await response.parse()
            assert_matches_type(BboxListResponse, bbox, path=["response"])

        assert cast(Any, response.is_closed) is True
