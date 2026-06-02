# EXERCICE D'ENTRAÎNEMENT — QUICKBITE DATA LAB

**MSc 2 — Manager en Data Marketing**
**Bloc UEP « B3 – Pilotage de la Donnée »**
**Parties évaluées : Algorithmes & Bases de données · Langages de Programmation (Python) · API**

- Durée conseillée : 2h00
- Documents autorisés : aucun – Internet interdit
- Calculatrice autorisée
- Support : feuille (réponses rédigées, schémas et pseudo-code acceptés)

> ⚠️ Cet exercice est un **entraînement**. Il reprend les mêmes notions que le partiel officiel mais sur un cas différent. Soignez la rigueur SQL, la clarté algorithmique et la structuration du raisonnement.

---

## 1. Contexte général

**QuickBite** est une application européenne de **livraison de repas à domicile** mettant en relation des clients et des restaurants partenaires.

**Données clés :**
- 2,1 millions d'utilisateurs actifs
- 14 000 restaurants partenaires
- 9,3 millions de commandes / mois
- Panier moyen : 24,50 €
- 72 % des commandes passées via l'application mobile
- Abonnement « QuickBite+ » : 5,99 €/mois (livraison gratuite)

**Objectifs stratégiques 2027 :**
1. Augmenter la fréquence de commande par utilisateur
2. Améliorer la recommandation de restaurants/plats
3. Optimiser la performance des campagnes d'acquisition
4. Moderniser l'architecture data et l'ouvrir via des API

---

## 2. Données disponibles (extrait simplifié)

### Table `USERS`
| Champ | Type |
|---|---|
| user_id | INT |
| signup_date | DATE |
| city | VARCHAR |
| device_type | VARCHAR |
| plan_type | VARCHAR (free / premium) |
| monthly_fee | FLOAT |

### Table `RESTAURANTS`
| Champ | Type |
|---|---|
| restaurant_id | INT |
| name | VARCHAR |
| city | VARCHAR |
| cuisine_type | VARCHAR |
| rating | FLOAT |

### Table `ORDERS`
| Champ | Type |
|---|---|
| order_id | INT |
| user_id | INT |
| restaurant_id | INT |
| order_date | DATETIME |
| amount | FLOAT |
| delivery_time_minutes | INT |
| status | VARCHAR |

`status` possibles : `delivered`, `cancelled`, `refunded`

### Table `WEB_EVENTS`
| Champ | Type |
|---|---|
| event_id | INT |
| user_id | INT |
| event_type | VARCHAR |
| session_id | VARCHAR |
| timestamp | DATETIME |

`event_type` possibles :
- `app_open`
- `search`
- `restaurant_view`
- `add_to_cart`
- `checkout_start`
- `order_complete`

### Table `MARKETING_CAMPAIGNS`
| Champ | Type |
|---|---|
| campaign_id | INT |
| channel | VARCHAR |
| impressions | INT |
| clicks | INT |
| conversions | INT |
| cost | FLOAT |

---

## PARTIE 1 — ALGORITHMES & BASES DE DONNÉES (25 points)

**1.1** Proposez un **schéma relationnel optimisé** pour ces 5 tables : indiquez les clés primaires (PK), les clés étrangères (FK) et au moins **3 index** pertinents en justifiant leur utilité. *(6 pts)*

**1.2** Écrivez une requête **SQL** qui calcule, pour chaque utilisateur, son **panier moyen** (montant moyen des commandes `delivered`) et son **nombre de commandes** sur les **60 derniers jours**. Triez du panier moyen le plus élevé au plus faible. *(6 pts)*

**1.3** Expliquez la **complexité algorithmique** d'une **recherche séquentielle** vs d'une **recherche indexée** lorsqu'on cherche toutes les commandes d'un `user_id` donné dans la table `ORDERS` (qui contient des centaines de millions de lignes). Donnez la notation Big-O et expliquez le compromis (coût en lecture vs coût en écriture/stockage). *(6 pts)*

**1.4** Proposez un **algorithme simple de recommandation de restaurants** pour un utilisateur (logique en français + **pseudo-code**). Vous pouvez vous appuyer sur l'historique de commandes et/ou le type de cuisine. *(7 pts)*

---

## PARTIE 2 — LANGAGES DE PROGRAMMATION / PYTHON (25 points)

**2.1** Expliquez pourquoi **Python** est aujourd'hui un langage de référence en data marketing (citez au moins 4 raisons concrètes). *(5 pts)*

**2.2** Écrivez un **pseudo-code Python** (ou code Python réel) permettant de :
- charger un fichier `campaigns.csv` (colonnes : `campaign_id, channel, impressions, clicks, conversions, cost`)
- calculer le **CTR** (taux de clic) et le **CPA** (coût par acquisition) de chaque campagne
- afficher uniquement les campagnes dont le **CTR < 1,5 %**
*(8 pts)*

**2.3** Comparez **SQL** et **Python** pour l'analyse de données marketing : pour quel type de tâche chacun est-il le plus adapté ? Donnez 2 forces et 1 limite pour chacun. *(6 pts)*

**2.4** Un collègue dit : *« On peut tout faire avec des boucles `for`, pas besoin de bibliothèques. »* Expliquez l'intérêt d'utiliser des bibliothèques comme **pandas** plutôt que des boucles manuelles sur de gros volumes (lisibilité, performance, vectorisation). *(6 pts)*

---

## PARTIE 3 — API & ÉCOSYSTÈME DATA MODERNE (25 points)

**3.1** Expliquez l'**intérêt des API** dans un écosystème data moderne. Donnez 3 cas d'usage concrets pour QuickBite (interne et externe). *(7 pts)*

**3.2** Définissez ce qu'est une **API REST**. Expliquez brièvement : les principales **méthodes HTTP** (GET, POST, PUT, DELETE), le format **JSON**, et le rôle d'un **token d'authentification**. *(6 pts)*

**3.3** Écrivez un **pseudo-code Python** qui interroge une API REST pour **enrichir les données** : par exemple récupérer les statistiques d'une campagne depuis l'API d'une régie publicitaire (endpoint `GET /campaigns/{id}/stats`, authentification par token), puis afficher le `cost` et les `conversions` retournés en JSON. Gérez le cas où la requête échoue. *(7 pts)*

**3.4** Citez 3 **codes de statut HTTP** courants (ex. 200, 404…) et expliquez ce que chacun signifie pour le développeur qui consomme l'API. *(5 pts)*

---

## BARÈME GLOBAL

| Partie | Points |
|---|---|
| Algorithmes & BDD | 25 |
| Langages de Programmation (Python) | 25 |
| API & Écosystème data | 25 |
| **TOTAL** | **75 points** |

## Critères d'évaluation
- Maîtrise technique
- Clarté algorithmique
- Rigueur SQL
- Capacité à formaliser un algorithme / coder logiquement (même en pseudo-code)
- Compréhension de l'écosystème data (API, outils)
- Structuration du raisonnement et pertinence business
