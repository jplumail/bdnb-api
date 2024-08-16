# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatimentGroupeSimulationsValeurVerteListParams"]


class BatimentGroupeSimulationsValeurVerteListParams(TypedDict, total=False):
    batiment_groupe_id: str
    """Identifiant du groupe de bÃ¢timent au sens de la BDNB"""

    code_departement_insee: str
    """Code dÃ©partement INSEE"""

    gain_classe_b_vers_a: float
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE B vers A.
    """

    gain_classe_c_vers_a: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE C vers A.
    """

    gain_classe_c_vers_b: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE C vers B.
    """

    gain_classe_d_vers_a: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE D vers A.
    """

    gain_classe_d_vers_b: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE D vers B.
    """

    gain_classe_d_vers_c: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE D vers C.
    """

    gain_classe_e_vers_a: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE E vers A.
    """

    gain_classe_e_vers_b: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE E vers B.
    """

    gain_classe_e_vers_c: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE E vers C.
    """

    gain_classe_e_vers_d: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE E vers D.
    """

    gain_classe_f_vers_a: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE F vers A.
    """

    gain_classe_f_vers_b: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE F vers B.
    """

    gain_classe_f_vers_c: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE F vers C.
    """

    gain_classe_f_vers_d: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE F vers D.
    """

    gain_classe_f_vers_e: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE F vers E.
    """

    gain_classe_g_vers_a: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE G vers A.
    """

    gain_classe_g_vers_b: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE G vers B.
    """

    gain_classe_g_vers_c: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE G vers C.
    """

    gain_classe_g_vers_d: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE G vers D.
    """

    gain_classe_g_vers_e: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE G vers E.
    """

    gain_classe_g_vers_f: object
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule le changement
    de DPE G vers F.
    """

    limit: str
    """Limiting and Pagination"""

    offset: str
    """Limiting and Pagination"""

    order: str
    """Ordering"""

    renovation: float
    """
    (simulations) gain en % de la valeur immobiliÃ¨re lorsqu'on simule une
    rÃ©novation.
    """

    select: str
    """Filtering Columns"""

    prefer: Annotated[Literal["count=none"], PropertyInfo(alias="Prefer")]

    range: Annotated[str, PropertyInfo(alias="Range")]

    range_unit: Annotated[str, PropertyInfo(alias="Range-Unit")]
