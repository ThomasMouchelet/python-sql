"""
=================================================================
TP QUICKBITE - À COMPLÉTER
Bloc B3 - Pilotage de la Donnée
=================================================================

OBJECTIF
--------
Interroger la base SQLite `quickbite.db` en Python pour répondre
à des questions business sur la plateforme de livraison QuickBite.

>>> VOTRE TRAVAIL : écrire vous-même les requêtes SQL <<<
    (les variables `requete` contiennent une chaîne vide à compléter)

AVANT DE COMMENCER
------------------
1. Lancez d'abord :   python seed_quickbite.py
   -> cela crée le fichier `quickbite.db`.
2. Complétez ensuite les requêtes SQL marquées  # TODO  ci-dessous.
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

RAPPEL : structure des tables
-----------------------------
users(user_id, signup_date, city, device_type, plan_type, monthly_fee)
restaurants(restaurant_id, name, city, cuisine_type, rating)
orders(order_id, user_id, restaurant_id, order_date, amount,
       delivery_time_minutes, status)   -- status: delivered/cancelled/refunded
web_events(event_id, user_id, event_type, session_id, timestamp)
marketing_campaigns(campaign_id, channel, impressions, clicks,
                    conversions, cost)
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
# QUESTION 1
# Calculez, pour chaque utilisateur, son PANIER MOYEN (montant moyen
# des commandes 'delivered') et son NOMBRE de commandes sur les
# 60 DERNIERS JOURS. Triez du panier moyen le plus élevé au plus bas.
# Colonnes attendues : user_id, panier_moyen, nb_commandes
# =================================================================
def panier_moyen_par_user():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 1 : écrivez la requête SQL complète
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()   # fetchall() -> toutes les lignes

    conn.close()
    return resultats


# =================================================================
# QUESTION 2
# Donnez le TOP 5 des restaurants par CHIFFRE D'AFFAIRES
# (somme des montants des commandes 'delivered').
# Colonnes attendues : name, cuisine_type, ca_total
# (Indice : il faut une jointure entre orders et restaurants.)
# =================================================================
def top5_restaurants_ca():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 2 : écrivez la requête SQL complète (avec jointure)
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 3
# Pour chaque VILLE, calculez le nombre d'utilisateurs et le
# pourcentage d'abonnés 'premium'. Triez par % premium décroissant.
# Colonnes attendues : city, nb_users, pct_premium
# =================================================================
def repartition_premium_par_ville():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 3 : écrivez la requête SQL complète
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 4 (Python + SQL)
# Étape SQL : récupérez toutes les campagnes.
# Étape Python : calculez CTR (%) et CPA (€), gardez celles
# dont le CTR < 1.5 %.
#   - CTR = clicks / impressions * 100
#   - CPA = cost / conversions
# =================================================================
def campagnes_faible_ctr():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 4a : écrivez la requête SQL qui récupère
    #           campaign_id, channel, impressions, clicks, conversions, cost
    requete = """

    """

    cur.execute(requete)
    lignes = cur.fetchall()
    conn.close()

    resultats = []
    for ligne in lignes:
        campaign_id, channel, impressions, clicks, conversions, cost = ligne

        # TODO 4b : calculez le CTR (attention à la division par zéro)
        ctr = None  # remplacez

        # TODO 4c : calculez le CPA (attention à conversions == 0)
        cpa = None  # remplacez

        # TODO 4d : ne gardez que les campagnes avec CTR < 1.5
        # if ...:
        #     resultats.append({...})

    return resultats


# =================================================================
# QUESTION 5 (BONUS - funnel)
# Comptez le nombre d'événements par event_type, triés du plus
# fréquent au moins fréquent.
# Colonnes attendues : event_type, nb_evenements
# =================================================================
def funnel_evenements():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 5 : écrivez la requête SQL complète
    requete = """

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
