# Sprint 3 - Elliot Pozucek

## Tâche : Récupération de la section bibliographique et renvoit dans un plain texte.

### Analyse du code

#### Général

Ajout du fichier `ref_bibblio.py` qui permet de récupérer la section des références bibliographiques d'un corpus textuel (`txt`).

Modification du script `clear_txt.sh` pour ajouter la suppression des xml générés.

Ajout d'un paramètre `-r` pour le script `parser.py` qui permet de parser les fichiers `pdf` dans leur version `txt` sans les transformer. Ils contiennent donc le résultat brut de la commande `pdftotext -raw`. J'ai ajouté ce paramètre afin de pouvoir effectuer des tests.

#### Fonction `get_references`

Cette fonction permet de récupérer la section des références bibliographiques d'un texte. Voici les étapes de la fonction :

- récupérer la section des références bibliographiques d'un texte (cherche la dernière occurence des mots-clés "References" ou "Bibliography", en ignorant la casse)
- nettoyer le texte brute de la section récupérée (enlève les espaces superflus, les sauts de ligne, etc.)
- chercher un pattern de référence bibliographique : dans les trois cas, on cherche une occurence du pattern, puis on récupère le texte compris entre chaque occurence du pattern
    - numérotation '[n]'
    - numérotation 'n.'
    - pas de numérotation -> cherche une initiale (ex: J. Smith), puis saute 30 caractères et cherche à nouveau une initiale
- renvoyer la liste des références bibliographiques trouvées

#### Exemple

Dans le pdf, on a :

![](images/pdf_version.png)

Après avoir parsé le pdf, on a :

![](images/txt_version.png)

Puis dans le xml, on a :

![](images/xml_version.png)

#### Explication pour le pattern sans numérotation

Le pattern sans numérotation est le plus complexe à mettre en place. En effet, je n'ai pas trouvé de solution robuste à tous les cas de figure. J'ai donc décidé de faire un compromis entre la robustesse et la simplicité.

J'ai d'abord remarqué que seul deux textes de `CORPUS_TRAIN` contiennent des références bibliographiques sans numérotation. J'ai ensuite remarqué que dans ces deux textes, les références commencent toutes par une initiale en majuscules puis d'un point (ex: J. Smith).  
Cependant, la plupart des références contiennent plusieurs initiales (ex: J. Smith et A. Doe). J'ai donc décidé de chercher une initiale en majuscule suivie d'un point, puis de sauter 30 caractères (toujours moins que la longueur d'une référence) et de chercher à nouveau une initiale en majuscule.

Pour notre corpus, cette méthode fonctionne très bien. J'ai intégré mon travail dans le fichier `parser.py`. Mon travail est utilisé pour générer les fichiers xml.

---

#### Ajout d'un

### Pistes d'amélioration

Les méthodes de recherche de pattern sont très simples et sont adaptées à notre corpus. Elles manquent donc de robustesse.

Je commence à voir les limitations de notre méthode de base pour extraire le texte brut. En effet, ne pas pouvoir utiliser les retours/sauts de ligne pour séparer les différentes sections du texte est très contraignant, car ces sauts/retours de ligne ont souvent une valeur sémantique significative.

---

### Analyse de performances

En terme de performance, la méthode que j'ai mise en place dans le sprint 2 (`log_execution_time`) nous est très utile. En effet, la moyenne des temps d'exécution de l'ensemble de notre programme est passé de 0.5 secondes à 1.25 secondes sur ma machine. 

On peut donc dire que la méthode de recherche de pattern est très gourmande en temps d'exécution.

---

### **Remarque**

Je t'aime Angelo