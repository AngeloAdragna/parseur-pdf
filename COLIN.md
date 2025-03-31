# pdf2txt

## Test de l'option `-t type`
### test option xml
Le xml pourrait permettre de garder la structure des phrases
```diff
+ Conserve la structure des blocs de texte avec la balise `textbox`
+ Conserve les espaces, même en fin de ligne avec "<text> </text>"
- Présence de "<text>\n</text>" à toutes les fins de lignes
- Perte de la structure des tableaux
```

### test html
Franchement ça vaut le coup d'oeil :looool:
(Oui oui le tableau est par dessus un texte)
![](https://cloud.col1n.fr/s/3mAkeAxgLw9XQi4/preview)
```diff
- J'ai pas besoin d'expliquer
- Structure chelou
- Les tableaux sont HORRIBLES
```


# Python
## PyPDF2
