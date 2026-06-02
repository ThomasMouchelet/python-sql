"""
=================================================================
TP QUICKBITE - À COMPLÉTER  (version progressive 👶 → ⭐⭐⭐⭐)
Bloc B3 - Pilotage de la Donnée
=================================================================

OBJECTIF
--------
Interroger la base SQLite `quickbite.db` en Python pour répondre
à des questions business sur la plateforme de livraison QuickBite.

On commence par des requêtes ULTRA SIMPLES (lire une table),
puis on monte le niveau PETIT À PETIT :

    Q1  👶      lire une table entière (SELECT *)
    Q2  👶      lire UNE seule colonne
    Q3  👶      valeurs distinctes (DISTINCT)
    Q4  ⭐      SELECT plusieurs colonnes
    Q5  ⭐      filtre WHERE
    Q6  ⭐⭐     tri ORDER BY + LIMIT
    Q7  ⭐⭐     COUNT avec un filtre
    Q8  ⭐⭐     GROUP BY + COUNT
    Q9  ⭐⭐⭐    GROUP BY + AVG / SUM
    Q10 ⭐⭐⭐    filtre de date (60 derniers jours) + GROUP BY
    Q11 ⭐⭐⭐⭐   JOINTURE entre deux tables
    Q12 ⭐⭐⭐⭐   pourcentage avec CASE WHEN
    Q13 ⭐⭐⭐⭐   SQL + Python (calcul CTR / CPA)
    Q14 ⭐⭐⭐    BONUS : funnel d'événements

>>> VOTRE TRAVAIL : écrire vous-même les requêtes SQL <<<
    (les variables `requete` sont à compléter là où il y a # TODO)

AVANT DE COMMENCER
------------------
1. Lancez d'abord :   python seed_quickbite.py
   -> cela crée le fichier `quickbite.db`.
2. Complétez ensuite les requêtes marquées  # TODO  ci-dessous,
   DANS L'ORDRE (chaque question réutilise une notion de la précédente).
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
# QUESTION 1  👶  — Lire une table entière
# Affichez les 5 premières lignes COMPLÈTES de la table restaurants
# (toutes les colonnes).
# Indice : SELECT * FROM restaurants LIMIT 5;
#          (* = "toutes les colonnes")
# =================================================================
def voir_restaurants():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 1 : SELECT * FROM restaurants LIMIT 5
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()   # fetchall() -> toutes les lignes

    conn.close()
    return resultats


# =================================================================
# QUESTION 2  👶  — Lire UNE seule colonne
# Affichez seulement le NOM des 5 premiers restaurants.
# Indice : SELECT name FROM restaurants LIMIT 5;
# =================================================================
def noms_restaurants():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 2 : SELECT name FROM restaurants LIMIT 5
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 3  👶  — Valeurs distinctes (DISTINCT)
# Quelles sont les VILLES différentes où habitent les utilisateurs ?
# (chaque ville ne doit apparaître qu'une seule fois)
# Indice : SELECT DISTINCT city FROM users;
# =================================================================
def villes_distinctes():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 3 : SELECT DISTINCT city FROM users
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 4  ⭐  — SELECT plusieurs colonnes
# Affichez le NOM, la VILLE et le TYPE DE CUISINE des 10 premiers
# restaurants.
# Colonnes attendues : name, city, cuisine_type
# Indice : SELECT name, city, cuisine_type FROM restaurants LIMIT 10;
# =================================================================
def lister_restaurants():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 4 : SELECT name, city, cuisine_type FROM restaurants LIMIT 10
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 5  ⭐  — Filtre avec WHERE
# Affichez le nom et la ville de tous les restaurants dont le type
# de cuisine est 'Italien'.
# Colonnes attendues : name, city
# Indice : ... WHERE cuisine_type = 'Italien';
# =================================================================
def restaurants_italiens():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 5 : SELECT name, city FROM restaurants WHERE cuisine_type = 'Italien'
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 6  ⭐⭐  — Tri ORDER BY + LIMIT
# Donnez les 10 restaurants les MIEUX NOTÉS (rating le plus élevé).
# Colonnes attendues : name, cuisine_type, rating
# Indice : ... ORDER BY rating DESC LIMIT 10;
# =================================================================
def top10_restaurants_note():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 6 : SELECT ... ORDER BY rating DESC LIMIT 10
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 7  ⭐⭐  — COUNT avec un filtre
# Combien y a-t-il de commandes effectivement LIVRÉES
# (status = 'delivered') ? (On veut un seul nombre.)
# Indice : SELECT COUNT(*) FROM orders WHERE status = 'delivered';
# =================================================================
def nb_commandes_livrees():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 7 : SELECT COUNT(*) FROM orders WHERE status = 'delivered'
    requete = """

    """

    cur.execute(requete)
    ligne = cur.fetchone()                 # 1 ligne : (nombre,)
    resultat = ligne[0] if ligne else 0    # 0 tant que la requête est vide

    conn.close()
    return resultat


# =================================================================
# QUESTION 8  ⭐⭐  — GROUP BY + COUNT
# Comptez le nombre d'utilisateurs PAR VILLE, de la ville qui
# compte le plus d'utilisateurs à celle qui en compte le moins.
# Colonnes attendues : city, nb_users
# Indice : ... GROUP BY city ORDER BY nb_users DESC;
# =================================================================
def nb_users_par_ville():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 8 : SELECT city, COUNT(*) AS nb_users FROM users
    #          GROUP BY city ORDER BY nb_users DESC
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 9  ⭐⭐⭐  — GROUP BY + AVG / SUM (agrégats)
# Pour chaque RESTAURANT, calculez son PANIER MOYEN et son CHIFFRE
# D'AFFAIRES (somme des montants) sur les commandes 'delivered'.
# Triez du CA le plus élevé au plus bas.
# Colonnes attendues : restaurant_id, panier_moyen, ca_total
# Indice : AVG(amount), SUM(amount), GROUP BY restaurant_id
#          + filtre WHERE status = 'delivered'
#          (ROUND(..., 2) pour arrondir à 2 décimales)
# =================================================================
def stats_par_restaurant():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 9 : SELECT restaurant_id,
    #                 ROUND(AVG(amount), 2) AS panier_moyen,
    #                 ROUND(SUM(amount), 2) AS ca_total
    #          FROM orders
    #          WHERE status = 'delivered'
    #          GROUP BY restaurant_id
    #          ORDER BY ca_total DESC
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 10  ⭐⭐⭐  — Filtre de DATE + GROUP BY
# Calculez, pour chaque utilisateur, son PANIER MOYEN (montant moyen
# des commandes 'delivered') et son NOMBRE de commandes, mais
# UNIQUEMENT sur les 60 DERNIERS JOURS.
# Triez du panier moyen le plus élevé au plus bas.
# Colonnes attendues : user_id, panier_moyen, nb_commandes
# Indice : on reprend la Q9 mais on GROUP BY user_id et on ajoute
#          un filtre de date :  AND order_date >= date('now', '-60 days')
# =================================================================
def panier_moyen_par_user_60j():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 10 : reprenez la logique de la Q9 mais GROUP BY user_id
    #           + filtre status = 'delivered'
    #           + filtre order_date >= date('now', '-60 days')
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 11  ⭐⭐⭐⭐  — JOINTURE entre deux tables
# Donnez le TOP 5 des restaurants par CHIFFRE D'AFFAIRES
# (somme des montants des commandes 'delivered'), mais cette fois
# avec le NOM et le TYPE DE CUISINE du restaurant.
# Colonnes attendues : name, cuisine_type, ca_total
# Indice : la table orders n'a pas le nom du resto -> il faut une
#          JOINTURE :  FROM orders o JOIN restaurants r
#                        ON o.restaurant_id = r.restaurant_id
# =================================================================
def top5_restaurants_ca():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 11 : SELECT r.name, r.cuisine_type, ROUND(SUM(o.amount), 2) AS ca_total
    #           FROM orders o
    #           JOIN restaurants r ON o.restaurant_id = r.restaurant_id
    #           WHERE o.status = 'delivered'
    #           GROUP BY r.restaurant_id
    #           ORDER BY ca_total DESC
    #           LIMIT 5
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 12  ⭐⭐⭐⭐  — Pourcentage avec CASE WHEN
# Pour chaque VILLE, calculez le nombre d'utilisateurs et le
# POURCENTAGE d'abonnés 'premium'. Triez par % premium décroissant.
# Colonnes attendues : city, nb_users, pct_premium
# Indice : pour compter les premium dans un GROUP BY :
#          SUM(CASE WHEN plan_type = 'premium' THEN 1 ELSE 0 END)
#          Le pourcentage = 100.0 * premium / total
# =================================================================
def repartition_premium_par_ville():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 12 : SELECT city,
    #                  COUNT(*) AS nb_users,
    #                  ROUND(100.0 * SUM(CASE WHEN plan_type = 'premium'
    #                                         THEN 1 ELSE 0 END) / COUNT(*), 1)
    #                      AS pct_premium
    #           FROM users
    #           GROUP BY city
    #           ORDER BY pct_premium DESC
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 13  ⭐⭐⭐⭐  — SQL + Python
# Étape SQL : récupérez toutes les campagnes.
# Étape Python : calculez le CTR (%) et le CPA (€) de chaque
# campagne, puis ne gardez QUE celles dont le CTR < 1.5 %.
#   - CTR = clicks / impressions * 100
#   - CPA = cost / conversions
# (Le calcul se fait EN PYTHON, pas en SQL : c'est l'occasion de
#  voir comment SQL et Python se complètent.)
# =================================================================
def campagnes_faible_ctr():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 13a : récupérez campaign_id, channel, impressions, clicks,
    #            conversions, cost depuis marketing_campaigns
    requete = """

    """

    cur.execute(requete)
    lignes = cur.fetchall()
    conn.close()

    resultats = []
    for ligne in lignes:
        campaign_id, channel, impressions, clicks, conversions, cost = ligne

        # TODO 13b : calculez le CTR (attention à la division par zéro)
        ctr = None  # remplacez

        # TODO 13c : calculez le CPA (attention à conversions == 0)
        cpa = None  # remplacez

        # TODO 13d : ne gardez que les campagnes avec CTR < 1.5
        # if ...:
        #     resultats.append({
        #         "campaign_id": campaign_id,
        #         "channel": channel,
        #         "ctr": round(ctr, 2),
        #         "cpa": cpa,
        #     })

    return resultats


# =================================================================
# QUESTION 14  ⭐⭐⭐  — BONUS : funnel d'événements
# Comptez le nombre d'événements par event_type, triés du plus
# fréquent au moins fréquent.
# Colonnes attendues : event_type, nb_evenements
# Indice : GROUP BY event_type + COUNT(*) + ORDER BY ... DESC
# =================================================================
def funnel_evenements():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 14 : SELECT event_type, COUNT(*) AS nb_evenements
    #           FROM web_events GROUP BY event_type ORDER BY nb_evenements DESC
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

    print("\n[Q1 👶] 5 premières lignes de restaurants :")
    for ligne in voir_restaurants():
        print("   ", ligne)

    print("\n[Q2 👶] Noms de 5 restaurants :")
    for ligne in noms_restaurants():
        print("   ", ligne)

    print("\n[Q3 👶] Villes distinctes des utilisateurs :")
    for ligne in villes_distinctes():
        print("   ", ligne)

    print("\n[Q4 ⭐] 10 premiers restaurants (3 colonnes) :")
    for ligne in lister_restaurants():
        print("   ", ligne)

    print("\n[Q5 ⭐] Restaurants italiens :")
    for ligne in restaurants_italiens()[:10]:
        print("   ", ligne)

    print("\n[Q6 ⭐⭐] Top 10 restaurants par note :")
    for ligne in top10_restaurants_note():
        print("   ", ligne)

    print("\n[Q7 ⭐⭐] Nombre de commandes livrées :",
          nb_commandes_livrees())

    print("\n[Q8 ⭐⭐] Nombre d'utilisateurs par ville :")
    for ligne in nb_users_par_ville():
        print("   ", ligne)

    print("\n[Q9 ⭐⭐⭐] Stats par restaurant (5 premiers) :")
    for ligne in stats_par_restaurant()[:5]:
        print("   ", ligne)

    print("\n[Q10 ⭐⭐⭐] Panier moyen par utilisateur (60 j) — 5 premiers :")
    for ligne in panier_moyen_par_user_60j()[:5]:
        print("   ", ligne)

    print("\n[Q11 ⭐⭐⭐⭐] Top 5 restaurants par CA (avec jointure) :")
    for ligne in top5_restaurants_ca():
        print("   ", ligne)

    print("\n[Q12 ⭐⭐⭐⭐] Répartition premium par ville :")
    for ligne in repartition_premium_par_ville():
        print("   ", ligne)

    print("\n[Q13 ⭐⭐⭐⭐] Campagnes avec CTR < 1.5% :")
    for c in campagnes_faible_ctr():
        print("   ", c)

    print("\n[Q14 ⭐⭐⭐] Funnel des événements :")
    for ligne in funnel_evenements():
        print("   ", ligne)


if __name__ == "__main__":
    main()
