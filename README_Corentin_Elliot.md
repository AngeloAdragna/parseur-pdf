# Revue du sprint 2 de Corentin SACCOMAN & Elliot POZUCEK

Réalisation du "squelette" du script python.  
Utilisation des librairies suivantes :
- **subprocess** pour le lancement des commandes bash
- **sys** pour le traitement des paramètres du programme
- **shutil** pour la gestion des répertoires
- **pathlib** pour la gestion des fichiers
- **re** pour l'analyse lexicale avec les expressions régulières

Le programme prend en paramètres le répertoire d'entrée (les fichiers pdf) et un répertoire de sortie (différent du précédent).  
A partir de ces répertoires, les fichiers .pdf sont transformés en .txt dans le répertoire d'accueil avec la commande `pdftotext -raw`.  
Le répertoire de sortie est écrasé s'il existe déjà.

Puis, le script applique les méthodes **get_file_name**, **get_title** et **get_abstract** sur chaque fichier .txt.
Le fichier .txt récupéré avec **pdftotxt -raw** est écrasé avec les infos récupérées par les méthodes susmentionnées (le titre, le nom du fichier et l'abstract).

Exemple de lancement du script :
```bash
python3 script.py CORPUS_TRAIN/ CORPUS_TXT/
```

Le répertoire de sortie (dans cet exemple `CORPUS_TXT/`) contiendra les fichiers .txt avec le nom du fichier, le titre et l'abstract.

## Historique du sprint 2

### 09/04/2025

Le script est capable de récupérer le nom du fichier. Le script converti les fichiers `.pdf` en `.txt` et les met dans le répertoire de sortie.

### 11/04/2025

Attente du travail du reste de l'équipe afin de réaliser l'intégration de leurs différentes parties.
Le script gère les erreurs de type "fichier introuvable" et "répertoire introuvable".

## 18/04/2025

### Intégration du travail de l'équipe

Le script intègre maintenant les fichiers pyhton en charge de récupérer le titre et l'abstract des articles.
Les fonctionnalités principales sont donc terminées.  

Un exemple de fichier .txt en sortie :
![Exemple sortie](images/exemple_sortie.png)  

**Remarque** : Chaque section est écrite sur une seule ligne à la fois, comme demandé dans le sujet (sur la capture d'écran, les retours à la ligne sont causés par l'affichage dans la console).

### Ajout d'une mesure de temps d'éxécution

Ajout d'une mesure du temps d'éxécution du script (`log_execution_time`). Le temps d'éxécution est stocké dans un fichier log (qui est ignoré par git pour éviter les conflits).

### Version C++

Ajout d'une version du programme en C++ afin de comparer les performances (voir [`parser.cpp`](./parser.cpp)). Les deux versions sont équivalentes en terme de fonctionnalité, sauf pour l'extraction de l'abstract qui est bancale sous C++.

En terme de temps d'éxécution, les deux versions semblent être similaire au dixième de seconde près (sur une machine identique).

Compiler le programme :
```bash
make parser.exe
```
Lancer le programme :
```bash
./parser.exe CORPUS_TRAIN/ CORPUS_TXT/
```
Supprimer l'exécutable :
```bash
make clean
```


## Analyse du code

 - Le script n'arrive pas à récupérer correctement le titre du fichier `mikheev.pdf` : il ne récupère que la lettre 'c'
 - Pour les autres, le script python à l'air de fonctionner correctement.
 - Le script C++ ne récupère pas le début de l'abstract.

## Pistes d'amélioration

- Au lieu d'écrire l'avancement du script directement dans la console, écrire dans un fichier log.
- Récupérer le nom de l'auteur
- Mieux commenter le code (surtout pour `abstract.py`) <span style="color:blue"> [FAIT]</span>
- Ajouter une fonctionnalité qui permet de mesurer le temps d'éxecution et de le stocker dans les logs <span style="color:blue"> [FAIT]</span>
- Faire un programme équivalent en C++ afin de comparer les performances <span style="color:blue"> [FAIT]</span>

## Analyse de performances

Sur un unique lancement de programme, nous constatons que la version C++ est environ 1 seconde plus rapide que la version Python.    
![Comparatif Python/C++](images/comparatif_execution.png)  

En lançant plusieurs exécutions de chaque version, nous obtenons des fichiers de logs remplis, desquels nous pouvons tirer de l'information.  
![Comparatif Python/C++ sur 10 lancements](images/comparatif_logs.png)    
Et nous pouvons constater que le Python est majoritairement plus lent que le C++.  
Cependant, comme précisé plus haut, la version C++ est moins fiable que la version Python. Il faut donc privilégier la version Python, un peu plus lente, pour ne pas sacrifier l'efficacité.
