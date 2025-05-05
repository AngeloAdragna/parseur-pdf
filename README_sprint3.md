# Sprint 3

**Auteurs : L3 CMI Informatique**

- Angelo Adragna
- Corentin Saccoman
- Elliot Pozucek
- Colin Palazzetti Rubera
- Elvin Fichot-Corgeron

<!--pandoc README_sprint1.md -o README_sprint1.pdf --pdf-engine=xelatex-->

## **Rôles**
- Angelo est le maître de `SCRUM` et le `Product Owner`, il doit réaliser la rédaction du rapport avec les différents artéfacts.
- Corentin, Elliot, Colin et Elvin sont développers.
- Corentin doit s'occuper de l'intégration du fonctionnement xml depuis l'option de lancement jusqu'à l'écriture des balises.
- Elliot doit récupérer la section bibliographique t renvoyer un plain texte.
- Colin doit harmoniser les différents fichiers.
- Elvin doit récupérer la section de l'auteur et renvoyer un plain texte.

## **Objectif**
Suite à une discussion au LIA, nous avons décidé que les fichiers parsés plein texte ne suffisent plus à
nos besoins. Nous avons entendu parler que les fichiers structurés XML possèdent plusieurs avantages
et qu’ils sont largement utilisés en TAL. Nous préférons donc comme sortie un fichier XML utf8 avec
la structure suivante:
```xml
<article>
 <preamble> Le nom du fichier d’origine </preamble>
 <titre> Le titre du papier </titre>
 <auteur> La section auteurs et leur adresse </auteur>
 <abstract> Le résumé de l’article </abstract>
 <biblio> Les références bibliographiques du papier</biblio>
</article>
```
Cependant quelques chercheurs veulent garder la sortie texte aussi… Cette nouvelle sortie .xml
complète la sortie texte .txt du sprint précédent.
Ainsi, au moment de lancer votre parseur, il faudra ajouter un argument ( -t | -x ) pour bien choisir le
type de sortie : soit générer des fichiers dans une version texte (-t) , soit au format XML (-x)
Les détailles sont dans le [sprint3](sprint3_carnet_du_produit.pdf).

## **Execution du programme**


## **Revu réunion, planification Sprint 05/05/25**
   



## **Backlog**
 - Option xml au lancement (plain texte par défaut) et tranduction texte xml.
 - Récuperer section auteur.
 - Récuperer section bibliographique.
 - Harmoniser fichiers de codes.
 - Améliorer fonctionnalités du code.
 - Réaliser artefacts compris dans le conteneur de ce Sprint 3.


## **Burndown**
![Exemple sortie](images/burndown-2.png)  


## _Consignes pour le compte rendu des développeurs_ : 
- Déposez vos comptes rendu au plus tard le 09/05/2025 à 18h sur la branche 3.
- Fournir au moins 1 image de l'avancement par fonctionnalité par développer.
- Votre compte rendu doit comporter un analyse de votre développement, les aspects positifs, négatifs, limitations...
- Indiquer quel jour vous avez fini vos fonctionnalités.

## **Travail de chaque codeur pendant la mêlée (Revue Sprint)**

---

1. **Angelo Adragna** : documenter les événements/artefacts Scrum (réunions de planification de sprint, mêlée quotidienne, revue de sprint, rétrospective du sprint) :
   - Les backlogs doivent être réalisés en premier lieu, lors de la première réunion, afin de répartir les tâches entre chaque personne.
   - Chaque réunion a bien permis d'éclaircir les zones d'ombre sur le projet et le travail de chacun. Cela a également permis d'établir une liste de questions pour le client, afin d'obtenir davantage de détails et de spécifications.
   - Le Burndown est facile à réaliser à la toute fin du sprint.
   - La rédaction doit cependant se faire au fur et à mesure de l'avancement de chacun.
   - La mise en commun du travail de chacun peut parfois s'avérer ardue, en raison du manque de détails dans le fonctionnement des productions personnelles des développeurs.
   - Attention à ne pas mettre une deadline trop proche de la fin du sprint, même si l'idée était de laisser un maximum de temps aux développeurs. Cela les a poussés à rush à la fin, car certaines tâches dépendaient de la finalisation d'autres tâches.


---

2. **Corentin Saccoman** :  L'intégration du fonctionnement xml depuis l'option de lancement jusqu'à l'écriture des balises.

   
### Analyse du code


### Pistes d'amélioration


### Analyse de performances

   
### **Remarque** 
   
 ---

3. **Elliot Pozucek** : Récupération de la section bibliographique et renvoit dans un plain texte.

### Analyse du code


### Pistes d'amélioration


### Analyse de performances

   
### **Remarque** 


---

4. **Colin Palazzetti Rubera** : Harmonisation des différents fichiers de code avec notamment la docstring Numpydoc.

### Analyse du code


### Pistes d'amélioration


### Analyse de performances

   
### **Remarque** 


---

5. **Elvin Fichot-Corgeron** : Récupération de la section de l'auteur et renvoit dans un plain texte.

### Analyse du code


### Pistes d'amélioration


### Analyse de performances

   
### **Remarque** 


---

## **Retour sur le travail effectué (Rétrospective Sprint 2)**
- Debrief sur le produit du second sprint assez positif. Le travail a été complexe mais correctement effectué par chaque membre de la `SCRUM Team`.
- Liste de questions à donner au Scrum Master pour qu'il échange avec le client sur les besoins.
- Répartition des tâches selon les affinités de chacun. Bonne communication et cohésion d'équipe.
- Questionnement refactor et harmonisation des fichiers pour une meilleur lisibilité et compréhension.
- Les artéfacts ne semblent ne plus poser de problèmes, bien qu'un léger doute plane encore. Cependant la méthode SCRUM est volontairement peu détaillé donc cela semble naturel.
- Les différents rendus des devs etaient trop proche du rendu du produit du sprint 2.
- Très bonne cohésion d'equipe. Elliot à réalisé un acte d'entraide remarquable. En effet Corentin à eu un imprevu ce qui fait qu'il aurait été en retard sur la réalisation de son compte rendu, c'est donc Elliot qui s'est volontairement proposé pour réalisé le susdit compte rendu.
  
### **Ce que nous avons déterminé**
Après avoir comparé les temps d'exécution entre une version Python et une version C++ du parseur, nous avons néanmoins choisi de continuer en Python.  
En effet, comme nous pouvons le voir dans le travail d'Elliot et Corentin, Python peut s'avérer légèrement plus lent, cependant, la différence est négligeable.  
Nous avons opté pour une base en Python de manière unanime, tant par préférence des développeurs que pour le large choix de bibliothèques Python pour le traitement des données, mais aussi pour la fiabilité de Python.  
Ce choix s'inscrit dans une démarche de projection sur les futures tâches à réaliser.

### **Ce qui a bien fonctionné**
Nous avons réussi à remplir toutes les demandes présentes dans le backlog.

### **Ce qui a posé problème**
Au niveau du développement, le principal problème a été d'identifier le début et la fin des différentes zones de titre et d'abstract, sachant que ces zones ne sont pas toujours déclarées de façon précise. Notamment pour le fichier `mikheev.pdf`, où le titre récupère uniquement la lettre 'c'.  
Au niveau organisationnel, la deadline imposée par le Scrum Master pour la finition du code et du compte rendu par les développeurs était trop proche de la date de rendu au client.  
Cela a poussé toute l'équipe à effectuer un rush final.

### **Ce qu’on doit améliorer**
Les comptes rendus de certains développeurs ne répondent pas entièrement aux attentes détaillées dans les consignes.

---

### **Conclusion** :
Le travail global effectué par l'équipe est satisfaisant.  
Le travail des personnes impliquées est efficace et très satisfaisant.  
La communication est bonne, et l'on distingue une réelle amélioration dans le travail de chacun, tant au niveau de la qualité que de la quantité.

