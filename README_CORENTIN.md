2. **Corentin Saccoman** :  L'intégration du fonctionnement xml depuis l'option de lancement jusqu'à l'écriture des balises.

   
### Analyse du code
L'intégration du mode XML repose sur la fonction parse_arguments, écrite pour gérer les arguments passés en ligne de commande. Deux options sont proposées :

- **-t** (par défaut) pour une sortie en plain text
- **-x** pour une sortie au format XML

Ces deux options sont exclusives l'une de l'autre (on ne peut pas les cumuler).

Cette fonction se charge également de récupérer les chemins du répertoire d'entrée et du répertoire de sortie.

Les arguments ainsi extraits sont ensuite utilisés dans les différentes fonctions de traitement (dont les noms ont été modifiés pour s'adapter à la nouvelle demande):

```python
def pdfs_to_format(repertoire_entree: Path, repertoire_sortie: str, args)

def convert_pdf_file(fichier_pdf: Path, repertoire_sortie: Path, args)

def add_infos_to_file(fichier: Path, args)
```

### Exemples d'utilisation:
    Format txt sans option  : python parser.py CORPUS_TRAIN/ CORPUS_TXT/
    Format txt avec option  : python parser.py -t CORPUS_TRAIN/ CORPUS_TXT/
    Format xml              : python parser.py -x CORPUS_TRAIN/ CORPUS_XML/

    Résultats attendus:  
    Le répértoire CORPUS_TXT/ contiendra les fichiers texte avec uniquement le nom du fichier, le titre et l'abstract  
    Le répértoire CORPUS_XML/ contiendra les fichiers texte avec toutes les infos demandées pour le xml  

### Comparaison des formats
**FORMAT TXT**  
![Format TXT](images/txt_example.png)  
**FORMAT XML**  
![Format XML](images/xml_example.png)  

Chaque fonction adapte son comportement en fonction du mode choisi, que ce soit pour le traitement du contenu ou la génération de fichiers avec la bonne extension (.txt ou .xml) et la bonne structure de données.
### Pistes d'amélioration
- Ajout d'un mode de test pour pouvoir visualiser la sortie de pdftotext avant nos modifications (Réalisé par Elliot)

- Tests unitaires pour parse_arguments afin d'assurer une robustesse en cas d'ajout d'options futures.

### Analyse de performances

Le mode XML n’introduit pas de surcharge notable dans le traitement des fichiers.  
La principale différence réside dans la structure de sortie, légèrement plus coûteuse en termes de taille mais négligeable sur des volumes faibles à moyens.  
L'appel conditionnel aux traitements en fonction du mode sélectionné évite des branches inutiles dans le pipeline de traitement.

### **Remarque** 
La demande du client est bien respectée avec l'ajout de différentes balises (caractéristiques) qui n'étaient pas présentes dans le format txt.  
Justement, ces parties n'ont pas été ajoutée au format txt, pour la simple et bonne raison que le client ne nous l'a pas demandé. De plus, dans le format txt, il est demandé que chaque partie soit sur une seule ligne à chaque fois, impossible avec les auteurs et les références bibliographiques.

### Dates clés :
- 05/05/2025 : Fin de ma partie et intégration du travail de Colin et d'Elliot. En attente du travail d'Elvin qu'il pourra intégrer lui même (En attente d'ajout d'images).
- 09/05/2025 : Ajout de captures d'écran au readme suite à l'intégration de la partie d'Elvin