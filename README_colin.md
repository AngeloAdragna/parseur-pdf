

4. **Colin Palazzetti Rubera** : Harmonisation des différents fichiers de code avec notamment la docstring Numpydoc.

### Analyse du code
- La docstring est globalement déjà complète, mais dans différents formats selon le développeur
- Mes modifications étant transparentes, j'ai puu les faire sans problème
- La seule partie "visible" pour les développeurs a été l'harmonisation des noms de fichiers

### Pistes d'amélioration
- optimisations de regex possibles
- Le code est assez complexe, et je pense que de la factorisation serait possible
- Une réflexion autour du cache pour l'étape intermédiaire est à voir
- Ce code fonctionne uniquement sous linux (avec pdftotext installé)
    - Aucune gestion de l'absence du programme
    - `FileNotFoundError: [WinError 2] Le fichier spécifié est introuvable` sous Windows 11 (hors cadre, mais testé)

### Analyse de performances
Ayant relu l'ensemble du projet, j'ai pu détecter des pistes particulières d'amélioration :
- Multiple ouverture du fichier txt détectées - cette partie a été réduite au minimum
- Beaucoup de regex, avec des fois des combinaisons possibles - Non optimisé
   
Le fichier (non commit) local utilisé pour garder de la consistence dans les docstring
![Fichier de structure pour les docstrings](images\docstring.png)

## Amélioration Sprint 2
### Récupération de l'abstract
Sachant qu'on a maintenant le txt de tout l'article recherche de mot possible dans l'article, pour essayer de trouver les mots existants qui seraient égaux 

Ajout dans le code :
```diff
- if False:
+ if word.lower() in txt_lower:
```
J'ai du corriger un petit bug : en retirant le `-` pour préparer la recherche de mot dans le sprint 2, je retirait une lettre en plus `compre-{\n}ssion` ⇒ `comprssion`, ce sui rendait la recherche impossible.

Détection du bug à l'aide de la fonction `json.dumps` :
![alt text](images/dump_error.png)
![alt text](images/dump_ok.png)

Cette partie s'ajoute aussi au txt