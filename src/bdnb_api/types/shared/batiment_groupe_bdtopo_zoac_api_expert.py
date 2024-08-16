# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["BatimentGroupeBdtopoZoacAPIExpert"]


class BatimentGroupeBdtopoZoacAPIExpert(BaseModel):
    batiment_groupe_id: Optional[str] = None
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB

    Note: This is a Primary Key.<pk/>
    """

    code_departement_insee: Optional[str] = None
    """Code dÃ©partement INSEE"""

    l_nature: Optional[List[str]] = None
    """(ign) CatÃ©gorie de nature du bÃ¢timent"""

    l_nature_detaillee: Optional[List[str]] = None
    """(ign) CatÃ©gorie dÃ©taillÃ©e de nature de l'Ã©quipement"""

    l_toponyme: Optional[List[str]] = None
    """(ign) Toponymie de l'Ã©quipement"""
