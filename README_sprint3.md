# Sprint 3

**Auteurs : L3 CMI Informatique**

- Angelo Adragna
- Corentin Saccoman
- Elliot Pozucek
- Colin Palazzetti Rubera
- Elvin Fichot-Corgeron

**lien vers Github**
[README Sprint 3](https://github.com/conception-logicielle-CERI/parseur-pdf/blob/sprint-3/README_sprint3.md)

<!--pandoc README_sprint1.md -o README_sprint1.pdf --pdf-engine=xelatex-->

## **Rôles**
- Angelo est `SCRUM Master` et `Product Owner`, il doit rédiger le rapport avec les différents artefacts.
- Corentin, Elliot, Colin et Elvin sont développeurs.
- Corentin doit s’occuper de l’intégration du fonctionnement XML, depuis l’option de lancement jusqu’à l’écriture des balises.
- Elliot doit récupérer la section bibliographique et renvoyer un texte brut.
- Colin doit harmoniser les différents fichiers.
- Elvin doit récupérer la section de l’auteur et renvoyer un texte brut.

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
    Format txt sans option  : python parser.py CORPUS_TRAIN/ CORPUS_TXT/
    Format txt avec option  : python parser.py -t CORPUS_TRAIN/ CORPUS_TXT/
    Format xml              : python parser.py -x CORPUS_TRAIN/ CORPUS_XML/

    Résultats attendus:  
    Le répértoire CORPUS_TXT/ contiendra les fichiers texte avec uniquement le nom du fichier, le titre et l'abstract  
    Le répértoire CORPUS_XML/ contiendra les fichiers texte avec toutes les infos demandées pour le xml  

## **Revu Sprint 2**
- Debrief sur le produit du second sprint positif. Le travail a été complexe mais correctement effectué par chaque membre de la `SCRUM Team`.
- Liste de questions à donner au Scrum Master pour qu'il échange avec le client sur les besoins.
- Répartition des tâches selon les affinités de chacun. Bonne communication et cohésion d'équipe.
- Questionnement, refactor et harmonisation des fichiers pour une meilleure lisibilité et compréhension.
- Les artefacts ne semblent plus poser de problèmes, bien qu'un léger doute plane encore. Cependant, la méthode SCRUM est volontairement peu détaillée, donc cela semble naturel.
- Les différents rendus des devs étaient trop proches du rendu du produit du sprint 2.
- Très bonne cohésion d'équipe. Elliot a réalisé un acte d'entraide remarquable. En effet, Corentin a eu un imprévu, ce qui fait qu'il aurait été en retard sur la réalisation de son compte rendu. C'est donc Elliot qui s'est volontairement proposé pour réaliser le susdit compte rendu.



## **Réunion planification Sprint 05/05/25**
![notes sur papier](images/reunion.png)  
Retranscription :
- Échange avec le client pour connaître son besoin par rapport à l'extraction des auteurs. Le client souhaite-t-il avoir une balise auteur par auteur ? La réponse est oui.
- S'assurer que le parsage est réalisé sur tout le document PDF et pas uniquement la première page. Sinon, le système devra être modifié afin de récupérer le champ bibliographique, souvent à la fin du PDF.
- Améliorer les différentes fonctions, notamment le parsage d'abstract.
- Réalisation du backlog en priorité, puis des autres artefacts.
- Détermination de la docstring par Colin et Angelo.
- Discussion de l'équipe afin de confirmer le choix de continuer en Python.


## **Backlog**
- Option XML au lancement (texte brut par défaut) et traduction texte XML.
- Récupérer la section auteur.
- Récupérer la section bibliographique.
- Harmoniser les fichiers de code.
- Améliorer les fonctionnalités du code.
- Réaliser les artefacts compris dans le conteneur de ce sprint 3.

## **Burndown**
![Exemple sortie](images/burndown-2.png)  


## _Consignes pour le compte rendu des développeurs_ : 
- Déposez votre compte rendu au plus tard le 09/05/2025 à 18h sur la branche 3.
- Fournir AU MOINS une image de l’avancement par fonctionnalité par développeur.
- Votre compte rendu doit comporter une analyse de votre développement, les aspects positifs, négatifs, limitations…
- Indiquer quel jour vous avez fini chaque fonctionnalité.

## **Travail de chaque codeur pendant la mêlée (Revue Sprint)**

---

1. **Angelo Adragna** : Documentation des événements/artefacts Scrum (réunions de planification de sprint, mêlée quotidienne, revue de sprint, rétrospective du sprint).
- Les backlogs doivent être réalisés en premier lieu, lors de la première réunion, afin de répartir les tâches entre chaque personne.
- La réunion a permis d'établir la liste de questions pour le client, afin d'obtenir davantage de détails et de spécifications.
- Le Burndown est facile à réaliser à la toute fin du sprint.
- La rédaction doit cependant se faire au fur et à mesure de l'avancement de chacun.
- La mise en commun du travail de chacun peut parfois s'avérer ardue, en raison du manque de détails dans le fonctionnement des productions personnelles des développeurs.
- J'ai pris en compte la deadline trop proche de la fin du sprint, afin d'éviter un rush final.
- Médiation et conseils aux développeurs.


---

2. **Corentin Saccoman** :  L'intégration du fonctionnement XML depuis l'option de lancement jusqu'à l'écriture des balises XML.
   
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
   
 ---

3. **Elliot Pozucek** : Récupération de la section bibliographique et renvoi dans un fichier texte brut.


### Analyse du code


### Pistes d'amélioration


### Analyse de performances

   
### **Remarque** 


---

4. **Colin Palazzetti Rubera** : Harmonisation des différents fichiers de code, avec notamment la docstring NumPyDoc.

### Analyse du code


### Pistes d'amélioration


### Analyse de performances

   
### **Remarque** 


---

5. **Elvin Fichot-Corgeron** : Récupération de la section de l’auteur et renvoi dans un fichier texte brut.


### Analyse du code


### Pistes d'amélioration


### Analyse de performances

   
### **Remarque** 


---
A faire à la fin
## **Retour sur le travail effectué (Rétrospective Sprint 3)**

  
### **Ce que nous avons déterminé**

### **Ce qui a bien fonctionné**

### **Ce qui a posé problème**
PATCH
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

