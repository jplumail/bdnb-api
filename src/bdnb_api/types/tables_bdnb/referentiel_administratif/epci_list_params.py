# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EpciListParams"]


class EpciListParams(TypedDict, total=False):
    code_epci_insee: str
    """Code de l'EPCI"""

    geom_epci: str
    """GÃ©omÃ©trie de l'EPCI"""

    libelle_epci: str
    """LibellÃ© de l'EPCI"""

    limit: str
    """Limiting and Pagination"""

    nature_epci: str
    """Type d'EPCI"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
