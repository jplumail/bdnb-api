# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentGroupeBdtopoBatListParams"]


class BatimentGroupeBdtopoBatListParams(TypedDict, total=False):
    altitude_sol_mean: str
    """(ign) Altitude au sol moyenne [m]"""

    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    hauteur_mean: str
    """(ign) Hauteur moyenne des bÃ¢timents [m]"""

    l_etat: str
    """(ign) Etat des bÃ¢timents"""

    l_nature: str
    """(ign) CatÃ©gorie de nature du bÃ¢timent"""

    l_usage_1: str
    """(ign) Usage principal du bÃ¢timent"""

    l_usage_2: str
    """(ign) Usage secondaire du bÃ¢timent"""

    limit: str
    """Limiting and Pagination"""

    max_hauteur: str
    """(ign) Hauteur maximale des bÃ¢timents [m]"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
