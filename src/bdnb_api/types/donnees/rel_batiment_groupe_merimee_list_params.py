# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RelBatimentGroupeMerimeeListParams"]


class RelBatimentGroupeMerimeeListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    distance_batiment_historique: str
    """
    (mer) Distance entre le batiment_historique et le batiment_construction (si
    moins de 500m) [m]
    """

    limit: str
    """Limiting and Pagination"""

    merimee_ref: str
    """identifiant de la table merimee"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
