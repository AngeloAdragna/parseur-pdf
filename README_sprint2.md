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
- Corentin et Elliot travailleront sur la méthode `pdftotext`, ensemble dans un seul fichier en Python.
- Colin et Elvin travailleront sur la méthode `pdf2txt`, chacun de leur côté : Colin dans un fichier `.py` et Elvin dans un autre.

## **Objectif**
Dans la séance précédente vous avez choisit le convertisseur le plus adapté PDF→texte. Il s’agit
maintenant d’analyser les articles plain texte par le parseur. Il sera développé dans un langage adéquat,
et analysera les sorties textuelles du convertisseur.
Nous voulons comme sortie un fichier .txt par fichier ayant les sections et la structure suivante.

## **Réunion**
- Debrief sur le produit du premier sprint assez positif malgré une legère dissipation du à des zones d'ombres sur la consigne.
- Répartission des tâches.
- Liste de questions à donner au Scrum master pour qu'il échange avec le client sur les besoins

## **Backlog**
- Le système doit traiter un dossier contenant des fichiers PDF, créer un sous-dossier pour stocker les sorties en texte brut avec les mêmes noms que les fichiers PDF, et supprimer le sous-dossier s'il existe déjà.
- Réaliser un plain text en sortie.
- Le nom du fichier d'origine dans une ligne avec les espaces convertis en "_" en sortie.
- Le titre du papier dans une ligne en sortie.
- Le résumé (abstract) de l’auteur (dans une ligne) en sortie.

Le langage doit être choisi en fonctions des critères :
   1/ Maîtrisé par les membres de l’équipe
   2/ Performance en temps d’exécution


## **Travail de chaque codeur pendant la mêlée (Revue Sprint)**

_Consignes_ : 
- Déposez vos comptes rendu au plus tard le 18/04/2025 à 20h sur la branche 2
- Fournir au moins une image de l'avancement par fonctionnalité.
- Votre compte rendu doit comporter un analyse de votre développe, les aspects positifs, négatifs, limitations...
- Vous devez comparer le temps d'exécution de votre fonctionnalité en python et en C++

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
   - **Note** :  

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

