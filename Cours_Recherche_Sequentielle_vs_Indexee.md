# 🔍 Recherche séquentielle vs Recherche indexée

> **Fiche de cours — Bloc B3 « Pilotage de la Donnée »**
> Objectif : comprendre pourquoi un index accélère une base de données, et à quel prix.

---

## 1. L'idée en une phrase

> Quand on cherche une donnée dans une table, la base peut soit **tout lire ligne par ligne** (séquentiel), soit **aller directement au bon endroit grâce à un index** (indexé).
>
> C'est la différence entre **lire un livre en entier** et **utiliser sa table des matières**.

---

## 2. L'analogie du dictionnaire 📖

Tu cherches le mot **« zèbre »** dans un dictionnaire.

### 🐢 Méthode séquentielle
Tu commences à la **page 1**, et tu lis **chaque page une par une** :
`page 1… page 2… page 3… … page 1499… page 1500 → trouvé !`

➡️ Tu as lu **tout le dictionnaire** pour un seul mot.

### ⚡ Méthode indexée
Le dictionnaire est **trié par ordre alphabétique** (= c'est ça, l'« index »).
Tu ouvres directement vers la fin (lettre Z), tu affines en quelques sauts → trouvé.

➡️ Tu n'as lu que **quelques pages**.

> 💡 **Le tri, c'est l'index.** Sans tri, impossible de « sauter » au bon endroit : on est obligé de tout parcourir.

---

## 3. Concrètement en base de données

Prenons une table `ORDERS` (commandes) avec **200 millions de lignes**.
On veut toutes les commandes du client n°5000 :

```sql
SELECT * FROM ORDERS WHERE user_id = 5000;
```

### 🐢 Sans index → recherche séquentielle (« full table scan »)

La base **lit les 200 millions de lignes**, une par une, et teste à chaque fois :
« *est-ce que `user_id = 5000` ?* »

```
Ligne 1   → user_id = 12   ❌
Ligne 2   → user_id = 8743 ❌
Ligne 3   → user_id = 5000 ✅  (on garde)
Ligne 4   → user_id = 221  ❌
...
Ligne 200 000 000 → ...
```

Même s'il n'y a que 8 commandes pour ce client, la base a dû **tout vérifier**. 😱

### ⚡ Avec index → recherche indexée

On crée une fois pour toutes un index sur la colonne :

```sql
CREATE INDEX idx_orders_user ON ORDERS(user_id);
```

La base construit alors **en coulisses** une structure de données **triée** appelée
**arbre B-tree** (B = *balanced*, équilibré). Pour trouver `user_id = 5000`,
elle **descend dans l'arbre** au lieu de tout parcourir :

```
                 [ 5000 ? ]
                /          \
        plus petit       plus grand
           /  \             /   \
         ...  [≈5000]      ...   ...
                 ↓
        → lignes du client 5000 trouvées directement
```

➡️ Quelques sauts suffisent au lieu de 200 millions de lectures.

---

## 4. La différence chiffrée : la complexité (Big-O)

La **complexité algorithmique** mesure comment le temps de recherche
**augmente avec le nombre de lignes** `n`.

| | Recherche séquentielle | Recherche indexée |
|---|---|---|
| Méthode | Parcourt **toutes** les lignes | Descend dans un arbre trié |
| Complexité | **O(n)** — *linéaire* | **O(log n)** — *logarithmique* |
| Image | Lire tout le livre | Utiliser la table des matières |

### Pourquoi c'est énorme ? Comparons sur des volumes réels :

| Nombre de lignes (n) | Séquentiel O(n) | Indexé O(log₂ n) |
|---|---|---|
| 1 000 | 1 000 lectures | ~10 |
| 1 000 000 | 1 000 000 lectures | ~20 |
| 200 000 000 | 200 000 000 lectures | **~28** |

> 👉 Multiplier les données par 200 000 ne rajoute que **~8 étapes** avec un index.
> Avec une recherche séquentielle, ça multiplie le temps par 200 000.

---

## 5. ⚠️ Le piège : l'index n'est PAS gratuit

Question logique d'étudiant :
> *« Si l'index va si vite, pourquoi ne pas indexer TOUTES les colonnes ? »*

Parce qu'il y a un **compromis** (le mot clé à retenir) :

| ✅ Avantages de l'index | ❌ Inconvénients de l'index |
|---|---|
| Lectures (`SELECT`) **beaucoup** plus rapides | Prend de la **place de stockage** en plus |
| Idéal pour les colonnes très recherchées | **Ralentit les écritures** : à chaque `INSERT` / `UPDATE` / `DELETE`, la base doit **mettre à jour l'index** en plus de la table |

> 🎯 **Règle d'or** : on indexe les colonnes **souvent utilisées dans
> `WHERE`, `JOIN` ou `ORDER BY`** (ex. `user_id`, `order_date`),
> **pas** toutes les colonnes.

---

## 6. ⚠️ À ne pas confondre

> Ce n'est **pas la requête SQL** qui est « séquentielle » ou « indexée ».
> La requête s'écrit **exactement pareil** dans les deux cas :
>
> ```sql
> SELECT * FROM ORDERS WHERE user_id = 5000;
> ```
>
> Ce qui change, c'est **la façon dont la base va chercher** :
> - **un index existe** sur `user_id` → recherche **indexée** ⚡
> - **aucun index** → recherche **séquentielle** 🐢
>
> 💡 La base choisit automatiquement la meilleure méthode disponible.
> On peut le vérifier avec la commande `EXPLAIN` devant une requête
> (elle montre si la base fait un *scan* ou utilise un *index*).

---

## 7. À retenir (résumé express)

- **Séquentiel** = tout lire ligne par ligne → **O(n)** → lent sur gros volumes 🐢
- **Indexé** = aller direct grâce à une structure triée (B-tree) → **O(log n)** → rapide ⚡
- Un index **accélère les lectures** mais **coûte du stockage** et **ralentit les écritures**
- On indexe les colonnes des `WHERE` / `JOIN` / `ORDER BY`, **pas tout**
- La requête est identique ; c'est la **présence d'un index** qui change la vitesse

---

## 8. Pour aller plus loin (optionnel)

```sql
-- Voir comment la base exécute la requête
EXPLAIN SELECT * FROM ORDERS WHERE user_id = 5000;

-- Créer un index composite (utile si on filtre sur 2 colonnes ensemble)
CREATE INDEX idx_orders_user_date ON ORDERS(user_id, order_date);
```

> Un **index composite** `(user_id, order_date)` est parfait pour une requête
> du type « les commandes d'un client **sur les 60 derniers jours** ».
