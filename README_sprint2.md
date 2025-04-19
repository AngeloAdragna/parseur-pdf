# Sprint 2

**Auteurs : L3 CMI Informatique**

- Angelo Adragna
- Corentin Saccoman
- Elliot Pozucek
- Colin Palazzetti Rubera
- Elvin Fichot-Corgeron

<!--pandoc README_sprint1.md -o README_sprint1.pdf --pdf-engine=xelatex-->

## **Rôles**

- Angelo est le maître de `SCRUM`.
- Corentin doit créer la structure de l'algorithme en prenant en paramètre un dossier pdf, appelant les différentes méthodes et en renvoyant un dossier de txt.
- Elliot doit traiter le nom du fichier d'orgine.
- Colin doit traiter le résumé (abstract) de l’auteur.
- Elvin doit traiter le titre du papier.

## **Objectif**
Dans la séance précédente vous avez choisit le convertisseur le plus adapté PDF→texte. Il s’agit
maintenant d’analyser les articles plain texte par le parseur. Il sera développé dans un langage adéquat,
et analysera les sorties textuelles du convertisseur.
Nous voulons comme sortie un fichier .txt par fichier ayant les sections et la structure suivante.
Les détailles sont dans le [readme](sprint2_carnet_du_produit.pdf).

## **Réunion**
- Debrief sur le produit du premier sprint assez positif, malgré une légère dissipation due à des zones d'ombres sur la consigne.
- Répartition des tâches.
- Liste de questions à donner au Scrum Master pour qu'il échange avec le client sur les besoins.

## **Backlog**
 - Le système doit traiter un dossier contenant des fichiers PDF, créer un sous-dossier pour stocker les sorties en texte brut avec les mêmes noms que les fichiers PDF, et supprimer le       sous-dossier s’il existe déjà.
 - Générer un fichier en texte brut en sortie.
 - Afficher le nom du fichier d’origine sur une ligne, avec les espaces remplacés par des underscores (“_”).
 - Afficher le titre de l’article sur une ligne.
 - Afficher le résumé (abstract) de l’auteur sur une ligne.

Le langage doit être choisi en fonctions des critères :
   1/ Maîtrisé par les membres de l’équipe
   2/ Performance en temps d’exécution


## **Burndown**

## **Revu réunion 09/04/25**
 - Répartition des tâches selon les affinités de chacun. Bonne communication et cohésion d'équipe.
 - Discussion et explication des différents artéfacts :
    - Le carnet du produit (Product Backlog) : liste priorisée de toutes les fonctionnalités à développer pour le produit.
    - Le carnet du sprint (Sprint Backlog) : ensemble des tâches sélectionnées pour être réalisées pendant un sprint.
    - L’incrément : version du produit incluant toutes les fonctionnalités terminées à la fin d’un sprint.
    - Les fonctionnalités (User Story) : descriptions simples des besoins utilisateurs, exprimées du point de vue de l’utilisateur.
    - Le diagramme de progression (Sprint Burndown Chart) : graphique montrant l’évolution du travail restant à faire pendant le sprint. 

## **Revu réunion 11/04/25**
 - Soucis pour identifier le debut et la fin des différentes zones de titre et de abstract sachant, que les zones ne sont pas toujours déclarées de façon précises.


## _Consignes_ : 
- Déposez vos comptes rendu au plus tard le 18/04/2025 à 20h sur la branche 2
- Fournir au moins une image de l'avancement par fonctionnalité.
- Votre compte rendu doit comporter un analyse de votre développe, les aspects positifs, négatifs, limitations...
- Vous devez comparer le temps d'exécution de votre fonctionnalité en python et en C++
- Indiquer quel jour vous avez fini votre fonctionnalité

## **Travail de chaque codeur pendant la mêlée (Revue Sprint)**

---

1. **Angelo Adragna** : documenter les événements/artefacts Scrum (réunions de planification de sprint, mêlée quotidienne, revue de sprint, rétrospective du sprint)
   - **Appréciation générale** :  
   - **Note** :
   
---

2. **Corentin Saccoman** : Structure de l'algorithme de prenant en paramètre un dossier de pdf et appelant les différentes fonctions des autres menbres de l'équipe .
   - **Appréciation générale** :  
   - **Note** :  

---

3. **Elliot Pozucek** : Traitement du nom du fichier d'orgine.
   - **Appréciation générale** :  
   - **Note** :  

---

4. **Colin Palazzetti Rubera** : Le résumé (abstract) de l’auteur.
   - **Appréciation générale** :  
   - **Note** :  Lors de la lecture des résumés donnés : 
      - Certains mots sont coupés par le passage à la ligne, mais dans d'autres cas il s'agit d'un mot composé. Pour l'abstract, il faut savoir dans quel cas nous sommes pour écrire sur une seule ligne (Ceci est toujours à faire)
      - Dans la majorité des cas, l'abstract est entouré des mots "ABSTRACT" et "INTRODUCTION", dans un des articles fournis, le mot abstract est absent, alors une partie pour ce cas particulier a été ajoutée

---

5. **Elvin Fichot-Corgeron** : Le titre du papier.
   - **Appréciation générale** :  
   - **Note** :  

---

## **Retour sur le travail effectué (Rétrospective Sprint)**

### **Ce qui nous avons déterminé**
- Nous choisisons le langage python de façon unanime par pur préférence et expérience des utilisateurs.

### **Ce qui a bien fonctionné**


### **Ce qui a posé problème**


### **Ce qu’on doit améliorer**


---

### **Conclusion** :

