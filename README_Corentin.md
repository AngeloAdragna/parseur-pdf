# Revue du sprint 2 de Corentin SACCOMAN

Réalisation du "squelette" du script python.  
Utilisation des librairies suivantes :
- **subprocess** pour le lancement des commandes bash
- **sys** pour le traitement des paramètres du programme
- **shutil** pour la gestion des répertoires
- **pathlib** pour la gestion des fichiers
- **re** pour l'analyse lexicale avec les expressions régulières

Le programme prend en paramètres le répertoire d'entrée (les fichiers pdf) et un répertoire de sortie (différent du précédent).  
A partir de ces répertoires, les fichiers .pdf sont transformés en .txt dans le répertoire d'accueil avec la commande ***pdftotext -raw***.  
Le répertoire de sortie est écrasé s'il existe déjà.  


Fonctionnalité terminée le 09/04/2025.  

Actuellement le 11/04/2025, je suis en attente du travail du reste de l'équipe afin de réaliser l'intégration de leurs différentes parties.