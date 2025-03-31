# TP Conception logicielle - Scrum

**Auteurs : L3 CMI Informatique**

- Angelo Adragna
- Corentin Saccoman
- Elliot Pozucek
- Colin Palazzetti Rubera
- Elvin FICHOT--CORGERON

<!--jupyter nbconvert --to pdf integrale.ipynb-->

## **Roles**

- Angelo est le maitre de `SCRUB`.
- Corentin et Elliot travailleront sur la méthode `pdftotext`.
- Colin et Elvin travailleront sur la méthode `pdf2txt`.

## **Présentation**

Vous pouvez consulter le [carnet produit du sprint 1](./sprint1_carnet_produit.pdf) pour plus de détails.

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

## **Consignes pour l'équipe**

- Deposer un fichier à votre nom pour chaque branch, de la nature de votre choix avec un listing des paramètres testés, détaillant l'intéret, avantages et inconveniants.

- Deposer un fichier comprenant votre code, à votre nom, pour chaque branch, de la nature de votre choix.

- Fournir à votre maître des screens de certains rendu visuels vous semblant pertinents.

- Le maître doit pour rediger un readme du projet.

- Le maître doit pour rediger un readme pour faire une revue de sprint et une rétrospective du sprint.
