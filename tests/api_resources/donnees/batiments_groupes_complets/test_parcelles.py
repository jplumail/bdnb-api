# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bdnb_api import BdnbAPI, AsyncBdnbAPI
from tests.utils import assert_matches_type
from bdnb_api.types.donnees.batiments_groupes_complets import ParcelleListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParcelles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BdnbAPI) -> None:
        parcelle = client.donnees.batiments_groupes_complets.parcelles.list()
        assert_matches_type(ParcelleListResponse, parcelle, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BdnbAPI) -> None:
        parcelle = client.donnees.batiments_groupes_complets.parcelles.list(
            alea_argiles="alea_argiles",
            alea_radon="alea_radon",
            altitude_sol_mean="altitude_sol_mean",
            annee_construction="annee_construction",
            arrete_2021="arrete_2021",
            batiment_groupe_id="batiment_groupe_id",
            chauffage_solaire="chauffage_solaire",
            classe_bilan_dpe="classe_bilan_dpe",
            classe_conso_energie_arrete_2012="classe_conso_energie_arrete_2012",
            classe_inertie="classe_inertie",
            cle_interop_adr_principale_ban="cle_interop_adr_principale_ban",
            code_commune_insee="code_commune_insee",
            code_departement_insee="code_departement_insee",
            code_epci_insee="code_epci_insee",
            code_iris="code_iris",
            code_qp="code_qp",
            code_region_insee="code_region_insee",
            conso_3_usages_ep_m2_arrete_2012="conso_3_usages_ep_m2_arrete_2012",
            conso_5_usages_ep_m2="conso_5_usages_ep_m2",
            conso_pro_dle_elec_2020="conso_pro_dle_elec_2020",
            conso_pro_dle_gaz_2020="conso_pro_dle_gaz_2020",
            conso_res_dle_elec_2020="conso_res_dle_elec_2020",
            conso_res_dle_gaz_2020="conso_res_dle_gaz_2020",
            contient_fictive_geom_groupe="contient_fictive_geom_groupe",
            croisement_geospx_reussi="croisement_geospx_reussi",
            date_reception_dpe="date_reception_dpe",
            difference_rel_valeur_fonciere_etat_initial_renove_categorie="difference_rel_valeur_fonciere_etat_initial_renove_categorie",
            distance_batiment_historique_plus_proche="distance_batiment_historique_plus_proche",
            ecs_solaire="ecs_solaire",
            emission_ges_3_usages_ep_m2_arrete_2012="emission_ges_3_usages_ep_m2_arrete_2012",
            emission_ges_5_usages_m2="emission_ges_5_usages_m2",
            epaisseur_lame="epaisseur_lame",
            etat_initial_consommation_energie_estim_inc="etat_initial_consommation_energie_estim_inc",
            etat_initial_consommation_energie_estim_lower="etat_initial_consommation_energie_estim_lower",
            etat_initial_consommation_energie_estim_mean="etat_initial_consommation_energie_estim_mean",
            etat_initial_consommation_energie_estim_upper="etat_initial_consommation_energie_estim_upper",
            etat_initial_consommation_energie_primaire_estim_lower="etat_initial_consommation_energie_primaire_estim_lower",
            etat_initial_consommation_energie_primaire_estim_mean="etat_initial_consommation_energie_primaire_estim_mean",
            etat_initial_consommation_energie_primaire_estim_upper="etat_initial_consommation_energie_primaire_estim_upper",
            etat_initial_consommation_ges_estim_inc="etat_initial_consommation_ges_estim_inc",
            etat_initial_ges_estim_lower="etat_initial_ges_estim_lower",
            etat_initial_ges_estim_mean="etat_initial_ges_estim_mean",
            etat_initial_ges_estim_upper="etat_initial_ges_estim_upper",
            etat_initial_risque_canicule="etat_initial_risque_canicule",
            etat_initial_risque_canicule_inc="etat_initial_risque_canicule_inc",
            etat_renove_consommation_energie_estim_inc="etat_renove_consommation_energie_estim_inc",
            etat_renove_consommation_energie_estim_lower="etat_renove_consommation_energie_estim_lower",
            etat_renove_consommation_energie_estim_mean="etat_renove_consommation_energie_estim_mean",
            etat_renove_consommation_energie_estim_upper="etat_renove_consommation_energie_estim_upper",
            etat_renove_consommation_energie_primaire_estim_lower="etat_renove_consommation_energie_primaire_estim_lower",
            etat_renove_consommation_energie_primaire_estim_mean="etat_renove_consommation_energie_primaire_estim_mean",
            etat_renove_consommation_energie_primaire_estim_upper="etat_renove_consommation_energie_primaire_estim_upper",
            etat_renove_consommation_ges_estim_inc="etat_renove_consommation_ges_estim_inc",
            etat_renove_ges_estim_lower="etat_renove_ges_estim_lower",
            etat_renove_ges_estim_mean="etat_renove_ges_estim_mean",
            etat_renove_ges_estim_upper="etat_renove_ges_estim_upper",
            etat_renove_risque_canicule="etat_renove_risque_canicule",
            etat_renove_risque_canicule_inc="etat_renove_risque_canicule_inc",
            etiquette_dpe_initial_a="etiquette_dpe_initial_a",
            etiquette_dpe_initial_b="etiquette_dpe_initial_b",
            etiquette_dpe_initial_c="etiquette_dpe_initial_c",
            etiquette_dpe_initial_d="etiquette_dpe_initial_d",
            etiquette_dpe_initial_e="etiquette_dpe_initial_e",
            etiquette_dpe_initial_f="etiquette_dpe_initial_f",
            etiquette_dpe_initial_g="etiquette_dpe_initial_g",
            etiquette_dpe_initial_inc="etiquette_dpe_initial_inc",
            etiquette_dpe_initial_map="etiquette_dpe_initial_map",
            etiquette_dpe_initial_map_2nd="etiquette_dpe_initial_map_2nd",
            etiquette_dpe_initial_map_2nd_prob="etiquette_dpe_initial_map_2nd_prob",
            etiquette_dpe_renove_a="etiquette_dpe_renove_a",
            etiquette_dpe_renove_b="etiquette_dpe_renove_b",
            etiquette_dpe_renove_c="etiquette_dpe_renove_c",
            etiquette_dpe_renove_d="etiquette_dpe_renove_d",
            etiquette_dpe_renove_e="etiquette_dpe_renove_e",
            etiquette_dpe_renove_f="etiquette_dpe_renove_f",
            etiquette_dpe_renove_g="etiquette_dpe_renove_g",
            etiquette_dpe_renove_inc="etiquette_dpe_renove_inc",
            etiquette_dpe_renove_map="etiquette_dpe_renove_map",
            etiquette_dpe_renove_map_2nd="etiquette_dpe_renove_map_2nd",
            etiquette_dpe_renove_map_2nd_prob="etiquette_dpe_renove_map_2nd_prob",
            etiquette_dpe_synthese_particulier_simple="etiquette_dpe_synthese_particulier_simple",
            etiquette_dpe_synthese_particulier_source="etiquette_dpe_synthese_particulier_source",
            facteur_solaire_baie_vitree="facteur_solaire_baie_vitree",
            fiabilite_cr_adr_niv_1="fiabilite_cr_adr_niv_1",
            fiabilite_cr_adr_niv_2="fiabilite_cr_adr_niv_2",
            fiabilite_emprise_sol="fiabilite_emprise_sol",
            fiabilite_hauteur="fiabilite_hauteur",
            geom_groupe="geom_groupe",
            gisement_gain_conso_finale_total="gisement_gain_conso_finale_total",
            gisement_gain_energetique_mean="gisement_gain_energetique_mean",
            gisement_gain_ges_mean="gisement_gain_ges_mean",
            hauteur_mean="hauteur_mean",
            identifiant_dpe="identifiant_dpe",
            l_cle_interop_adr="l_cle_interop_adr",
            l_denomination_proprietaire="l_denomination_proprietaire",
            l_libelle_adr="l_libelle_adr",
            l_orientation_baie_vitree="l_orientation_baie_vitree",
            l_parcelle_id="l_parcelle_id",
            l_siren="l_siren",
            l_type_generateur_chauffage="l_type_generateur_chauffage",
            l_type_generateur_ecs="l_type_generateur_ecs",
            libelle_adr_principale_ban="libelle_adr_principale_ban",
            libelle_commune_insee="libelle_commune_insee",
            limit="limit",
            mat_mur_txt="mat_mur_txt",
            mat_toit_txt="mat_toit_txt",
            materiaux_structure_mur_exterieur="materiaux_structure_mur_exterieur",
            materiaux_structure_mur_exterieur_simplifie="materiaux_structure_mur_exterieur_simplifie",
            materiaux_toiture_simplifie="materiaux_toiture_simplifie",
            nb_adresse_valid_ban="nb_adresse_valid_ban",
            nb_classe_bilan_dpe_a="nb_classe_bilan_dpe_a",
            nb_classe_bilan_dpe_b="nb_classe_bilan_dpe_b",
            nb_classe_bilan_dpe_c="nb_classe_bilan_dpe_c",
            nb_classe_bilan_dpe_d="nb_classe_bilan_dpe_d",
            nb_classe_bilan_dpe_e="nb_classe_bilan_dpe_e",
            nb_classe_bilan_dpe_f="nb_classe_bilan_dpe_f",
            nb_classe_bilan_dpe_g="nb_classe_bilan_dpe_g",
            nb_classe_conso_energie_arrete_2012_a="nb_classe_conso_energie_arrete_2012_a",
            nb_classe_conso_energie_arrete_2012_b="nb_classe_conso_energie_arrete_2012_b",
            nb_classe_conso_energie_arrete_2012_c="nb_classe_conso_energie_arrete_2012_c",
            nb_classe_conso_energie_arrete_2012_d="nb_classe_conso_energie_arrete_2012_d",
            nb_classe_conso_energie_arrete_2012_e="nb_classe_conso_energie_arrete_2012_e",
            nb_classe_conso_energie_arrete_2012_f="nb_classe_conso_energie_arrete_2012_f",
            nb_classe_conso_energie_arrete_2012_g="nb_classe_conso_energie_arrete_2012_g",
            nb_classe_conso_energie_arrete_2012_nc="nb_classe_conso_energie_arrete_2012_nc",
            nb_log="nb_log",
            nb_log_rnc="nb_log_rnc",
            nb_lot_garpark_rnc="nb_lot_garpark_rnc",
            nb_lot_tertiaire_rnc="nb_lot_tertiaire_rnc",
            nb_niveau="nb_niveau",
            nb_pdl_pro_dle_elec_2020="nb_pdl_pro_dle_elec_2020",
            nb_pdl_pro_dle_gaz_2020="nb_pdl_pro_dle_gaz_2020",
            nb_pdl_res_dle_elec_2020="nb_pdl_res_dle_elec_2020",
            nb_pdl_res_dle_gaz_2020="nb_pdl_res_dle_gaz_2020",
            nom_batiment_historique_plus_proche="nom_batiment_historique_plus_proche",
            nom_qp="nom_qp",
            nom_quartier_qpv="nom_quartier_qpv",
            numero_immat_principal="numero_immat_principal",
            offset="offset",
            order="order",
            parcelle_id="parcelle_id",
            pourcentage_surface_baie_vitree_exterieur="pourcentage_surface_baie_vitree_exterieur",
            presence_balcon="presence_balcon",
            quartier_prioritaire="quartier_prioritaire",
            s_geom_groupe="s_geom_groupe",
            select="select",
            surface_emprise_sol="surface_emprise_sol",
            surface_facade_ext="surface_facade_ext",
            surface_facade_mitoyenne="surface_facade_mitoyenne",
            surface_facade_totale="surface_facade_totale",
            surface_facade_vitree="surface_facade_vitree",
            traversant="traversant",
            type_dpe="type_dpe",
            type_energie_chauffage="type_energie_chauffage",
            type_energie_chauffage_appoint="type_energie_chauffage_appoint",
            type_fermeture="type_fermeture",
            type_gaz_lame="type_gaz_lame",
            type_generateur_chauffage="type_generateur_chauffage",
            type_generateur_chauffage_anciennete="type_generateur_chauffage_anciennete",
            type_generateur_chauffage_anciennete_appoint="type_generateur_chauffage_anciennete_appoint",
            type_generateur_chauffage_appoint="type_generateur_chauffage_appoint",
            type_generateur_climatisation="type_generateur_climatisation",
            type_generateur_climatisation_anciennete="type_generateur_climatisation_anciennete",
            type_generateur_ecs="type_generateur_ecs",
            type_generateur_ecs_anciennete="type_generateur_ecs_anciennete",
            type_installation_chauffage="type_installation_chauffage",
            type_installation_ecs="type_installation_ecs",
            type_isolation_mur_exterieur="type_isolation_mur_exterieur",
            type_isolation_plancher_bas="type_isolation_plancher_bas",
            type_isolation_plancher_haut="type_isolation_plancher_haut",
            type_materiaux_menuiserie="type_materiaux_menuiserie",
            type_plancher_bas_deperditif="type_plancher_bas_deperditif",
            type_plancher_haut_deperditif="type_plancher_haut_deperditif",
            type_production_energie_renouvelable="type_production_energie_renouvelable",
            type_ventilation="type_ventilation",
            type_vitrage="type_vitrage",
            u_baie_vitree="u_baie_vitree",
            u_mur_exterieur="u_mur_exterieur",
            u_plancher_bas_final_deperditif="u_plancher_bas_final_deperditif",
            u_plancher_haut_deperditif="u_plancher_haut_deperditif",
            usage_niveau_1_txt="usage_niveau_1_txt",
            valeur_fonciere_etat_initial_incertitude="valeur_fonciere_etat_initial_incertitude",
            vitrage_vir="vitrage_vir",
            volume_brut="volume_brut",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(ParcelleListResponse, parcelle, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BdnbAPI) -> None:
        response = client.donnees.batiments_groupes_complets.parcelles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcelle = response.parse()
        assert_matches_type(ParcelleListResponse, parcelle, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BdnbAPI) -> None:
        with client.donnees.batiments_groupes_complets.parcelles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcelle = response.parse()
            assert_matches_type(ParcelleListResponse, parcelle, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncParcelles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncBdnbAPI) -> None:
        parcelle = await async_client.donnees.batiments_groupes_complets.parcelles.list()
        assert_matches_type(ParcelleListResponse, parcelle, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBdnbAPI) -> None:
        parcelle = await async_client.donnees.batiments_groupes_complets.parcelles.list(
            alea_argiles="alea_argiles",
            alea_radon="alea_radon",
            altitude_sol_mean="altitude_sol_mean",
            annee_construction="annee_construction",
            arrete_2021="arrete_2021",
            batiment_groupe_id="batiment_groupe_id",
            chauffage_solaire="chauffage_solaire",
            classe_bilan_dpe="classe_bilan_dpe",
            classe_conso_energie_arrete_2012="classe_conso_energie_arrete_2012",
            classe_inertie="classe_inertie",
            cle_interop_adr_principale_ban="cle_interop_adr_principale_ban",
            code_commune_insee="code_commune_insee",
            code_departement_insee="code_departement_insee",
            code_epci_insee="code_epci_insee",
            code_iris="code_iris",
            code_qp="code_qp",
            code_region_insee="code_region_insee",
            conso_3_usages_ep_m2_arrete_2012="conso_3_usages_ep_m2_arrete_2012",
            conso_5_usages_ep_m2="conso_5_usages_ep_m2",
            conso_pro_dle_elec_2020="conso_pro_dle_elec_2020",
            conso_pro_dle_gaz_2020="conso_pro_dle_gaz_2020",
            conso_res_dle_elec_2020="conso_res_dle_elec_2020",
            conso_res_dle_gaz_2020="conso_res_dle_gaz_2020",
            contient_fictive_geom_groupe="contient_fictive_geom_groupe",
            croisement_geospx_reussi="croisement_geospx_reussi",
            date_reception_dpe="date_reception_dpe",
            difference_rel_valeur_fonciere_etat_initial_renove_categorie="difference_rel_valeur_fonciere_etat_initial_renove_categorie",
            distance_batiment_historique_plus_proche="distance_batiment_historique_plus_proche",
            ecs_solaire="ecs_solaire",
            emission_ges_3_usages_ep_m2_arrete_2012="emission_ges_3_usages_ep_m2_arrete_2012",
            emission_ges_5_usages_m2="emission_ges_5_usages_m2",
            epaisseur_lame="epaisseur_lame",
            etat_initial_consommation_energie_estim_inc="etat_initial_consommation_energie_estim_inc",
            etat_initial_consommation_energie_estim_lower="etat_initial_consommation_energie_estim_lower",
            etat_initial_consommation_energie_estim_mean="etat_initial_consommation_energie_estim_mean",
            etat_initial_consommation_energie_estim_upper="etat_initial_consommation_energie_estim_upper",
            etat_initial_consommation_energie_primaire_estim_lower="etat_initial_consommation_energie_primaire_estim_lower",
            etat_initial_consommation_energie_primaire_estim_mean="etat_initial_consommation_energie_primaire_estim_mean",
            etat_initial_consommation_energie_primaire_estim_upper="etat_initial_consommation_energie_primaire_estim_upper",
            etat_initial_consommation_ges_estim_inc="etat_initial_consommation_ges_estim_inc",
            etat_initial_ges_estim_lower="etat_initial_ges_estim_lower",
            etat_initial_ges_estim_mean="etat_initial_ges_estim_mean",
            etat_initial_ges_estim_upper="etat_initial_ges_estim_upper",
            etat_initial_risque_canicule="etat_initial_risque_canicule",
            etat_initial_risque_canicule_inc="etat_initial_risque_canicule_inc",
            etat_renove_consommation_energie_estim_inc="etat_renove_consommation_energie_estim_inc",
            etat_renove_consommation_energie_estim_lower="etat_renove_consommation_energie_estim_lower",
            etat_renove_consommation_energie_estim_mean="etat_renove_consommation_energie_estim_mean",
            etat_renove_consommation_energie_estim_upper="etat_renove_consommation_energie_estim_upper",
            etat_renove_consommation_energie_primaire_estim_lower="etat_renove_consommation_energie_primaire_estim_lower",
            etat_renove_consommation_energie_primaire_estim_mean="etat_renove_consommation_energie_primaire_estim_mean",
            etat_renove_consommation_energie_primaire_estim_upper="etat_renove_consommation_energie_primaire_estim_upper",
            etat_renove_consommation_ges_estim_inc="etat_renove_consommation_ges_estim_inc",
            etat_renove_ges_estim_lower="etat_renove_ges_estim_lower",
            etat_renove_ges_estim_mean="etat_renove_ges_estim_mean",
            etat_renove_ges_estim_upper="etat_renove_ges_estim_upper",
            etat_renove_risque_canicule="etat_renove_risque_canicule",
            etat_renove_risque_canicule_inc="etat_renove_risque_canicule_inc",
            etiquette_dpe_initial_a="etiquette_dpe_initial_a",
            etiquette_dpe_initial_b="etiquette_dpe_initial_b",
            etiquette_dpe_initial_c="etiquette_dpe_initial_c",
            etiquette_dpe_initial_d="etiquette_dpe_initial_d",
            etiquette_dpe_initial_e="etiquette_dpe_initial_e",
            etiquette_dpe_initial_f="etiquette_dpe_initial_f",
            etiquette_dpe_initial_g="etiquette_dpe_initial_g",
            etiquette_dpe_initial_inc="etiquette_dpe_initial_inc",
            etiquette_dpe_initial_map="etiquette_dpe_initial_map",
            etiquette_dpe_initial_map_2nd="etiquette_dpe_initial_map_2nd",
            etiquette_dpe_initial_map_2nd_prob="etiquette_dpe_initial_map_2nd_prob",
            etiquette_dpe_renove_a="etiquette_dpe_renove_a",
            etiquette_dpe_renove_b="etiquette_dpe_renove_b",
            etiquette_dpe_renove_c="etiquette_dpe_renove_c",
            etiquette_dpe_renove_d="etiquette_dpe_renove_d",
            etiquette_dpe_renove_e="etiquette_dpe_renove_e",
            etiquette_dpe_renove_f="etiquette_dpe_renove_f",
            etiquette_dpe_renove_g="etiquette_dpe_renove_g",
            etiquette_dpe_renove_inc="etiquette_dpe_renove_inc",
            etiquette_dpe_renove_map="etiquette_dpe_renove_map",
            etiquette_dpe_renove_map_2nd="etiquette_dpe_renove_map_2nd",
            etiquette_dpe_renove_map_2nd_prob="etiquette_dpe_renove_map_2nd_prob",
            etiquette_dpe_synthese_particulier_simple="etiquette_dpe_synthese_particulier_simple",
            etiquette_dpe_synthese_particulier_source="etiquette_dpe_synthese_particulier_source",
            facteur_solaire_baie_vitree="facteur_solaire_baie_vitree",
            fiabilite_cr_adr_niv_1="fiabilite_cr_adr_niv_1",
            fiabilite_cr_adr_niv_2="fiabilite_cr_adr_niv_2",
            fiabilite_emprise_sol="fiabilite_emprise_sol",
            fiabilite_hauteur="fiabilite_hauteur",
            geom_groupe="geom_groupe",
            gisement_gain_conso_finale_total="gisement_gain_conso_finale_total",
            gisement_gain_energetique_mean="gisement_gain_energetique_mean",
            gisement_gain_ges_mean="gisement_gain_ges_mean",
            hauteur_mean="hauteur_mean",
            identifiant_dpe="identifiant_dpe",
            l_cle_interop_adr="l_cle_interop_adr",
            l_denomination_proprietaire="l_denomination_proprietaire",
            l_libelle_adr="l_libelle_adr",
            l_orientation_baie_vitree="l_orientation_baie_vitree",
            l_parcelle_id="l_parcelle_id",
            l_siren="l_siren",
            l_type_generateur_chauffage="l_type_generateur_chauffage",
            l_type_generateur_ecs="l_type_generateur_ecs",
            libelle_adr_principale_ban="libelle_adr_principale_ban",
            libelle_commune_insee="libelle_commune_insee",
            limit="limit",
            mat_mur_txt="mat_mur_txt",
            mat_toit_txt="mat_toit_txt",
            materiaux_structure_mur_exterieur="materiaux_structure_mur_exterieur",
            materiaux_structure_mur_exterieur_simplifie="materiaux_structure_mur_exterieur_simplifie",
            materiaux_toiture_simplifie="materiaux_toiture_simplifie",
            nb_adresse_valid_ban="nb_adresse_valid_ban",
            nb_classe_bilan_dpe_a="nb_classe_bilan_dpe_a",
            nb_classe_bilan_dpe_b="nb_classe_bilan_dpe_b",
            nb_classe_bilan_dpe_c="nb_classe_bilan_dpe_c",
            nb_classe_bilan_dpe_d="nb_classe_bilan_dpe_d",
            nb_classe_bilan_dpe_e="nb_classe_bilan_dpe_e",
            nb_classe_bilan_dpe_f="nb_classe_bilan_dpe_f",
            nb_classe_bilan_dpe_g="nb_classe_bilan_dpe_g",
            nb_classe_conso_energie_arrete_2012_a="nb_classe_conso_energie_arrete_2012_a",
            nb_classe_conso_energie_arrete_2012_b="nb_classe_conso_energie_arrete_2012_b",
            nb_classe_conso_energie_arrete_2012_c="nb_classe_conso_energie_arrete_2012_c",
            nb_classe_conso_energie_arrete_2012_d="nb_classe_conso_energie_arrete_2012_d",
            nb_classe_conso_energie_arrete_2012_e="nb_classe_conso_energie_arrete_2012_e",
            nb_classe_conso_energie_arrete_2012_f="nb_classe_conso_energie_arrete_2012_f",
            nb_classe_conso_energie_arrete_2012_g="nb_classe_conso_energie_arrete_2012_g",
            nb_classe_conso_energie_arrete_2012_nc="nb_classe_conso_energie_arrete_2012_nc",
            nb_log="nb_log",
            nb_log_rnc="nb_log_rnc",
            nb_lot_garpark_rnc="nb_lot_garpark_rnc",
            nb_lot_tertiaire_rnc="nb_lot_tertiaire_rnc",
            nb_niveau="nb_niveau",
            nb_pdl_pro_dle_elec_2020="nb_pdl_pro_dle_elec_2020",
            nb_pdl_pro_dle_gaz_2020="nb_pdl_pro_dle_gaz_2020",
            nb_pdl_res_dle_elec_2020="nb_pdl_res_dle_elec_2020",
            nb_pdl_res_dle_gaz_2020="nb_pdl_res_dle_gaz_2020",
            nom_batiment_historique_plus_proche="nom_batiment_historique_plus_proche",
            nom_qp="nom_qp",
            nom_quartier_qpv="nom_quartier_qpv",
            numero_immat_principal="numero_immat_principal",
            offset="offset",
            order="order",
            parcelle_id="parcelle_id",
            pourcentage_surface_baie_vitree_exterieur="pourcentage_surface_baie_vitree_exterieur",
            presence_balcon="presence_balcon",
            quartier_prioritaire="quartier_prioritaire",
            s_geom_groupe="s_geom_groupe",
            select="select",
            surface_emprise_sol="surface_emprise_sol",
            surface_facade_ext="surface_facade_ext",
            surface_facade_mitoyenne="surface_facade_mitoyenne",
            surface_facade_totale="surface_facade_totale",
            surface_facade_vitree="surface_facade_vitree",
            traversant="traversant",
            type_dpe="type_dpe",
            type_energie_chauffage="type_energie_chauffage",
            type_energie_chauffage_appoint="type_energie_chauffage_appoint",
            type_fermeture="type_fermeture",
            type_gaz_lame="type_gaz_lame",
            type_generateur_chauffage="type_generateur_chauffage",
            type_generateur_chauffage_anciennete="type_generateur_chauffage_anciennete",
            type_generateur_chauffage_anciennete_appoint="type_generateur_chauffage_anciennete_appoint",
            type_generateur_chauffage_appoint="type_generateur_chauffage_appoint",
            type_generateur_climatisation="type_generateur_climatisation",
            type_generateur_climatisation_anciennete="type_generateur_climatisation_anciennete",
            type_generateur_ecs="type_generateur_ecs",
            type_generateur_ecs_anciennete="type_generateur_ecs_anciennete",
            type_installation_chauffage="type_installation_chauffage",
            type_installation_ecs="type_installation_ecs",
            type_isolation_mur_exterieur="type_isolation_mur_exterieur",
            type_isolation_plancher_bas="type_isolation_plancher_bas",
            type_isolation_plancher_haut="type_isolation_plancher_haut",
            type_materiaux_menuiserie="type_materiaux_menuiserie",
            type_plancher_bas_deperditif="type_plancher_bas_deperditif",
            type_plancher_haut_deperditif="type_plancher_haut_deperditif",
            type_production_energie_renouvelable="type_production_energie_renouvelable",
            type_ventilation="type_ventilation",
            type_vitrage="type_vitrage",
            u_baie_vitree="u_baie_vitree",
            u_mur_exterieur="u_mur_exterieur",
            u_plancher_bas_final_deperditif="u_plancher_bas_final_deperditif",
            u_plancher_haut_deperditif="u_plancher_haut_deperditif",
            usage_niveau_1_txt="usage_niveau_1_txt",
            valeur_fonciere_etat_initial_incertitude="valeur_fonciere_etat_initial_incertitude",
            vitrage_vir="vitrage_vir",
            volume_brut="volume_brut",
            prefer="count=none",
            range="Range",
            range_unit="Range-Unit",
        )
        assert_matches_type(ParcelleListResponse, parcelle, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBdnbAPI) -> None:
        response = await async_client.donnees.batiments_groupes_complets.parcelles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parcelle = await response.parse()
        assert_matches_type(ParcelleListResponse, parcelle, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBdnbAPI) -> None:
        async with async_client.donnees.batiments_groupes_complets.parcelles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parcelle = await response.parse()
            assert_matches_type(ParcelleListResponse, parcelle, path=["response"])

        assert cast(Any, response.is_closed) is True
