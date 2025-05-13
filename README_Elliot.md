## **Elliot Pozucek** : Récupération du corps de chaque fichier.

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

---

```python
rf"^\s*\d{{1,2}}\.?\s+({'|'.join(re.escape(keyword) for keyword in end_keywords)})\s*$",
```

Ce paterne détecte les titres de section numérotés, comme :

- `6 Conclusion`
- `12. Evaluation`
- `5 Future Work`
- `6. DISCUSSION`

Je considère les majuscules et minuscules (sans utiliser *ignorecas*) car cela simplie grandement la détection des *headers* de section.

---

```python
rf"^\s*[IVX]+\.\s+({'|'.join(re.escape(keyword.upper()) for keyword in end_keywords)})\s*$",
```

Ce paterne permet de détecter les titres de section avec une numérotation romaine, comme par exemple :

- `VI. CONCLUSIONS`
- `IV. DISCUSSION`

En pratique, un seul des fichiers du corpus présente ce paterne.

---

```python
rf"^\s*({'|'.join(re.escape(keyword) for keyword in end_keywords)})\s*$"
```

Ce dernier paterne couvre les cas où la section est indiquée sans numérotation :

- `Conclusion`
- `Evaluation`
- `Discussion`

Il s'applique uniquement si ces mots apparaissent seuls sur leur ligne (la casse doit être strictement respectée).

---

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

---

### Pistes d'amélioration

Il a été décidé lors du *product backlog* que l'introduction ne faisait pas partie du corps, donc ma solution initiale ne respectait pas vraiment les consignes.

Cependant, grâce au travail de Corentin, j'ai pu récupérer la section qui suit l'introduction, ce qui m'a permis de respecter les consignes.

Toutefois, les solutions mises en place pour détecter les différentes sections sont très peu robustes. En effet, elles reposent sur des mots-clés hardcodés et des expressions régulières qui ne prennent pas en compte toutes les variations possibles de la structure des articles. Si l'on venait à tester notre programme sur des articles non présents dans notre corpus de test, il est probable que le programme ne fonctionne pas correctement.

---

### Analyse de performances

Mon programme n'a pas augmenté le temps d'éxécution sur ma machine (toujours autour de 1 seconde). À voir avec les autres parties du sprint-4.

---

### **Remarque**

La version actuelle est 100% fonctionnelle pour tous les fichiers du corpus.

---

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