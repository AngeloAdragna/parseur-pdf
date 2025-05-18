# Sprint 5

**Auteurs : L3 CMI Informatique**

- Angelo Adragna
- Corentin Saccoman
- Elliot Pozucek
- Colin Palazzetti Rubera
- Elvin Fichot-Corgeron

**lien vers Github**
[README Sprint 5](https://github.com/conception-logicielle-CERI/parseur-pdf/edit/sprint-5/README_sprint5.md)

<!--pandoc README_sprint1.md -o README_sprint1.pdf --pdf-engine=xelatex-->

## **Rôles**

- Angelo est `SCRUM Master` et `Product Owner`, il doit rédiger le rapport avec les différents artefacts ainsi qu'une ou deux pages synthétiques récapitulant le résultat du sprint.
- Corentin, Elliot, Colin et Elvin sont développeurs.
- Les développeurs travaillent par binômes.
- Une partie de l’équipe (Corentin et Elliot) doit passer le système sur les 10 articles pour détecter les limites fixes et verifier si le nombre de frontières veritables découpé par l'humain est identique à celui découpé automatiquement.
- Un second binôme (Colin et Elvin) devra s'occuper d'établir le corpus de référence (les frontières souples) des sections en analysant miniscieusement à la main chaque phrases et comptabiliser le nombre de points.

## **Objectif**
Le Département de contrôle de qualité du LIA demande une évaluation de la qualité du système.
Cette évaluation peut être réalisée en fonction de la précision obtenue sur un corpus de référence (découpage de sections fait par des humains). Ainsi, les fragments de texte extraits présents dans les références seront comptabilisés positivement; leur absence sera pénalisée.
La précision sera calculée comme suit :

    Précision = Sections_correctes_trouvées_par_le_système / Sections_trouvées_par_le_système

Une section sera considérée correcte si :
- a) Toutes ses phrases ont été bien détectées : frontières strictes.
- b) Quelques phrases peuvent chevaucher les sections (± 2 phrases) : frontières souples.

Il faut ajouter une dernière phase d’évaluation du système qui reporte le résultat de la précision.
La précision sera mesurée sur un corpus de test de 10 nouveaux articles PDF. Une partie de l’équipe doit passer votre système sur les 10 articles, une autre doit établir le corpus de référence les frontières (souples) des sections. Enfin, vous devez calculer (à la main si vous voulez être agiles) la précision de votre système comme la moyenne sur l’ensemble des articles parsés.

Les détailles sont dans le [sprint5](sprint5_carnet_du_produit.pdf). 

## **Execution du programme**
```sh
# Affichage de l'aide pour les options : 
python parser.py -h

# Pas d'option de sélection des fichiers à parser :
python parser.py CORPUS_TRAIN/ CORPUS_TXT/                    # Format txt sans option
python parser.py -t CORPUS_TRAIN/ CORPUS_TXT/                 # Format txt avec option
python parser.py -x CORPUS_TRAIN/ CORPUS_XML/                 # Format xml 

# Sélection manuelle des fichiers à parser :
python parser.py -m CORPUS_TRAIN/ CORPUS_TXT/                 # Format txt sans option
python parser.py -t -m CORPUS_TRAIN/ CORPUS_TXT/              # Format txt avec option
python parser.py -x -m CORPUS_TRAIN/ CORPUS_XML/              # Format xml

# Option pour ne pas afficher les informations de parsage
python parser.py --no-verbose CORPUS_TRAIN/ CORPUS_TXT/       # Format txt sans option sans les infos de parsage
python parser.py -x --no-verbose CORPUS_TRAIN/ CORPUS_XML/    # Format xml sans les infos de parsage
python parser.py -x -m --no-verbose CORPUS_TRAIN/ CORPUS_XML/ # Séléction manuelle des fichiers à parser sans les infos de parsage

# Format raw (sortie brute de pdftotext) pour le débug
python parser.py -r CORPUS_TRAIN/ CORPUS_RAW/    
```
**Résultats attendus :**   
Le répértoire CORPUS_TXT/ contiendra les fichiers texte avec uniquement le nom du fichier, le titre et l'abstract.  
Le répértoire CORPUS_XML/ contiendra les fichiers xml avec toutes les infos demandées pour le xml.


## **Revu Sprint 5**
- Debrief sur le produit du quatrième sprint mitigé. Le travail a été effecuté sans être testé, ceci à causé de gros problème à l'aube du sprint 5.
- Répartition des tâches par binômes selon les affinités de chacun. Communication très difficile.
- Les différents rendus des devs étaient satisfaisants.
- Un problème commun aux développeurs semble être le manque de robustesses du aux différements formats possibles au seins des PDF.
  
## **Réunion planification Sprint 16/05/25**
La communication était mauvaise, le `SCRUM MASTER` à peiné à tenir notes de cette réunion car chacun est parti de son côté et que le contenu à réalisé est maigre et rapide à repartir.
![notes sur papier](images/reunion5.jpg)  

## **Sprint Backlog**
   - Test précision avec des frontières strictes.
   - Test précision avec des frontières souples.
   - Calcul de la précision : Précision = Sections_correctes_trouvées_par_le_système / Sections_trouvées_par_le_système
- Améliorer les fonctionnalités du code.
- Réaliser les artefacts compris dans le conteneur de ce sprint 5.

## **Burndown**
![Exemple sortie](images/burndown5.jpg)

## _Consignes pour le compte rendu des développeurs_ :
- Premier retour de la part des développeurs le dimanche 18/05/2025 sur le travail effecté.
- Déposez votre compte rendu au plus tard le ? à ? sur la branche 5.
- Fournir AU MOINS une image de l’avancement par fonctionnalité par développeur.
- Votre compte rendu doit comporter une analyse succinte de votre travail, tourné principalement autour de la `précision`… Vous pourrez vous baser sur le squelette pour vous guider si nécéssaire.
- Indiquer quel jour vous avez fini chaque étape de votre progression !
- Penser à bien décrire les différents calculs de précision de chaque document.

## **Travail de chaque membre de la `SCRUM Team` pendant la mêlée (Revue Sprint)**

---

## 1. **Angelo Adragna** : Documentation des événements/artefacts Scrum (réunions de planification de sprint, mêlée quotidienne, revue de sprint, rétrospective du sprint) et rédaction condensé en 2 pages tournée vers la précision du programme.

- Les backlogs doivent être réalisés en premier lieu, lors de la première réunion, afin de répartir les tâches entre chaque personne.
- La réunion a permis d'établir la liste de questions pour le client, afin d'obtenir davantage de détails et de spécifications.
- Le Burndown se termine à la fin du sprint 5.
- La rédaction se fait au fil du sprint.
- Création d'un squelette de rendu pour facilier la mise en commun du travail de chacun. Je propose donc un modèle en raison du manque de détails dans les productions personnelles des développeurs.
- Médiation et conseils aux développeurs.
- Rédaction synthétique en une ou deux pages.

---

## 2. **Elliot Pozucek**, **Corentin Saccoman** : Test précision avec des frontières strictes (en binôme)

### **Développement**

#### Comptage des frontières

Afin d'évaluer la précision de notre algorithme sur l'ensemble de test, nous avons besoin de connaître le nombre de frontières présentes dans chaque article, le nombre de frontières trouvées par notre algorithme et le nombre de frontières trouvées par notre algorithme qui sont correctes (bien délimitées à +/- 2 lignes près).

Pour être précis :

 - nous avons créé un fichier `frontieres.xml`
 - ce fichier contient les mêmes balises que les fichiers xml résultants de l'algorithme (\<titre>, \<auteur>, etc)
 - trois balises ont été ajoutées :
    - \<frontieres-veritables> : le nombre de frontières réellement présentes dans l'article
    - \<frontieres-trouvees> : le nombre de frontières trouvées par l'algorithme
    - \<frontieres-correctes> : le nombre de frontières trouvées par l'algorithme qui sont correctes (bien délimitées à +/- 2 lignes près)
 - Une balise <document> a été ajoutée pour chaque article, avec un nom (ex: \<document nom="article1">)

##### Comtage des frontières réelles

Voici la méthode utilisée pour compter le nombre de frontières présentes dans un article :
 - on éxécute l'algorithme avec l'option -r (python parser.py -r CORPUS_TEST/ CORPUS_TEST_RAW/)
 - pour chaque article :
    - on ouvre le pdf et le fichier txt (raw)
    - pour chaque section :
        - on repère dans le pdf le début de la section
        - on cherche la première ligne de la section dans le txt (raw)
        - on écrit le numéro de la ligne dans le fichier `frontieres.xml`
        - on cherche la fin de la section dans le pdf
        - on cherche la première ligne de la section dans le txt (raw)
        - on écrit le numéro de la ligne dans le fichier `frontieres.xml`
        - cela donne par exemple : \<titre>1-3\</titre> (le titre se situe entre la ligne 1 et la ligne 3 dans le txt raw)
        - si la section n'existe pas dans le pdf, on écrit `None`
    - une fois ce travail effectué pour chaque section, on compte le nombre de sections réellement présentes dans l'article en comptant le nombre de balises où il n'y a pas de `None` et on écrit le résultat dans le fichier `frontieres.xml`, dans la balise \<frontieres-veritables>
 - une fois ce travail effectué pour chaque article, le fichier `frontieres.xml` contient le nombre de sections présentes dans chaque article

##### Comptage des frontières trouvées

Voici la méthode utilisée pour compter le nombre de frontières trouvées par notre algorithme :
 - on éxécute l'algorithme avec l'option -x (python parser.py -x CORPUS_TEST/ CORPUS_TEST_XML/)
 - pour chaque article :
    - on ouvre le fichier xml
    - on compte le nombre de balises non-vides (la balise \<preambule> est ignorée), le nombre de balises non-vides correspond au nombre de sections trouvées par l'algorithme
    - on écrit le résultat dans le fichier `frontieres.xml`, dans la balise \<frontieres-trouvees>
 - une fois ce travail effectué pour chaque article, le fichier `frontieres.xml` contient le nombre de sections trouvées par l'algorithme dans chaque article

#### Ajout de l'option --no-verbose (Elliot)

Lors de la réalisation de ma partie du sprint-5, j'ai remarqué que le terminal était très pollué par les messages de parsing. Bien que ces messages soient utiles, j'ai décidé de créer une option `--no-verbose` pour permette de les désactiver.

J'ai donc ajouté la ligne suivante dans `parser.py`, dans la fonction `parse_arguments()` : 
```python
# Ajout d'un argument --no-verbose pour désactiver les messages d'information
parser.add_argument("--no-verbose", action="store_true", help="N'affiche pas les informations détaillées pendant l'exécution.")
```

J'ai ensuite ajouté une vérification dans les méthodes `convert_pdf_file()` et lors de l'énumération des fichiers pdf dans le `main` afin de ne pas afficher les messages si l'option `--no-verbose` est activée.

```python
# convert_pdf_file
if not args.no_verbose :
    print(f"{fichier_pdf.name} converti en {fichier_sortie.name}")

# main
if not args.no_verbose:
    print("Fichiers PDF trouvés :")
    for pdf in pdfs:
        print(" -", pdf.name)
```

Cette option est robuste et fonctionne avec toutes les autres options (j'ai testé avec toutes les combinaisons d'options possibles).  
Par exemple, on peut exécuter la commande suivante :
```bash
python parser.py -x --no-verbose CORPUS_TEST/ CORPUS_TEST_XML/
```
Cela va exécuter l'algorithme avec l'option -x (génération du fichier xml) et l'option `--no-verbose` (pas de messages d'information).

---

#### Ajout du fichier precision.py (Elliot)

Une fois que le fichier `frontieres.xml` a été correctement rempli, j'ai voulu créer un script permettant de calculer la précision de notre algorithme en fonction de ce fichier.  
J'ai donc créé le fichier `precision.py` qui contient la fonction `calcul_precision()`. Cette fonction prend en entrée un chemin (str) et écrit dans le terminal la précision de l'algorithme sur chaque article de l'ensemble de test, ainsi que la précision globale sur cet ensemble. Ce script ne fonctionne qu'avec le fichier `frontieres.xml` ou avec un fichier xml de même structure.

La précision pour chaque article est calculée conformément à la formule donnée dans l'Objectif du sprint-5 :

```python
precision = frontieres_correctes / frontieres_trouvees
```

Le script va parser le fichier xml donné en entrée (`frontieres.xml`) et va, pour chaque article, récupérer le nombre de frontières trouvées et le nombre de frontières correctes. La précision est calculée puis affichée dans le terminal. Les erreurs sont gérées (ex: si le nombre de frontières trouvées est égal à 0, pas un nombre, si les balises ne sont pas présentes, etc).

Voici un exemple d'utilisation (précision = 0 car pas encore de comptage des frontières correctes) :

![](images/elliot_img1.png)


#### Comptage manuel du score de chaque fichier (Corentin)
Une fois le nombre de frontières déterminées, il a fallu vérifier manuellement leur correspondance avec la réalité.  
J'ai alors rempli la balise \<frontieres-correctes> afin d'apporter une consolidation aux résultats trouvés pas Colin et Elvin.  

J'ai effectué cette mesure manuelle sur l'intégralité des fichiers de test.  
Pour ce qui est des résultats trouvés par Elvin, ils concordaient.  

Suite à ces mesures et au remplissage des balises du fichiers `frontieres.xml`, j'ai pu exécuter le programme `precision.py` afin de calculer la précision individuelle de chaque fichier ainsi que la précision globale du parseur.  
![](images/corentin_img1.png)  

Le score global est fortement affecté par le deuxième fichier, ayant un formatage assez singulier, dégradant les performances du parseur.

### **Remarque**

### **Précision**

### **Piste d'amélioration**

### **Dates clés** :
- Corentin, Elliot, 16/05 : Réalisation du fichier `frontieres.xml` et découpage manuel des fichiers de test.
- Elliot, 18/05 : Réalisation du programme de test de précision, ajout d'un argument au parseur, actualisation du balisage de `frontieres.xml`
- Corentin, 18/05 : Détermination des performances du parseur et attente des résulats de Colin pour vérifications.

  ---

## 3. **Colin Palazzetti Rubera** : Test précision avec des frontières souples.

### **Retour sur les documents découpés**

### **Précision**

### **Piste d'amélioration**

### **Dates clés** :
 
  ---

## 4. **Elvin Fichot-Corgeron** : Test précision avec des frontières souples.

### **Retour sur les documents découpés**

### **Précision**

### **Piste d'amélioration**

### **Dates clés** :

  ---

## **Retour sur le travail effectué (Rétrospective Sprint 5)** A faire
### **Ce qui a bien fonctionné**
- Bonne répartition des tâches entre les membres, chacun a pu avancer sur sa partie sans trop d’interférences.
- L’intégration progressive des travaux (Colin, Elliot, Corentin) a permis une mise en commun fluide.
- Les réunions Scrum ont été efficaces pour identifier les points bloquants et ajuster les priorités.
- La génération des fichiers XML et TXT selon les besoins du client a été bien maîtrisée.
- L’ajout du menu de sélection manuelle de fichiers améliore l’ergonomie de l’outil.
- La détection de la section `Introduction` est globalement robuste, même si quelques cas spéciaux demeurent.
- Le découpage précis du `Corps` de texte avec préservation des retours à la ligne facilite les traitements futurs.
- Une réelle progression dans la qualité des contributions individuelles et de la documentation.
- Réelle entraide entre Corentin et Elliot afin de pouvoir supprimer l'introduction à l'aide du REGEX de Corentin de la section `Corps` d'Elliot.

### **Ce qui a posé problème**
- Le fichier *marcu_statistics_sentence_pass_one.pdf* reste problématique car il ne suit aucun des formats habituels pour les titres de section.
- L'absence de numérotation dans certains fichiers empêche une récupération fiable des sections comme `Introduction`.
- La reconnaissance automatique des débuts et fins de section `Corps` reste complexe en raison de l’hétérogénéité du corpus.
- Certains cas extrêmes dans les séparations ligne/colonne ou les notes de bas de page parasitent encore le parsing.
- Quelques divergences entre les formats XML générés par différents membres ont nécessité une harmonisation finale.
- Une dépendance persistante à l’outil `pdftotext` (Linux uniquement) complique la portabilité.

### **Ce qu’on doit améliorer**
- Uniformiser davantage la structure des balises XML générées par chaque module pour éviter des incohérences.
- Proposer une détection plus sémantique pour les débuts de section en se basant sur le contenu et non uniquement les titres.
- Prévoir une phase de nettoyage de texte en amont pour corriger automatiquement les caractères spéciaux ou artefacts liés au format PDF.
- Ajouter des tests unitaires pour les nouvelles fonctions (`extract_introduction`, découpage du `corps`, menu de sélection).
- Rendre l’application plus portable en envisageant une alternative multiplateforme à `pdftotext`.
- Améliorer la couverture documentaire avec des exemples concrets dans le README final.

---

## **Conclusion** :

### Selon Angelo Adragna
- Suivi rigoureux de la méthode Scrum, avec une planification plus détaillée et des revues efficaces.
- Coordination fluide malgré les difficultés techniques rencontrées sur certains fichiers.
- Le squelette commun a facilité l’unification du rendu final.
- Bonne anticipation des points de friction en amont des deadlines.
- Une dynamique de groupe constructive et un gain notable en autonomie dans la rédaction des comptes rendus.

### Selon Corentin Saccoman
- L’ajout du menu interactif permet une vraie valeur ajoutée à l’expérience utilisateur.
- L'extraction de la section `Introduction` a nécessité des compromis mais fonctionne bien dans la majorité des cas.
- Bonne maîtrise des expressions régulières et adaptation au corpus, avec des réflexions sur les limites à long terme.
- Volonté de rendre le code robuste malgré les exceptions.
- Quelques frustrations sur l'impossibilité de généraliser certains patterns, mais vision claire des pistes futures.

### Selon Elliot Pozucek
- Le traitement de la section `Corps` a gagné en clarté, grâce au découpage ligne à ligne et au respect de la structure d’origine.
- Le maintien des retours à la ligne est un choix pertinent pour une utilisation ultérieure du contenu.
- Quelques difficultés à gérer les transitions entre les sections (`abstract`, `introduction`, `corps`), mais des solutions concrètes ont été apportées.
- Le temps de traitement reste raisonnable malgré les nouveaux traitements.
- Suggestion d’intégrer un système de logs plus fin pour suivre l’évolution de chaque fichier.

### Selon Colin Palazzetti Rubera
- Travail de normalisation des formats XML et harmonisation des conventions entre les modules.
- Poursuite des efforts sur la documentation (docstrings, structure).
- Identification d’un besoin de meilleure robustesse dans les extractions d’informations critiques (ex. : titre, auteurs).
- Propositions concrètes pour renforcer la résilience du système en cas de fichier malformé ou ambigu.

### Global
Les modules développés sont plus stables, les intégrations se font sans blocage majeur, et les livrables sont conformes aux attentes.  
L’autonomie de chaque membre est notable et les prises d’initiative (menu, gestion des sections, normalisation) vont au-delà des attentes initiales.  
L’outil commence à être réellement exploitable pour le client, avec un usage plus flexible et une structure de sortie bien définie.  
Il reste des améliorations possibles pour la robustesse et la portabilité, mais le cœur du système est désormais en place.  
L'objectif reste le produit, c'est pourquoi, même si l'équipe souhaitait aller plus loin en termes de fonctionnalités, elle a su se contraindre à ce qui était imposé.
