"""
seed_quickbite.py
=================================================================
Crée la base SQLite `quickbite.db` et la remplit de fausses données
(seed) pour le TP du Bloc B3 - Pilotage de la Donnée.

Usage :
    python seed_quickbite.py

Aucune installation requise : sqlite3, random et datetime sont
inclus dans Python.

Le script est IDEMPOTENT : il supprime et recrée les tables à
chaque exécution, et utilise une graine aléatoire fixe (random.seed)
pour que tous les étudiants obtiennent EXACTEMENT les mêmes données.
=================================================================
"""

import sqlite3
import random
from datetime import datetime, timedelta

# Graine fixe -> données identiques pour tout le monde (reproductibilité)
random.seed(42)

DB_NAME = "quickbite.db"

# Date "actuelle" simulée pour générer des dates cohérentes
TODAY = datetime(2026, 6, 1)

# --- Volumes générés -------------------------------------------------
NB_USERS = 500
NB_RESTAURANTS = 60
NB_ORDERS = 4000
NB_WEB_EVENTS = 12000
# Les campagnes sont définies "à la main" plus bas

# --- Valeurs possibles -----------------------------------------------
CITIES = ["Paris", "Lyon", "Marseille", "Bordeaux", "Lille", "Nantes", "Toulouse"]
DEVICES = ["mobile", "desktop", "tablet"]
PLANS = ["free", "premium"]
CUISINES = ["Italien", "Japonais", "Burger", "Indien", "Libanais",
            "Français", "Mexicain", "Vegan", "Thaï", "Pizza"]
ORDER_STATUS = ["delivered", "delivered", "delivered", "delivered",
                "cancelled", "refunded"]  # ~66% delivered
EVENT_TYPES = ["app_open", "search", "restaurant_view",
               "add_to_cart", "checkout_start", "order_complete"]
CHANNELS = ["google", "meta", "tiktok", "email", "youtube"]


def random_date(jours_max=180):
    """Renvoie une date aléatoire entre il y a `jours_max` jours et aujourd'hui."""
    delta_jours = random.randint(0, jours_max)
    delta_secondes = random.randint(0, 86399)
    return TODAY - timedelta(days=delta_jours, seconds=delta_secondes)


def creer_tables(cur):
    """Supprime puis recrée les 5 tables avec PK, FK et index."""
    cur.executescript("""
        DROP TABLE IF EXISTS web_events;
        DROP TABLE IF EXISTS orders;
        DROP TABLE IF EXISTS marketing_campaigns;
        DROP TABLE IF EXISTS restaurants;
        DROP TABLE IF EXISTS users;

        CREATE TABLE users (
            user_id     INTEGER PRIMARY KEY,
            signup_date TEXT,
            city        TEXT,
            device_type TEXT,
            plan_type   TEXT,
            monthly_fee REAL
        );

        CREATE TABLE restaurants (
            restaurant_id INTEGER PRIMARY KEY,
            name          TEXT,
            city          TEXT,
            cuisine_type  TEXT,
            rating        REAL
        );

        CREATE TABLE orders (
            order_id              INTEGER PRIMARY KEY,
            user_id               INTEGER NOT NULL,
            restaurant_id         INTEGER NOT NULL,
            order_date            TEXT,
            amount                REAL,
            delivery_time_minutes INTEGER,
            status                TEXT,
            FOREIGN KEY (user_id)       REFERENCES users(user_id),
            FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
        );

        CREATE TABLE web_events (
            event_id   INTEGER PRIMARY KEY,
            user_id    INTEGER NOT NULL,
            event_type TEXT,
            session_id TEXT,
            timestamp  TEXT,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        );

        CREATE TABLE marketing_campaigns (
            campaign_id INTEGER PRIMARY KEY,
            channel     TEXT,
            impressions INTEGER,
            clicks      INTEGER,
            conversions INTEGER,
            cost        REAL
        );

        -- Index utiles (cf. cours recherche séquentielle vs indexée)
        CREATE INDEX idx_orders_user_date ON orders(user_id, order_date);
        CREATE INDEX idx_orders_restaurant ON orders(restaurant_id);
        CREATE INDEX idx_events_user_type  ON web_events(user_id, event_type);
    """)


def inserer_users(cur):
    lignes = []
    for uid in range(1, NB_USERS + 1):
        plan = random.choices(PLANS, weights=[70, 30])[0]
        fee = 5.99 if plan == "premium" else 0.0
        lignes.append((
            uid,
            random_date(365).strftime("%Y-%m-%d"),
            random.choice(CITIES),
            random.choice(DEVICES),
            plan,
            fee,
        ))
    cur.executemany(
        "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", lignes)


def inserer_restaurants(cur):
    lignes = []
    for rid in range(1, NB_RESTAURANTS + 1):
        cuisine = random.choice(CUISINES)
        lignes.append((
            rid,
            f"{cuisine} House {rid}",
            random.choice(CITIES),
            cuisine,
            round(random.uniform(3.0, 5.0), 1),
        ))
    cur.executemany(
        "INSERT INTO restaurants VALUES (?, ?, ?, ?, ?)", lignes)


def inserer_orders(cur):
    lignes = []
    for oid in range(1, NB_ORDERS + 1):
        lignes.append((
            oid,
            random.randint(1, NB_USERS),
            random.randint(1, NB_RESTAURANTS),
            random_date(120).strftime("%Y-%m-%d %H:%M:%S"),
            round(random.uniform(9.0, 65.0), 2),
            random.randint(15, 70),
            random.choice(ORDER_STATUS),
        ))
    cur.executemany(
        "INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?)", lignes)


def inserer_web_events(cur):
    lignes = []
    for eid in range(1, NB_WEB_EVENTS + 1):
        lignes.append((
            eid,
            random.randint(1, NB_USERS),
            random.choice(EVENT_TYPES),
            f"sess_{random.randint(1, 6000)}",
            random_date(90).strftime("%Y-%m-%d %H:%M:%S"),
        ))
    cur.executemany(
        "INSERT INTO web_events VALUES (?, ?, ?, ?, ?)", lignes)


def inserer_campaigns(cur):
    lignes = []
    for cid in range(1, 13):  # 12 campagnes
        impressions = random.randint(200_000, 2_000_000)
        clicks = int(impressions * random.uniform(0.005, 0.05))   # CTR 0.5%-5%
        conversions = int(clicks * random.uniform(0.02, 0.10))    # 2%-10%
        cost = round(clicks * random.uniform(0.30, 1.50), 2)      # CPC variable
        lignes.append((
            cid,
            random.choice(CHANNELS),
            impressions,
            clicks,
            conversions,
            cost,
        ))
    cur.executemany(
        "INSERT INTO marketing_campaigns VALUES (?, ?, ?, ?, ?, ?)", lignes)


def main():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    print("Création des tables...")
    creer_tables(cur)

    print(f"Insertion de {NB_USERS} utilisateurs...")
    inserer_users(cur)

    print(f"Insertion de {NB_RESTAURANTS} restaurants...")
    inserer_restaurants(cur)

    print(f"Insertion de {NB_ORDERS} commandes...")
    inserer_orders(cur)

    print(f"Insertion de {NB_WEB_EVENTS} événements web...")
    inserer_web_events(cur)

    print("Insertion de 12 campagnes marketing...")
    inserer_campaigns(cur)

    conn.commit()

    # Petit récapitulatif de contrôle
    print("\n--- Récapitulatif ---")
    for table in ["users", "restaurants", "orders",
                  "web_events", "marketing_campaigns"]:
        nb = cur.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"  {table:<22} : {nb} lignes")

    conn.close()
    print(f"\n✅ Base '{DB_NAME}' créée avec succès.")


if __name__ == "__main__":
    main()
