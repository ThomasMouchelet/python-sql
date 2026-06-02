# TP QuickBite — Bases de données SQLite & Python

Travaux pratiques du **Bloc B3 – Pilotage de la Donnée**.
Vous allez interroger une base de données SQLite en Python à partir
d'un jeu de données fictif (plateforme de livraison de repas QuickBite).

---

## 🧰 Prérequis

- **Python 3** installé.
- **Rien d'autre à installer** : on utilise uniquement la bibliothèque
  standard (`sqlite3`), incluse dans Python.

Vérifier que Python est bien installé :

```bash
python3 --version
```

---

## 📂 Contenu du dossier

| Fichier | Rôle |
|---|---|
| `seed_quickbite.py` | Crée la base `quickbite.db` et la remplit de fausses données |
| `tp_quickbite_a_completer.py` | Le TP à compléter (questions à coder) |
| `quickbite.db` | La base de données (générée automatiquement, ne pas modifier à la main) |
| `README.md` | Ce fichier |

---

## 🚀 Commandes à lancer

> Ouvrez un terminal **dans ce dossier** avant de lancer les commandes.

### Étape 1 — Créer la base de données

```bash
python3 seed_quickbite.py
```

Cette commande crée le fichier `quickbite.db` et affiche un récapitulatif :

```
--- Récapitulatif ---
  users                  : 500 lignes
  restaurants            : 60 lignes
  orders                 : 4000 lignes
  web_events             : 12000 lignes
  marketing_campaigns    : 12 lignes

✅ Base 'quickbite.db' créée avec succès.
```

> 💡 Vous pouvez relancer cette commande à tout moment : elle recrée la
> base proprement (les données sont toujours **identiques** grâce à une
> graine aléatoire fixe).

### Étape 2 — Compléter et exécuter le TP

1. Ouvrez `tp_quickbite_a_completer.py` dans votre éditeur.
2. Complétez les parties marquées `# TODO`.
3. Lancez le script pour voir vos résultats :

```bash
python3 tp_quickbite_a_completer.py
```

Tant que les `# TODO` ne sont pas remplis, les résultats apparaîtront
vides : c'est normal. Au fur et à mesure que vous complétez, les
réponses s'affichent.

---

## 🗂️ Structure de la base (5 tables)

| Table | Description |
|---|---|
| `users` | Les utilisateurs (ville, type d'appareil, abonnement) |
| `restaurants` | Les restaurants partenaires (cuisine, note) |
| `orders` | Les commandes (montant, statut, date) |
| `web_events` | Les événements de navigation (funnel) |
| `marketing_campaigns` | Les campagnes publicitaires (clics, coûts, conversions) |

---

## 🔎 Explorer la base sans Python (optionnel)

Vous pouvez aussi inspecter la base directement avec l'outil en ligne
de commande `sqlite3` :

```bash
sqlite3 quickbite.db
```

Quelques commandes utiles une fois dedans :

```sql
.tables                         -- liste les tables
.schema orders                  -- structure d'une table
SELECT * FROM users LIMIT 5;    -- les 5 premiers utilisateurs
.quit                           -- quitter
```

---

## ⚠️ Rappels utiles

- **Dates en SQLite** : elles sont stockées en texte. Pour filtrer sur
  les 60 derniers jours :
  ```sql
  WHERE order_date >= date('now', '-60 days')
  ```
- **Lire les résultats en Python** :
  - `cur.fetchone()` → une seule ligne
  - `cur.fetchall()` → toutes les lignes
- Pensez à **fermer la connexion** avec `conn.close()` à la fin de
  chaque fonction.

---

## ❓ Problèmes fréquents

| Message | Cause / solution |
|---|---|
| `no such table: users` | Vous n'avez pas lancé `python3 seed_quickbite.py` d'abord. |
| `command not found: python3` | Essayez `python` au lieu de `python3`. |
| Résultats vides | Les `# TODO` ne sont pas encore complétés (normal au début). |
| `unable to open database file` | Lancez les commandes **depuis le dossier** qui contient les scripts. |
