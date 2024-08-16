# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MetadonneesCompletListParams"]


class MetadonneesCompletListParams(TypedDict, total=False):
    api_expert: str
    """Disponible pour les abonnÃ©s de l'API Expert"""

    api_open: str
    """Disponible sans souscription"""

    colonne_gorenove_legacy: str
    """Nom de la colonne dans l'ancienne API gorenove /v2/gorenove/buildings"""

    contrainte_acces: str
    """Contrainte d'accÃ¨s de la colonne"""

    contrainte_acces_table: str
    """Contrainte d'accÃ¨s de la table"""

    couverture_spatiale: str
    """Couverture spatiale du jeu de donnÃ©es"""

    couverture_temporelle: str
    """Couverture temporelle du jeu de donnÃ©es"""

    date_publication: str
    """Date de publication du jeu de donnÃ©es"""

    denomination_serie: str
    """DÃ©nomination du jeu de donnÃ©es"""

    description: str
    """Description de la table"""

    description_jeu_de_donnees: str
    """Description du jeu de donnÃ©es"""

    description_table: str

    index: str
    """la colonne est indexÃ©e dans la table"""

    libelle_metier: str
    """libelle Ã utiliser dans les applications web"""

    limit: str
    """Limiting and Pagination"""

    millesime_jeu_de_donnees: str
    """MillÃ©sime du jeu de donnÃ©es"""

    nom_colonne: str
    """Nom de la colonne"""

    nom_table: str
    """Nom de la table rattachÃ©e"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    route: str

    row_number: str

    select: str
    """Filtering Columns"""

    type: str
    """Type de la colonne"""

    unite: str
    """UnitÃ© de la colonne"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
