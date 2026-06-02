"""
=================================================================
TP QUICKBITE - À COMPLÉTER
Bloc B3 - Pilotage de la Donnée
=================================================================

OBJECTIF
--------
Interroger la base SQLite `quickbite.db` en Python pour répondre
à des questions business sur la plateforme de livraison QuickBite.

AVANT DE COMMENCER
------------------
1. Lancez d'abord :   python seed_quickbite.py
   -> cela crée le fichier `quickbite.db`.
2. Complétez ensuite les fonctions marquées  # TODO  ci-dessous.
3. Lancez ce fichier :   python tp_quickbite_a_completer.py

RÈGLES
------
- N'utilisez QUE la bibliothèque standard (sqlite3).
- Une requête SQL = une chaîne de caractères passée à cur.execute(...).
- Pensez à filtrer le statut des commandes quand c'est demandé.

RAPPEL : dates en SQLite
------------------------
Les dates sont stockées en TEXTE. Pour "les 60 derniers jours" :
    WHERE order_date >= date('now', '-60 days')
(ou date('2026-06-01', '-60 days') pour figer la date de référence)
=================================================================
"""

import sqlite3

DB_NAME = "quickbite.db"


def get_connexion():
    """Ouvre une connexion à la base SQLite."""
    return sqlite3.connect(DB_NAME)


# =================================================================
# EXEMPLE RÉSOLU (à lire pour comprendre le pattern attendu)
# =================================================================
def exemple_nb_utilisateurs():
    """Compte le nombre total d'utilisateurs. (déjà fait pour vous)"""
    conn = get_connexion()
    cur = conn.cursor()

    requete = "SELECT COUNT(*) FROM users;"
    cur.execute(requete)
    resultat = cur.fetchone()[0]   # fetchone() -> 1 ligne, [0] -> 1re colonne

    conn.close()
    return resultat


# =================================================================
# QUESTION 1 (SQL)
# Calculez, pour chaque utilisateur, son PANIER MOYEN (montant moyen
# des commandes 'delivered') et son NOMBRE de commandes sur les
# 60 DERNIERS JOURS. Triez du panier moyen le plus élevé au plus bas.
# Retournez la liste des lignes (user_id, panier_moyen, nb_commandes).
# =================================================================
def panier_moyen_par_user():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 1 : écrivez la requête SQL
    requete = """
        -- SELECT ...
        -- FROM orders
        -- WHERE ...
        -- GROUP BY ...
        -- ORDER BY ...
    """

    cur.execute(requete)
    resultats = cur.fetchall()   # fetchall() -> toutes les lignes

    conn.close()
    return resultats


# =================================================================
# QUESTION 2 (SQL + jointure)
# Donnez le TOP 5 des restaurants par CHIFFRE D'AFFAIRES
# (somme des montants des commandes 'delivered').
# Affichez : nom du restaurant, type de cuisine, CA total.
# Indice : jointure orders <-> restaurants, GROUP BY, ORDER BY, LIMIT.
# =================================================================
def top5_restaurants_ca():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 2 : écrivez la requête SQL avec une jointure
    requete = """
        -- SELECT r.name, r.cuisine_type, SUM(...) AS ca_total
        -- FROM orders o
        -- JOIN restaurants r ON ...
        -- WHERE ...
        -- GROUP BY ...
        -- ORDER BY ...
        -- LIMIT 5
    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 3 (SQL d'agrégation)
# Pour chaque VILLE, calculez le nombre d'utilisateurs et le
# pourcentage d'abonnés 'premium'.
# Astuce : SUM(CASE WHEN plan_type='premium' THEN 1 ELSE 0 END)
# =================================================================
def repartition_premium_par_ville():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 3 : écrivez la requête SQL
    requete = """
        -- SELECT city,
        --        COUNT(*) AS nb_users,
        --        ... AS pct_premium
        -- FROM users
        -- GROUP BY city
        -- ORDER BY pct_premium DESC
    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 4 (Python + SQL)
# Récupérez toutes les campagnes (campaign_id, channel, impressions,
# clicks, conversions, cost), puis EN PYTHON calculez pour chacune :
#   - le CTR (%)  = clicks / impressions * 100
#   - le CPA (€)  = cost / conversions
# Retournez la liste des campagnes dont le CTR < 1.5 %,
# sous forme de dictionnaires.
# =================================================================
def campagnes_faible_ctr():
    conn = get_connexion()
    cur = conn.cursor()

    cur.execute("""
        SELECT campaign_id, channel, impressions, clicks, conversions, cost
        FROM marketing_campaigns;
    """)
    lignes = cur.fetchall()
    conn.close()

    resultats = []
    for ligne in lignes:
        campaign_id, channel, impressions, clicks, conversions, cost = ligne

        # TODO 4a : calculez le CTR (attention à la division par zéro)
        ctr = None  # remplacez

        # TODO 4b : calculez le CPA (attention à conversions == 0)
        cpa = None  # remplacez

        # TODO 4c : ne gardez que les campagnes avec CTR < 1.5
        # if ...:
        #     resultats.append({...})

    return resultats


# =================================================================
# QUESTION 5 (BONUS - funnel)
# Comptez le nombre d'événements par event_type, triés du plus
# fréquent au moins fréquent, pour visualiser le funnel.
# =================================================================
def funnel_evenements():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 5 : écrivez la requête SQL
    requete = """
        -- SELECT event_type, COUNT(*) ...
    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# PROGRAMME PRINCIPAL — affiche les résultats
# =================================================================
def main():
    print("=" * 55)
    print("TP QUICKBITE - Résultats")
    print("=" * 55)

    print("\n[Exemple] Nombre d'utilisateurs :",
          exemple_nb_utilisateurs())

    print("\n[Q1] Panier moyen par utilisateur (60 j) — 5 premiers :")
    for ligne in panier_moyen_par_user()[:5]:
        print("   ", ligne)

    print("\n[Q2] Top 5 restaurants par CA :")
    for ligne in top5_restaurants_ca():
        print("   ", ligne)

    print("\n[Q3] Répartition premium par ville :")
    for ligne in repartition_premium_par_ville():
        print("   ", ligne)

    print("\n[Q4] Campagnes avec CTR < 1.5% :")
    for c in campagnes_faible_ctr():
        print("   ", c)

    print("\n[Q5] Funnel des événements :")
    for ligne in funnel_evenements():
        print("   ", ligne)


if __name__ == "__main__":
    main()
