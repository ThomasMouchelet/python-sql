

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
# QUESTION 1  👶
# Affichez les 5 premières lignes COMPLÈTES de la table restaurants
# (toutes les colonnes).
# =================================================================
def voir_restaurants():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 1 : écrivez la requête SQL
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()   # fetchall() -> toutes les lignes

    conn.close()
    return resultats


# =================================================================
# QUESTION 2  👶
# Affichez seulement le NOM des 5 premiers restaurants.
# =================================================================
def noms_restaurants():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 2 : écrivez la requête SQL
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 3  👶
# Quelles sont les VILLES différentes où habitent les utilisateurs ?
# (chaque ville ne doit apparaître qu'une seule fois)
# =================================================================
def villes_distinctes():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 3 : écrivez la requête SQL
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 4  ⭐
# Affichez le NOM, la VILLE et le TYPE DE CUISINE des 10 premiers
# restaurants.
# Colonnes attendues : name, city, cuisine_type
# =================================================================
def lister_restaurants():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 4 : écrivez la requête SQL
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 5  ⭐
# Affichez le nom et la ville de tous les restaurants dont le type
# de cuisine est 'Italien'.
# Colonnes attendues : name, city
# =================================================================
def restaurants_italiens():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 5 : écrivez la requête SQL
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 6  ⭐⭐
# Donnez les 10 restaurants les MIEUX NOTÉS (rating le plus élevé).
# Colonnes attendues : name, cuisine_type, rating
# =================================================================
def top10_restaurants_note():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 6 : écrivez la requête SQL
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 7  ⭐⭐
# Combien y a-t-il de commandes effectivement LIVRÉES
# (status = 'delivered') ? (On veut un seul nombre.)
# =================================================================
def nb_commandes_livrees():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 7 : écrivez la requête SQL
    requete = """

    """

    cur.execute(requete)
    ligne = cur.fetchone()                 # 1 ligne : (nombre,)
    resultat = ligne[0] if ligne else 0    # 0 tant que la requête est vide

    conn.close()
    return resultat


# =================================================================
# QUESTION 8  ⭐⭐
# Comptez le nombre d'utilisateurs PAR VILLE, de la ville qui
# compte le plus d'utilisateurs à celle qui en compte le moins.
# Colonnes attendues : city, nb_users
# =================================================================
def nb_users_par_ville():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 8 : écrivez la requête SQL
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 9  ⭐⭐⭐
# Pour chaque RESTAURANT, calculez son PANIER MOYEN et son CHIFFRE
# D'AFFAIRES (somme des montants) sur les commandes 'delivered'.
# Triez du CA le plus élevé au plus bas.
# Colonnes attendues : restaurant_id, panier_moyen, ca_total
# =================================================================
def stats_par_restaurant():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 9 : écrivez la requête SQL
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 10  ⭐⭐⭐
# Calculez, pour chaque utilisateur, son PANIER MOYEN (montant moyen
# des commandes 'delivered') et son NOMBRE de commandes, mais
# UNIQUEMENT sur les 60 DERNIERS JOURS.
# Triez du panier moyen le plus élevé au plus bas.
# Colonnes attendues : user_id, panier_moyen, nb_commandes
# =================================================================
def panier_moyen_par_user_60j():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 10 : écrivez la requête SQL
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 11  ⭐⭐⭐⭐
# Donnez le TOP 5 des restaurants par CHIFFRE D'AFFAIRES
# (somme des montants des commandes 'delivered'), avec le NOM et le
# TYPE DE CUISINE du restaurant.
# Colonnes attendues : name, cuisine_type, ca_total
# =================================================================
def top5_restaurants_ca():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 11 : écrivez la requête SQL
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 12  ⭐⭐⭐⭐
# Pour chaque VILLE, calculez le nombre d'utilisateurs et le
# POURCENTAGE d'abonnés 'premium'. Triez par % premium décroissant.
# Colonnes attendues : city, nb_users, pct_premium
# =================================================================
def repartition_premium_par_ville():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 12 : écrivez la requête SQL
    requete = """

    """

    cur.execute(requete)
    resultats = cur.fetchall()

    conn.close()
    return resultats


# =================================================================
# QUESTION 13  ⭐⭐⭐⭐  (SQL + Python)
# Étape SQL : récupérez toutes les campagnes.
# Étape Python : calculez le CTR (%) et le CPA (€) de chaque
# campagne, puis ne gardez QUE celles dont le CTR < 1.5 %.
#   - CTR = clicks / impressions * 100
#   - CPA = cost / conversions
# =================================================================
def campagnes_faible_ctr():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 13a : écrivez la requête SQL qui récupère
    #            campaign_id, channel, impressions, clicks, conversions, cost
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
# QUESTION 14  ⭐⭐⭐  (BONUS)
# Comptez le nombre d'événements par event_type, triés du plus
# fréquent au moins fréquent.
# Colonnes attendues : event_type, nb_evenements
# =================================================================
def funnel_evenements():
    conn = get_connexion()
    cur = conn.cursor()

    # TODO 14 : écrivez la requête SQL
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
