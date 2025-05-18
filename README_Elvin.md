# Sprint 5 Elvin FICHOT--CORGERON

## Tâche : Analyse des résultats

Le but de ma tâche est d'analyser les résultats trouvés par le parseur pour ensuite les comparer avec les frontières souples et ainsi calculer le score de précision.

Le score de précision se calcule avec la formule suivante :

$ Précision = nbsectioncorrectes/sectiontrouvé$

Pour rappel, on considére qu'une section est correcte si elle est dans la frontière souple (au plus 2 lignes d'écart avec la frontière stricte)

### Dynamical_Models_Explaining_Socia_Balance_and_Evolution_of_Cooperation

#### Frontières souples

- Titre : L1-2 valide
- Auteur : L2-7 + L19-~32 non valide
- Abstract : L8- ~32 non valide
- Introduction : L33- ~607 non valide
- Corps : L~608-~780 non valide
- Conclusion : L507-556 valide
- Discussion : Il n'y a pas de discussion
- Biblio : L790-892 valide

#### Précision

Il y a au total 7 sections et nous en trouvons 3 de correctes.

Le taux de précision est donc de 3/7 = 0.43

### Exact_Clustering_via_Integer_Programming_and_Maximum_Satisfiability

#### Frontières souples

- Titre : L1-2 : valide
- Auteur : L3-14 valide recupère bien toutes les informations même si certaines sont dupliqués
- Abstract : L16-37 valide
- Introduction : L39-172 non valide
- Corps : L173-922 non valide
- Conclusion : L924-964 valide (souple)
- Discussion : Pas de discussion dans le document
- Biblio : L971-1063 valide (souple)

#### Précision

Il y a au total 7 sections et nous en trouvons 5 de correctes.

Le taux de précision est donc de 5/7 = 0.71

### LDA_resume

#### Frontières souples

- Titre : L1-2 valide
- Auteur : L3-18 non valide il manque plusieurs lignes qui ne sont pas détecter
- Abstract : L20-37 valide
- Introduction : L39-104 valide
- Corps : L105-796 non valide
- Conclusion : L798-811 valide
- Discussion : L666-796 valide
- Biblio : L813-877 valide

#### Précision

Il y a au total 8 sections et nous en trouvons 6 de correctes.

Le taux de précision est donc de 6/8 = 0.75

### Partitioning_large_signed_two-mode_networks_Problems_and_prospects

#### Frontières trouvés par le parseur

- Titre : en tête de document non valide
- Auteur : L1 non valide
- Abstract : L3 non valide
- Introduction : L36-117 valide
- Corps : L118-1739 valide
- Conclusion : Pas de conclusion dans le document
- Discussion : L1740-1819 valide
- Biblio : L2069-2192 valide (souple)

#### Précision

Il y a au total 7 sections et nous en trouvons 4 de correctes.

Le taux de précision est donc de 4/7 = 0.57

### Polibits_42_02

#### Frontières souples

- Titre : L1-2 : valide
- Auteur : L3 : valide
- Abstract : L4-18 : valide
- Introduction : L33-82 valide
- Corps : L135-552 : non valide
- Conclusion : L554-566 : non valide
- Discussion : L512-552 : valide
- Biblio : L661-746 : valide

#### Précision

Il y doit y avoir en tout 8 sections nous en trouvons 6 de correctes.

Le taux de précision est donc de 6/8 = 0.75

## Remarque

Pour ce sprint j'ai rencontré une petite difficulté notament pour évaluer les auteurs. En effet il avait été convenu au sprint 2 de noter les auteurs de la manière suivante : _nom_ _adresses_ (universitaire et mail si précisés) Cependant, cette notation n'était pas en accord avec la manière de déterminer si une section est correcte. J'ai donc regardé bien en détails les lignes pour voir si les informations étaient plutôt cohérentes et essayé de me rapprocher au plus de la marge de souplesse déterminée.

Lorsque que j'ai noté les ~ pour les lignes c'est que la marge d'erreur est bien plus grande que 2 lignes et que cela ne changera pas le résultat.

## Retrospective sur le projet en entier

De mon point de vue, j'ai trouvé le projet très intéressant. Il démontre clairement la nécessité pour un développeur d'avoir un code robuste, car le projet peut évoluer à n'importe quel moment. Pour ce qui est de la méthode Scrum, j'ai déjà eu l'occasion de travailler avec aussi bien lors de plusieurs projets dans mon ancienne formation ou bien aussi en entreprise lors de mon alternance.
