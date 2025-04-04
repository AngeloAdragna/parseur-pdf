# Corentin SACCOMAN - Elliot POZUCEK - Analyse de pdftotext

Les `|` entre deux valeurs d'options (exemple : -H 2 | 5 ) signifient que toutes les valeurs ont été testé. 

## Options qui ne fonctionnent pas (fichier texte vide)
Ces options produisent un fichier texte vide.

### pdftotext -H 20 | 1080

### pdftotext -x 0 | 1 | 640 | 1200000 | 12000

### pdftotext -y 0 | 1 | 640 | 1200000 | 12000

## Options qui n'affectent pas le fichier texte (par rapport à la commande sans option).

### pdftotext -colspacing 0.1 | 0.3 | 0.7

### pdftotext -eol unix | mac

### pdftotext -nopgbrk

### pdftotext -r 320 | 460 | 640 | 3 | 72

## Options qui affectent significativement le fichier texte.

### pdftotext -raw
Converti le pdf en texte sans retranscrire la structure du pdf. L'ordre de lecture est donc conservé.

```diff
+ Cette option fonctionne bien avec les structures en colonnes : le texte est mis à la ligne de manière séquencielle, le texte reste donc cohérent (l'orde de lecture est respecté)
+ Les tableaux restent cohérent dans leur structure
- Les espaces sont réduits, rendant le tableau impossible à détecter pour un système (et peu lisible pour un humain)
- Les figures ne sont pas lisibles, le texte est reporté de manière linéaire (incompréhensible)
- Les mots coupés en deux dans le pdf (retour à la ligne) sont aussi coupés en deux dans le fichier texte
- Le changement de pages sont visibles dans le fichier texte et coupent le texte
```
### pdftotext -fixed 5

+ pdftotext -fixed 5 : rend bien les tableaux et les paragraphes, mais ne fonctionne pas avec les colonnes.

## pdftotext -layout :
```diff    
+ Permet de garder la mise en forme => Utile uniquement pour les tableaux chez nous
- Garder la mise en forme signifie  aussi et surtout qu'on garde la mise en forme colonne par colonne qu'on veut exclure...
```

## Appréciation générale de pdftotext
pdftotext est très simple d'utilisation mais son utilisation sur des articles scientifiques ayant un format assez particulier, avec des graphiques, des tableaux et des colonnes nécessite un énorme travail en post-traitement (script python ou bash) pour :
- Récupérer le bon format de texte
- Bien structurer le document (Parties Auteur, titre...).

Voir ce que sortent Colin et Elvin sur pdf2txt pour comparer.

Une combinaison des deux n'est pas à exclure.
