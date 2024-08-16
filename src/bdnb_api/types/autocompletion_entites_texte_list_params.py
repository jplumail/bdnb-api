# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AutocompletionEntitesTexteListParams"]


class AutocompletionEntitesTexteListParams(TypedDict, total=False):
    code: str
    """code de l'entitÃ©"""

    geom: str
    """geometrie de l'entitÃ© s'il y en a une"""

    limit: str
    """Limiting and Pagination"""

    nom: str
    """nom d'entitÃ©"""

    nom_unaccent: str
    """nom d'entitÃ© sans accent"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    origine_code: str
    """nom de la table de la colonne d'origine du code"""

    origine_nom: str
    """nom de la table de la colonne d'origine du nom"""

    select: str
    """Filtering Columns"""

    type_entite: str
    """type de l'entitÃ©"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
