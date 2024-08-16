# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TablesBdnbRetrieveReferentielAdministratifIrisParams"]


class TablesBdnbRetrieveReferentielAdministratifIrisParams(TypedDict, total=False):
    code_commune_insee: str
    """Code INSEE de la commune"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    code_iris: str
    """Code iris INSEE"""

    geom_iris: str
    """GÃ©omÃ©trie de l'IRIS"""

    libelle_iris: str
    """LibellÃ© de l'iris"""

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    type_iris: str
    """Type de l'IRIS"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
