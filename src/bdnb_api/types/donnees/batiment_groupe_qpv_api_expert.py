# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeQpvAPIExpert"]


class BatimentGroupeQpvAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    nom_quartier: Optional[str] = None
    """Nom du quartier prioritaire dans lequel se trouve le bÃ¢timent"""
