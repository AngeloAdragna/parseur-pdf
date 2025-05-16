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

- Angelo est `SCRUM Master` et `Product Owner`, il doit rédiger le rapport avec les différents artefacts.
- Corentin, Elliot, Colin et Elvin sont développeurs.
- Les développeurs travaillent par binômes.
- Une partie de l’équipe (Corentin et Elliot) doit passer votre système sur les 10 articles pour détecter les limites fixes.
- Un second binôme devra s'occuper d'établir le corpus de référence les frontières (souples) des sections en analysant miniscieusement à la main chaque phrases et comptabiliser à la main le nombre de points.

## **Objectif**

Cette évaluation peut être réalisée en fonction de la précision obtenue sur un corpus de référence
(découpage de sections fait par des humains). Ainsi, les fragments de texte extraits présents dans les
références seront comptabilisés positivement; leur absence sera pénalisée (voir l’exemple en Annexe).
La précision sera calculée comme suit :
 Précision = Sections_correctes_trouvées_par_le_système / Sections_trouvées_par_le_système
Une section sera considérée correcte si :
a) Toutes ses phrases ont été bien détectées : frontières strictes.
b) Quelques phrases peuvent chevaucher les sections (± 2 phrases) : frontières souples.
Il faut ajouter une dernière phase d’évaluation du système qui reporte le résultat de la précision.
La précision sera mesurée sur un corpus de test de 10 nouveaux articles PDF. Une partie de l’équipe
doit passer votre système sur les 10 articles, une autre doit établir le corpus de référence les frontières
(souples) des sections. Enfin, vous devez calculer (à la main si vous voulez être agiles) la précision de
votre système comme la moyenne sur l’ensemble des articles parsés. Finalement, un rapport doit être
écrit sous forme d’article scientifique. Cet article doit avoir les éléments suivantes :
• Titre
• Auteurs
• Abstract
• Méthode (explication du système)
• Résultats
• Conclusions
L’article doit être rédigé de préférence en Latex (bonus de +1pt) et doit être rendu en format PDF sur le
ENT (minimum 3, maximum 4 pages).

Les détailles sont dans le [sprint5](sprint5_carnet_du_produit.pdf). 

## **Execution du programme**
```sh
# Affichage de l'aide pour les options : 
python parser.py -h

# Pas d'option de sélection des fichiers à parser :
python parser.py CORPUS_TRAIN/ CORPUS_TXT/          # Format txt sans option
python parser.py -t CORPUS_TRAIN/ CORPUS_TXT/       # Format txt avec option
python parser.py -x CORPUS_TRAIN/ CORPUS_XML/       # Format xml 

# Sélection manuelle des fichiers à parser :
python parser.py -m CORPUS_TRAIN/ CORPUS_TXT/       # Format txt sans option
python parser.py -t -m CORPUS_TRAIN/ CORPUS_TXT/    # Format txt avec option
python parser.py -x -m CORPUS_TRAIN/ CORPUS_XML/    # Format xml
```
**Résultats attendus :**   
Le répértoire CORPUS_TXT/ contiendra les fichiers texte avec uniquement le nom du fichier, le titre et l'abstract  
Le répértoire CORPUS_XML/ contiendra les fichiers xml avec toutes les infos demandées pour le xml


## **Revu Sprint 4**

- Debrief sur le produit du troisième sprint mitigé. Le travail a été complexe mais effectué par chaque membre de la `SCRUM Team`.
- Liste de questions à donner au Scrum Master pour qu'il échange avec le client sur les besoins.
- Répartition des tâches selon les affinités de chacun. Bonne communication.
- Le code à correctement été refactor, ce qui permet aux développeurs de partir sur une base harmonisée.
- Les différents rendus des devs étaient très satisfaisant hormis pour Elvin qui à rendu un travail moyennement satisfaisant et en retard.
- Un problème commun aux développeurs semble être le manque de robustesses du aux différements formats possibles au seins des PDF.
  
## **Réunion planification Sprint 13/05/25**

![notes sur papier](images/reunion4.jpg)  
Retranscription :

- Échange avec le client pour connaître ses besoins par rapport à l'extraction des auteurs :
   - Le client souhaite-t-il que `discussion` et `evaluation` soient fusionnées ? La réponse est oui.
   - Que souhaite le client si une section est manquante dans le PDF originel ? La balise xml sera vide.
   - Que souhaite le client par rapport à une potentielle section de `remerciements` ? On l'ignore.
- Réalisation du backlog en priorité, puis des autres artefacts.

## **Backlog**

- Menu menu au début de l’exécution du système afin de choisir certains PDFs à parser au lancement.  
- Récupérer la section introduction.
- Récupérer la section corps.
- Récupérer la section discussion. 
- Récupérer la section conclusion. 
- Supprimer certaines redondances dans les fichiers de code.
- Améliorer les fonctionnalités du code.
- Réaliser les artefacts compris dans le conteneur de ce sprint 4.

## **Burndown**

![Exemple sortie](images/burndown4.jpg)

## _Consignes pour le compte rendu des développeurs_ :

- Déposez votre compte rendu au plus tard le mercredi 14/05/2025 à 16h sur la branche 4.
- Fournir AU MOINS une image de l’avancement par fonctionnalité par développeur.
- Votre compte rendu doit comporter une analyse de votre développement, les aspects positifs, négatifs, limitations… Vous pourrez vous baser sur le squelette pour vous guider si nécéssaire.
- Indiquer quel jour vous avez fini chaque fonctionnalité !

## **Travail de chaque menebre de la `SCRUM Team` pendant la mêlée (Revue Sprint)**

---

## 1. **Angelo Adragna** : Documentation des événements/artefacts Scrum (réunions de planification de sprint, mêlée quotidienne, revue de sprint, rétrospective du sprint).

- Les backlogs doivent être réalisés en premier lieu, lors de la première réunion, afin de répartir les tâches entre chaque personne.
- La réunion a permis d'établir la liste de questions pour le client, afin d'obtenir davantage de détails et de spécifications.
- Le Burndown se termine à la fin du sprint 4.
- La rédaction se fait au fil du sprint.
- Création d'un squelette de rendu pour facilier la mise en commun du travail de chacun. Je propose donc un modèle en raison du manque de détails dans les productions personnelles des développeurs.
- Médiation et conseils aux développeurs.

---

## 2. **Corentin Saccoman** : Récupération de la section `introduction` et réalisation du menu de sélection de fichiers.

### **2.1. Ajout du menu de sélection de fichiers**
   
#### **Analyse du code**
Afin de créer un menu permettant de choisir quel fichier parser ou non, un nouvel argument a été ajouté à la fonction `parse_arguments` :  
- **-m** (Pour menu). 
 
Ce nouvel argument est indépendant des autres et donc cumulable. Il fonctionne aussi bien pour le parsing au format **xml** que celui au format **txt**.  

Pour chaque fichier du répertoire d'entrée, le programme demande à l'utilisateur s'il désire le sélectionner ou non. Les réponses possibles sont les suivantes :  
- **Positives :**  
  - o, oui, y, yes, *touche entrée*
- **Négatives :**
  - n, non, no  
  
**REMARQUE :** La réponse n'est pas sensible à la casse.

C'est la fonction `list_pdfs` qui a été adaptée pour intégrer cette possibilité de choisir, en lui passant les options en paramètres.


#### **Exemples d'utilisation (complément du sprint 3):**
```sh
# Affichage de l'aide pour les options : 
python parser.py -h

# Pas d'option de sélection des fichiers à parser :
python parser.py CORPUS_TRAIN/ CORPUS_TXT/          # Format txt sans option
python parser.py -t CORPUS_TRAIN/ CORPUS_TXT/       # Format txt avec option
python parser.py -x CORPUS_TRAIN/ CORPUS_XML/       # Format xml 

# Sélection manuelle des fichiers à parser :
python parser.py -m CORPUS_TRAIN/ CORPUS_TXT/       # Format txt sans option
python parser.py -t -m CORPUS_TRAIN/ CORPUS_TXT/    # Format txt avec option
python parser.py -x -m CORPUS_TRAIN/ CORPUS_XML/    # Format xml
```
**Résultats attendus :**   
Le répértoire CORPUS_TXT/ contiendra les fichiers texte avec uniquement le nom du fichier, le titre et l'abstract  
Le répértoire CORPUS_XML/ contiendra les fichiers xml avec toutes les infos demandées pour le xml  

#### **Visualisation de l'exécution**
**Menu d'aide pour les options**  
<img src="images/menu_help_corentin.png" alt="Menu help options" width="720">

**Choix des fichiers**  
<img src="images/choix_fichiers_corentin.png" alt="Choix des fichiers" width="720">

#### **Pistes d'amélioration**
- Créer une fenêtre style TKinter afin d'avoir une représentation graphique et cliquable pour choisir les fichiers et le format de sortie (mais cela n'est pas demandé par le client).

#### **Analyse de performances**
L'ajout de cette option n'allourdit pas la consommation de ressources du parsing car elle n'intervient pas sur le processus d'analyse et de transformation du texte.

### **2.2. Récupération de la section `introduction`**
#### **Analyse du code**
Afin de réaliser le parsing de la section `Introduction` des fichiers pdf, j'ai créé le fichier `parser_intro.py` contenant la fonction suivante :  
```python
def extract_introduction(content: str) -> str:
    """
    Extrait la section 'Introduction' seule, jusqu'au début de la section suivante.
    Le texte est reformatté avec des retours à la ligne tous les ~100 caractères.
    """
```  
Comme indiqué dans la docstring, cette fonction récupère la section qui nous intéresse en se basant sur des expressions régulières. En effet, tous les fichiers (sauf une exception qui confirme la règle) contiennent une numérotation de leurs sections :  
- `1 `..., `2 `..., `3 `...
- `1. `..., `2. `..., `3. `...
- `I. `..., `II. `..., `III. `...

En conséquence, la récupération se déroule de la manière suivante :
- Découpage du texte ligne par ligne.
- Le programme détermine à partir de quelle ligne commence l'introduction grâce à une expression régulière.
- Le programme cherche l'expression exacte `A noisy-channel model for sentence compression` pour que l'exécution fonctionne aussi sur le fichier *marcu_statistics_sentence_pass_one.pdf* qui ne contient pas de numérotation. Dans ce cas, il détermine la ligne où se trouve cette expression pour pouvoir découper la partie qui nous intéresse et enlever le reste.
- S'il n'a pas trouvé l'expression exacte précédente, il cherche un pattern commançant par le chiffre deux (2, 2. ou II.) afin d'isoler la partie suivante, à laquelle la récupération s'arrêtera.  


La fonction `extract_introduction` est appelée dans le programme `parser.py` en même temps que celles correspondant aux autres balises afin d'intégrer l'introduction au xml.

<img src="images/parsing_intro_corentin.png" alt="Parsing de l'introduction" width="720">

#### **Pistes d'amélioration**
- Essayer de trouver un moyen de ne plus avoir recours à une expression régulière spécifique à un fichier. En clair, trouver un moyen de parser l'introduction quand les sections ne sont pas numérotées (très complexe en l'état).

#### **Analyse de performances**
Le processus de parsing prend tout de suite plus de temps, étant donné qu'on rajoute du traitement. Mais cela reste largement acceptable et ne ralentit pas drastiquement le programme.

#### **Remarques**
Durant l'analyse, les traits d'union permettant d'unifier des mots séparés entre deux lignes sont bien gérés afin de les réunifier. Cela n'a pas d'incidence sur les mots composés classiques.

### **Dates clés :**
- 12/05/2025 : Fin du développement et de l'intégration du menu de choix des fichiers.
- 12/05/2025 : Fin de la récupération de la section d'introduction.


  ---

## 3. **Elliot Pozucek** : Récupération de la section `corps` de chaque fichier.

### Analyse du code

#### Général

Afin de détecter correctement les parties à inclure dans le corps, j'ai analysé pour chaque fichier les *headers* de chaque section. J'ai ensuite compilé les sections qui m'intéressaient pour le corps. Voici l'analyse :
| Nom du fichier                          | Section Intro       | Section Début Corps                          | Section Fin Corps               |
|-----------------------------------------|---------------------|----------------------------------------------|----------------------------------|
| ACL2004-HEADLINE.txt                    | 1 Introduction      | 2 Previous Work                              | 6 Conclusions and Future Work   |
| Boudin-Torres-2006.txt                  | 1 Introduction      | 2 Method                                     | 4 Discussion and Future Work    |
| compression_phrases_Prog-Linear-jair.txt| 1. Introduction     | 2. Related Work                              | 6. Conclusions                  |
| compression.txt                         | 1 Introduction      | 2 Related Work                               | 7 Future Work                   |
| hybrid_approach.txt                     | 1 Introduction      | 2 From Full Sentence to Compressed          | 4 Conclusion                    |
| marcu_statistics_sentence_pass_one.txt  | Introduction        | A noisy-channel model for sentence          | Evaluation                      |
| mikheev.txt                             | 1. Introduction     | 2. Performance Measure, Corpora for Evaluation, and Intended Markup | 13. Discussion                  |
| probabilistic_sentence_reduction.txt    | 1 Introduction      | 2 Support Vector Machine                    | 5 Experiments and Discussion    |
| Stolcke_1996_Automatic_linguistic.txt   | 1. INTRODUCTION     | 2. THE IMPORTANCE OF LINGUISTIC SEGMENTATION| 6. DISCUSSION                   |
| Torres.txt                              | I. INTRODUCTION     | II. RELATED WORK                             | VI. CONCLUSIONS AND FUTURE WORK |
| Word2Vec.txt                            | 1 Introduction      | 2 Model Architectures                        | 6 Conclusion                    |

Avec cette analyse, j'ai pu identifier les paternes Regex que je peux implémenter afin de recupérer le corps de chaque fichier.

Le corps du texte est détecté de la manière suivante :

- on détecte la section d'introduction (qui est toujours présente)
- on détecte la section suivante (grâce au code de Corentin)
- on détecte la section de fin à l'aide de mots-clés hardcodés (ex: *Conclusion*, *Discussion*, *Future Work*, etc.)
- on extrait le corps entre la section après l'introduction et la section de fin
- on formate le corps pour qu'il soit bien et beau dans le xml (ajout de tabulation tous les ~100 caractères)
- on écrit le corps dans le fichier xml

Afin d'illustrer le bon fonctionnement du programme, voici quelques images :

Dans le pdf, on voit que la section de conclusion commence juste après "*tracking for each method.*".

![](images/img1_elliot.png)

Dans le xml, on retrouve bien cette phrase à la fin du corps :

![](images/img2_elliot.png)

#### Paternes de début

J'ai d'abord essayé de trouver une méthode robuste pour identifier le header de la section directement après l'introduction (ex: II. RELATED WORK), mais sans succès. J'ai donc décidé de me concentrer sur les paternes de fin.

Pour les paternes de début de corps, j'ai tout simplement inclus l'introduction dans le corpus, en utilisant un paterne Regex permettant de détecter le header de la section d'introduction.

Une fois la partie de Corentin terminée, j'ai intégré son code de détection de la section qui suit directement la section d'introduction.

```python
  intro_patterns = [
      r"^\s*\d{0,2}\.?\s*(Introduction|INTRODUCTION)\b",
      r"^\s*[IVX]{0,3}\.?\s*(Introduction|INTRODUCTION)\b"
  ]
  ```

Puis le paterne pour détecter la section d'après :

```python
next_section_pattern = r"^\s*(?:2|II)\.?\s+[A-Z][^\n]{0,100}$"
  ]
```

Merci à Corentin pour son aide sur cette partie !

#### Paternes de fin

Voici les paternes que j'ai codés pour détecter les dernières sections du corps d'un article.  
Ces sections délimitent la fin du corps que l'on souhaite extraire, et sont basées sur la présence explicite de mots-clés caractéristiques d'une conclusion.

Les mots-clés pris en compte sont les suivants (insensibles à la casse) :

```python
  end_keywords = [
      "Conclusion", "Discussion", "Future Work", "Conclusions", "Evaluation",
      "Conclusions and Future Work", "Discussion and Future Work",
      "CONCLUSIONS", "DISCUSSION", "FUTURE WORK"]
```

Une fois ces mots-clés identifiés, j'ai utilisé des expressions régulières pour les détecter dans le texte.

Je les ai regroupés en trois paternes différents, afin de couvrir les différents cas de figure que l'on peut rencontrer dans le corpus.

##### Paternes utilisés :


```python
rf"^\s*\d{{1,2}}\.?\s+({'|'.join(re.escape(keyword) for keyword in end_keywords)})\s*$",
```

Ce paterne détecte les titres de section numérotés, comme :

- `6 Conclusion`
- `12. Evaluation`
- `5 Future Work`
- `6. DISCUSSION`

Je considère les majuscules et minuscules (sans utiliser *ignorecas*) car cela simplie grandement la détection des *headers* de section.


```python
rf"^\s*[IVX]+\.\s+({'|'.join(re.escape(keyword.upper()) for keyword in end_keywords)})\s*$",
```

Ce paterne permet de détecter les titres de section avec une numérotation romaine, comme par exemple :

- `VI. CONCLUSIONS`
- `IV. DISCUSSION`

En pratique, un seul des fichiers du corpus présente ce paterne.


```python
rf"^\s*({'|'.join(re.escape(keyword) for keyword in end_keywords)})\s*$"
```

Ce dernier paterne couvre les cas où la section est indiquée sans numérotation :

- `Conclusion`
- `Evaluation`
- `Discussion`

Il s'applique uniquement si ces mots apparaissent seuls sur leur ligne (la casse doit être strictement respectée).



#### Tests unitaires

Lors du développement de mon programme, j'ai vite trouvé pénible de devoir vérifier à la main le contenu des fichiers XML générés pour vérifier que le corps extrait était correct.

J'ai donc décidé de créer un fichier de test unitaire, `test_parser_corps.py`, qui vérifie que le corps extrait est bien celui attendu.
Dans ce fichier, un dictionnaire contient les noms de chaque fichier xml et les 5 premiers mots et les 5 derniers mots du corps qui doivent être présents dans le fichier xml.

Voici un exemple :

```json
"ACL2004-HEADLINE.xml": {
    "start": "2 Previous Work Hedge Trimmer",
    "end": "event tracking for each method."
},
```

J'ai ensuite fait une fonction qui compare le corps extrait avec le corps attendu, en vérifiant que les 5 premiers et 5 derniers mots correspondent :

```python
first = " ".join(text.split()[:5])
last = " ".join(text.split()[-5:])

if first != expected["start"]:
    print(f"[ÉCHEC] Début incorrect dans {filename}\n  Attendu: '{expected['start']}'\n  Obtenu : '{first}'")
    all_passed = False
if last != expected["end"]:
    print(f"[ÉCHEC] Fin incorrecte dans {filename}\n  Attendu: '{expected['end']}'\n  Obtenu : '{last}'")
    all_passed = False
```

Ce programme m'a énormément aidé et m'a fait gagner beaucoup de temps. En effet, à chaque modification de mon code dans le parser, je n'avais qu'à lancer le test unitaire pour vérifier que tout fonctionnait correctement.

Afin d'utiliser ce programme de test, il suffit de l'éxécuter comme suit :

```bash
python3 test_parser_corps.py CORPUS_XML/
```


### Pistes d'amélioration

Il a été décidé lors du *product backlog* que l'introduction ne faisait pas partie du corps, donc ma solution initiale ne respectait pas vraiment les consignes.

Cependant, grâce au travail de Corentin, j'ai pu récupérer la section qui suit l'introduction, ce qui m'a permis de respecter les consignes.

Toutefois, les solutions mises en place pour détecter les différentes sections sont très peu robustes. En effet, elles reposent sur des mots-clés hardcodés et des expressions régulières qui ne prennent pas en compte toutes les variations possibles de la structure des articles. Si l'on venait à tester notre programme sur des articles non présents dans notre corpus de test, il est probable que le programme ne fonctionne pas correctement.


### Analyse de performances

Mon programme n'a pas augmenté le temps d'éxécution sur ma machine (toujours autour de 1 seconde). À voir avec les autres parties du sprint-4.


### **Remarque**

La version actuelle est 100% fonctionnelle pour tous les fichiers du corpus.


### Dates clés :

### 12/05 :
 - création de `parser_corps.py`
   - ajout de la récupération du corps de chaque fichier, de l'introduciton (incluse) à la dernière section (soit la *conclusion*, soit *discussion*, soit *futur work*)
   - ajout de la mise en forme du corps pour qu'il soit bien et beau dans le xml
   - ajout de l'écriture du corps dans le fichier xml

### 13/05 :
 - modification de `parser_corps.py`
   - ajout de la détection de la section qui suit l'introduction (grâce à Corentin)
   - refactoring du code pour le rendre plus lisible (notamment les paternes de fin du corps)
   - intégration du code de Corentin pour le nettoiement du texte (+ robuste)
   - documentation de l'ensemble du code de `parser_corps.py`
 - création de `test_parser_corps.py`
   - ajout de tests unitaires vérifiant que le corps est bien celui attendu

 
  ---

## 4. **Colin Palazzetti Rubera** : Récupération de la section `discussion` (`evaluation`) et s'occupe de la redondance de certains codes.

### Partie récupération
La partie discussion/évaluation n'est présente que dans très peu d'articles :
![](images/discussion_work.png)
La présence d'une fonction de test locale permet de bien identifier (et notamment via la génération d'un markdown qui résume les trouvailles) les points à améliorer :
![](images/discussion_dev.png)
Néanmoins, la présence de possible détection de fin avant le début, il a fallu débug pour comprendre ça :
![](images/discussion_debug.png)
Cela a permis de détecter ce problème et de le corriger en requérant le début pour chercher la fin

Et vu que pour mes tests j'ai limité à un seul fichier, ça ne marchait évidemment pas pour les autres (5 minutes de perdues) :
![](images/discussion_betise.png)


### Analyse du code
- Optimisation des regex
- vérification de l'optimisation des if
- vérification de l'optimisation des affectations de variables

### Pistes d'amélioration
IL y aura toujours moyen d'améliorer, dans les idées en vrac
- Faire un menu interactif pour le choix des pdf à traiter :
```
[ ] pdf 1
[ ] pdf 2
[x] pdf 3
[x] pdf 4
[ ] pdf 5
```

### Analyse de performances
Les performances moins bonnes de python sont compensées par une simplicité de lecture

Pour ce qui est de l'optimisation, j'ai essayé de rassembler les regex lorsque c'était possible et de retirer des affectations qui se suivent :
```py
a += b
a += c
a += d
```
devient
```py
a += b + c + d
```


### **Remarque**
Pour gagner du temps dans l'harminisation, il aurait fallu mettre une structure de base pour les parties (`parser_xxx.py`), qui aurait permis d'avoir directement une consistence.

Ceci n'aurait été possible que si les potentielles améliorations demandées avaient été présentées par le client au départ (et pas une idée floue de l'attendu)


### Dates clés :
12/05 : découverte du travail et premières reflexion

13/05 : relecture du code et ajout des optimisations

14/05 : relecture du code et ajout des optimisations, rédaction du README
 
  ---

## 5. **Elvin Fichot-Corgeron** : Récupération de la section `conclusion` (`Travaux à venir` ou `Perspectives`).


Pour ce sprint j'ai eu pour tâche de récupérer la section conclusion dans le texte

### Approche du travail :

Pour rechercher la section je recherche les différents titre possibles (Conclusion, Future Work ...)

Ensuite je récupère tous le texte jusqu'à trouver la prochaine section qui est forcément Acknowledgments ou References.

Ensuite je supprime les lignes non essentielles tel que le numéro de pages le nom de l'auteur ...

### **Dévelepement**

J'ai développé 3 méthodes pour parvenir à l'extraction

`get_string`, `build_section_regex` et `clean_string`

#### `get_string`

Cette méthode est la méthode principale qui va renvoyé la section au parseur. Dans cette méthode je trouve la section de début de la conclusion et la section de fin. Je récupère ensuite le texte qui est entre les 2 je retire les éléments inintérrssant et renvoie le texte

#### `build_section_regex`

Dans cette méthode j'identifie le pattern d'une section avec une regex. Cette méthode a été crée pour éviter de dupliquer du code pour chercher le pattern d'une section, le début et la fin.

#### `clean_string`

Dans cette méthode je retire les lignes inutiles tels que les noms d'auteurs où les numéros de page.

#### Résultats

La conclusion dans les pdf ressemble à ça :

![](images/ConclusionPdf.PNG)

Ensuite après le parsing j'obtient ce résultat :

![](images/ConclusionXML.PNG)

## **Remarque**

### Erreurs

Dans cette première version la conclusion n'est pas extraite correctement pour un seul fichier. En effet dans un fichier on a le titre qui se trouve au milieu de la version. Et il contient le mot References

`Summary Evaluation with and without References`

Je n'ai pas réussi à faire en sorte que l'exclusion ne soit pas pris en compte pour cette ligne.

### Piste d'amélioration

Je pense que le je pourrais améliorer la robustesse dans la recherche des sections de début et de fin afin d'être plus efficace et de couvrir correctement tous les cas.

### Analyse des performances

Le temps d'éxécution du programme n'a pas changé et reste le même que sans la recherche de la conclusion

## **Dates clés** :

- 12/05 : Lancement du sprint 4

- 13/05 : Première version terminé

 
  ---

## **Retour sur le travail effectué (Rétrospective Sprint 4)**

### **Ce que nous avons déterminé**
- Le menu au début de l’exécution du système sera implémenté afin de permettre à l'utilisateur de sélectionner les fichiers PDF à parser, plutôt que de traiter un répertoire complet.
- La section `discussion` et `evaluation` seront fusionnées dans un seul élément XML `discussion`, selon la demande du client.
- En cas de section manquante dans un PDF, la balise XML correspondante sera laissée vide, sans générer d'erreur ni d'exception.
- La section `remerciements` sera ignorée et ne sera pas incluse dans le rendu XML.
- Le format XML sera enrichi pour inclure les sections `introduction`, `corps`, `conclusion`, et `discussion`, conformément à la structure demandée par le client.
- Les balises XML seront organisées de manière à correspondre aux sections exactes présentes dans le document, sans introduire de nouvelles sections non demandées.
- La priorité sera donnée à la compatibilité des fonctionnalités avec le format des fichiers PDF utilisés, en tenant compte des différentes variantes possibles de structure.

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
