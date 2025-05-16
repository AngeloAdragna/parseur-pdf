# Sprint 5

**Auteurs : L3 CMI Informatique**

- Angelo Adragna
- Corentin Saccoman
- Elliot Pozucek
- Colin Palazzetti Rubera
- Elvin Fichot-Corgeron

**lien vers Github**
[README Sprint 5](https://github.com/conception-logicielle-CERI/parseur-pdf/edit/sprint-5/README_sprint5.md)

<!--pandoc README_sprint1.md -o README_sprint1.pdf --pdf-engine=xelatex-->

## **Rôles**

- Angelo est `SCRUM Master` et `Product Owner`, il doit rédiger le rapport avec les différents artefacts.
- Corentin, Elliot, Colin et Elvin sont développeurs.
- Les développeurs travaillent par binômes.
- Une partie de l’équipe (Corentin et Elliot) doit passer votre système sur les 10 articles pour détecter les limites fixes,ils devront verifier si le nombre de frontières veritables découpé par l'humain est identique à celui découpé automatiquement.
- Un second binôme devra s'occuper d'établir le corpus de référence les frontières (souples) des sections en analysant miniscieusement à la main chaque phrases et comptabiliser à la main le nombre de points.

## **Objectif**
Le Département de contrôle de qualité du LIA demande une évaluation de la qualité du système.
Cette évaluation peut être réalisée en fonction de la précision obtenue sur un corpus de référence
(découpage de sections fait par des humains). Ainsi, les fragments de texte extraits présents dans les
références seront comptabilisés positivement; leur absence sera pénalisée (voir l’exemple en Annexe).
La précision sera calculée comme suit :
 Précision = Sections_correctes_trouvées_par_le_système / Sections_trouvées_par_le_système
Une section sera considérée correcte si :
a) Toutes ses phrases ont été bien détectées : frontières strictes.
b) Quelques phrases peuvent chevaucher les sections (± 2 phrases) : frontières souples.
Il faut ajouter une dernière phase d’évaluation du système qui reporte le résultat de la précision.
La précision sera mesurée sur un corpus de test de 10 nouveaux articles PDF. Une partie de l’équipe
doit passer votre système sur les 10 articles, une autre doit établir le corpus de référence les frontières
(souples) des sections. Enfin, vous devez calculer (à la main si vous voulez être agiles) la précision de
votre système comme la moyenne sur l’ensemble des articles parsés.
Les détailles sont dans le [sprint5](sprint5_carnet_du_produit.pdf). 

## **Execution du programme**
```sh
# Affichage de l'aide pour les options : 
python parser.py -h

# Pas d'option de sélection des fichiers à parser :
python parser.py CORPUS_TRAIN/ CORPUS_TXT/          # Format txt sans option
python parser.py -t CORPUS_TRAIN/ CORPUS_TXT/       # Format txt avec option
python parser.py -x CORPUS_TRAIN/ CORPUS_XML/       # Format xml 

# Sélection manuelle des fichiers à parser :
python parser.py -m CORPUS_TRAIN/ CORPUS_TXT/       # Format txt sans option
python parser.py -t -m CORPUS_TRAIN/ CORPUS_TXT/    # Format txt avec option
python parser.py -x -m CORPUS_TRAIN/ CORPUS_XML/    # Format xml
```
**Résultats attendus :**   
Le répértoire CORPUS_TXT/ contiendra les fichiers texte avec uniquement le nom du fichier, le titre et l'abstract.
Le répértoire CORPUS_XML/ contiendra les fichiers xml avec toutes les infos demandées pour le xml.


## **Revu Sprint 5**
- Debrief sur le produit du quatrième sprint mitigé. Le travail a été effecuté sans être testé, ceci à causé de gros problème à l'aube du sprint 5.
- Répartition des tâches par binômes selon les affinités de chacun. Communication très difficile.
- Les différents rendus des devs étaient satisfaisants.
- Un problème commun aux développeurs semble être le manque de robustesses du aux différements formats possibles au seins des PDF.
  
## **Réunion planification Sprint 16/05/25**
La communication était mauvaise, le `SCRUM MASTER` à peiné à tenir notes de cette réunion car chacun est parti de son côté et que le contenu à réalisé est maigre et rapide à repartir.
![notes sur papier](images/reunion5.jpg)  

## **Sprint Backlog**
   - Test précision avec des frontières strictes.
   - Test précision avec des frontières souples.
   - Calcul de la précision : Précision = Sections_correctes_trouvées_par_le_système / Sections_trouvées_par_le_système
- Améliorer les fonctionnalités du code.
- Réaliser les artefacts compris dans le conteneur de ce sprint 5.

## **Burndown**
![Exemple sortie](images/burndown5.jpg)

## _Consignes pour le compte rendu des développeurs_ :
- Premier retour de la part des développeurs le dimanche 18/05/2025 sur le travail effecté.
- Déposez votre compte rendu au plus tard le ? à ? sur la branche 5.
- Fournir AU MOINS une image de l’avancement par fonctionnalité par développeur.
- Votre compte rendu doit comporter une analyse de votre développement, les aspects positifs, négatifs, limitations… Vous pourrez vous baser sur le squelette pour vous guider si nécéssaire.
- Indiquer quel jour vous avez fini chaque fonctionnalité !
- Penser à bien décrire la précision de chaque document pour les frontières souples.

## **Travail de chaque menebre de la `SCRUM Team` pendant la mêlée (Revue Sprint)**

---

## 1. **Angelo Adragna** : Documentation des événements/artefacts Scrum (réunions de planification de sprint, mêlée quotidienne, revue de sprint, rétrospective du sprint).

- Les backlogs doivent être réalisés en premier lieu, lors de la première réunion, afin de répartir les tâches entre chaque personne.
- La réunion a permis d'établir la liste de questions pour le client, afin d'obtenir davantage de détails et de spécifications.
- Le Burndown se termine à la fin du sprint 5.
- La rédaction se fait au fil du sprint.
- Création d'un squelette de rendu pour facilier la mise en commun du travail de chacun. Je propose donc un modèle en raison du manque de détails dans les productions personnelles des développeurs.
- Médiation et conseils aux développeurs.

---

## 2. **Corentin Saccoman** : Récupération de la section `introduction` et réalisation du menu de sélection de fichiers.

### **Développement**

### **Remarque**

### **Réussi**

### **Piste d'amélioration**

### **Dates clés** :

  ---

## 3. **Elliot Pozucek** : Récupération de la section `corps` de chaque fichier.

### **Développement**

### **Remarque**

### **Réussi**

### **Piste d'amélioration**

### **Dates clés** :

  ---

## 4. **Colin Palazzetti Rubera** : Récupération de la section `discussion` (`evaluation`) et s'occupe de la redondance de certains codes.

### **Développement**

### **Remarque**

### **Réussi**

### **Piste d'amélioration**

### **Dates clés** :
 
  ---

## 5. **Elvin Fichot-Corgeron** :

### **Développement**

### **Remarque**

### **Réussi**

### **Piste d'amélioration**

### **Dates clés** :

  ---

## **Retour sur le travail effectué (Rétrospective Sprint 5)**
### **Ce qui a bien fonctionné**
- Bonne répartition des tâches entre les membres, chacun a pu avancer sur sa partie sans trop d’interférences.
- L’intégration progressive des travaux (Colin, Elliot, Corentin) a permis une mise en commun fluide.
- Les réunions Scrum ont été efficaces pour identifier les points bloquants et ajuster les priorités.
- La génération des fichiers XML et TXT selon les besoins du client a été bien maîtrisée.
- L’ajout du menu de sélection manuelle de fichiers améliore l’ergonomie de l’outil.
- La détection de la section `Introduction` est globalement robuste, même si quelques cas spéciaux demeurent.
- Le découpage précis du `Corps` de texte avec préservation des retours à la ligne facilite les traitements futurs.
- Une réelle progression dans la qualité des contributions individuelles et de la documentation.
- Réelle entraide entre Corentin et Elliot afin de pouvoir supprimer l'introduction à l'aide du REGEX de Corentin de la section `Corps` d'Elliot.

### **Ce qui a posé problème**
- Le fichier *marcu_statistics_sentence_pass_one.pdf* reste problématique car il ne suit aucun des formats habituels pour les titres de section.
- L'absence de numérotation dans certains fichiers empêche une récupération fiable des sections comme `Introduction`.
- La reconnaissance automatique des débuts et fins de section `Corps` reste complexe en raison de l’hétérogénéité du corpus.
- Certains cas extrêmes dans les séparations ligne/colonne ou les notes de bas de page parasitent encore le parsing.
- Quelques divergences entre les formats XML générés par différents membres ont nécessité une harmonisation finale.
- Une dépendance persistante à l’outil `pdftotext` (Linux uniquement) complique la portabilité.

### **Ce qu’on doit améliorer**
- Uniformiser davantage la structure des balises XML générées par chaque module pour éviter des incohérences.
- Proposer une détection plus sémantique pour les débuts de section en se basant sur le contenu et non uniquement les titres.
- Prévoir une phase de nettoyage de texte en amont pour corriger automatiquement les caractères spéciaux ou artefacts liés au format PDF.
- Ajouter des tests unitaires pour les nouvelles fonctions (`extract_introduction`, découpage du `corps`, menu de sélection).
- Rendre l’application plus portable en envisageant une alternative multiplateforme à `pdftotext`.
- Améliorer la couverture documentaire avec des exemples concrets dans le README final.

---

## **Conclusion** :

### Selon Angelo Adragna
- Suivi rigoureux de la méthode Scrum, avec une planification plus détaillée et des revues efficaces.
- Coordination fluide malgré les difficultés techniques rencontrées sur certains fichiers.
- Le squelette commun a facilité l’unification du rendu final.
- Bonne anticipation des points de friction en amont des deadlines.
- Une dynamique de groupe constructive et un gain notable en autonomie dans la rédaction des comptes rendus.

### Selon Corentin Saccoman
- L’ajout du menu interactif permet une vraie valeur ajoutée à l’expérience utilisateur.
- L'extraction de la section `Introduction` a nécessité des compromis mais fonctionne bien dans la majorité des cas.
- Bonne maîtrise des expressions régulières et adaptation au corpus, avec des réflexions sur les limites à long terme.
- Volonté de rendre le code robuste malgré les exceptions.
- Quelques frustrations sur l'impossibilité de généraliser certains patterns, mais vision claire des pistes futures.

### Selon Elliot Pozucek
- Le traitement de la section `Corps` a gagné en clarté, grâce au découpage ligne à ligne et au respect de la structure d’origine.
- Le maintien des retours à la ligne est un choix pertinent pour une utilisation ultérieure du contenu.
- Quelques difficultés à gérer les transitions entre les sections (`abstract`, `introduction`, `corps`), mais des solutions concrètes ont été apportées.
- Le temps de traitement reste raisonnable malgré les nouveaux traitements.
- Suggestion d’intégrer un système de logs plus fin pour suivre l’évolution de chaque fichier.

### Selon Colin Palazzetti Rubera
- Travail de normalisation des formats XML et harmonisation des conventions entre les modules.
- Poursuite des efforts sur la documentation (docstrings, structure).
- Identification d’un besoin de meilleure robustesse dans les extractions d’informations critiques (ex. : titre, auteurs).
- Propositions concrètes pour renforcer la résilience du système en cas de fichier malformé ou ambigu.

### Global
Les modules développés sont plus stables, les intégrations se font sans blocage majeur, et les livrables sont conformes aux attentes.  
L’autonomie de chaque membre est notable et les prises d’initiative (menu, gestion des sections, normalisation) vont au-delà des attentes initiales.  
L’outil commence à être réellement exploitable pour le client, avec un usage plus flexible et une structure de sortie bien définie.  
Il reste des améliorations possibles pour la robustesse et la portabilité, mais le cœur du système est désormais en place.  
L'objectif reste le produit, c'est pourquoi, même si l'équipe souhaitait aller plus loin en termes de fonctionnalités, elle a su se contraindre à ce qui était imposé.
