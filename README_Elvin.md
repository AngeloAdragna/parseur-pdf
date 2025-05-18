# Sprint 5 Elvin FICHOT--CORGERON

## Tâche : Analyse des résultats

Le but de ma tâche est d'analyser les résultats trouvés par le parseur pour ensuite les comparer avec les frontières souples et ainsi calculer le score de précison.

Le score de précision se calcule avec la formule suivant :

$ Précision = nbsectioncorrectes/sectiontrouvé$

Pour rappel on considére qu'on section est correcte si elle est dans la frontière souple (au plus 2 lignes d'écart avec la frontière stricte)

### Polibits_42_02

#### Frontières souples

- Titre : L1-2 : valide
- Auteur : L3 : valide
- Abstract : L4-18 : valide
- Introduction : Non trouve par le parseur : non valide
- Corps : L 135 - 552 : non valide
- Conclusion : L 554 - 566 : non valide
- Discussion : L 512 - 552 : valide
- Biblio : L661-746 : valide

#### Précision

Il y doit y avoir en tous 8 sections nous en trouvons 5 de correctes.

Le taux de précision est donc de 5/8 = 0.625

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

## Remarque

Pour ce sprint j'ai rencontré une petite difficulté nottement pour évaluer les auteurs. En effet il avait été convenu au sprint 2 de noter les auteurs de la manière suivante : _nom_ _adresses_ (universitaire et mail si précisés) cepedant cette notation n'était pas en accord avec la manière de déterminer si une section est correct. J'ai donc regarder bien en détails les lignes pour oir si les informations était plutôt cohérente et essayer de me rapprocher au plus de la marge de souplesse déterminé.

Lorsque que j'ai noté les ~ pour les lignes c'est que la marge d'erreur est bien plus grande que 2 lignes et que cela ne changera pas le résultat.

## Retrospective sur le projet en entier

De mon point de j'ai trouvé le projet très intérressant. Il démontre clairement la néccéssité pour un développeur d'avoir un code robuste, car le projet peux évoluer à n'importe qu'elle moment. Pour ce qui est de la méthode Scrum j'ai déjà eu l'occasion de travailler avec aussi bien lors de plusieurs projet dans mon ancienne formation ou bien aussi en entreprise lors de mon alternance.
