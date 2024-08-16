# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentGroupeDleReseaux2020ListParams"]


class BatimentGroupeDleReseaux2020ListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    conso_pro: str
    """Consommation professionnelle [kWh/an]"""

    conso_pro_par_pdl: str
    """Consommation professionnelle par point de livraison [kWh/pdl.an]"""

    conso_res: str
    """Consommation rÃ©sidentielle [kWh/an]"""

    conso_res_par_pdl: str
    """Consommation rÃ©sidentielle par point de livraison [kWh/pdl.an]"""

    conso_tot: str
    """Consommation totale [kWh/an]"""

    conso_tot_par_pdl: str
    """Consommation totale par point de livraison [kWh/pdl.an]"""

    identifiant_reseau: str
    """Identifiant du reseau de chaleur"""

    limit: str
    """Limiting and Pagination"""

    nb_pdl_pro: str
    """Nombre de points de livraisons professionel"""

    nb_pdl_res: str
    """Nombre de points de livraisons rÃ©sidentiel"""

    nb_pdl_tot: str
    """Nombre total de points de livraisons"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    select: str
    """Filtering Columns"""

    type_reseau: str
    """type du rÃ©seau de chaleur"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
