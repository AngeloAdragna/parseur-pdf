# TP Conception logicielle - Scrum

**Auteurs : L3 CMI Informatique**

- Angelo Adragna
- Corentin Saccoman
- Elliot Pozucek
- Colin Palazzetti Rubera
- Elvin FICHOT--CORGERON

<!--jupyter nbconvert --to pdf integrale.ipynb-->

## **Roles**

- Angelo est le maitre de `SCRUM`.
- Corentin et Elliot travailleront sur la méthode `pdftotext`.
- Colin et Elvin travailleront sur la méthode `pdf2txt`.

## **Présentation**

### Étapes à suivre

1. **Préparation des fichiers**

   - Utiliser vos 10 fichiers PDF dans un dossier dédié pour l'entrainement.

2. **Conversion en texte brut**

   - Testez deux outils : `pdftotext` et `pdf2txt`.
   - Utilisez les options de lancement pour optimiser la conversion.

3. **Analyse qualitative**

   - Comparez les résultats pour chaque fichier selon ces critères :
     - Respect des frontières des phrases ?
     - Découpage correct des mots ?
     - Structure des lignes cohérente ?
   - Documentez vos observations dans un tableau simple :
     ```
     | Fichier       | Outil     | Fr. phrases | Mots découpés | Lignes désordonnées |
     | ------------- | --------- | ----------- | ------------- | ------------------- |
     | document1.pdf | pdftotext | ✅          | ❌            | ✅                 |
     | document1.pdf | pdf2txt   | ✅          | ✅            | ❌                 |
     ```

4. **Recommandations**
   - Classez et évaluez les outils selon leurs performances globales.
   - Retenez celui qui donne les résultats les plus fiables et précis.

### Résultats attendus

- Rapport détaillé des performances des outils.
- Texte brut structuré pour chaque fichier PDF.
- Recommandations pour la conversion efficace des fichiers PDF.

## **Sprint 2**
Vous pouvez consulter le [carnet produit du sprint 2](./sprint2_carnet_du_produit.pdf) pour plus de détails.
L'objectif est de développer un programme dans le langage de notre choix afin de produire un fichier texte qui contient :

- Le nom du fichier d’origine (dans une ligne, espaces convertis à _)
- Le titre du papier (dans une ligne)
- Le résumé (abstract) de l’auteur (dans une ligne)

Le système doit prendre comme entrée un dossier contenant les fichiers PDF et créer un sous-dossier pour déposer les sorties en plain texte avec le même noms que les PDF. Si le sous-dossier existe, il faudra l’effacer.

## **Consignes pour l'équipe**

