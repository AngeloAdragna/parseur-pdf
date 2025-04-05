# pdf2txt

## Test de l'option `-t type`
### test option xml
`pdf2txt -t xml Word2Vec.pdf > output.html`
Le xml pourrait permettre de garder la structure des phrases
```diff
+ Conserve la structure des blocs de texte avec la balise `textbox`
+ Conserve les espaces, même en fin de ligne avec "<text> </text>"
- Présence de "<text>\n</text>" à toutes les fins de lignes
- Perte de la structure des tableaux
```

### test html
`pdf2txt -t html Word2Vec.pdf > output.html`
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
```py
html_file = open('CORPUS_TRAIN/Word2Vec.html', 'w')

from PyPDF2 import PdfReader


parts = []

def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 50 and y < 720:
        parts.append(text)



reader = PdfReader('CORPUS_TRAIN/Word2Vec.pdf')
page = reader.pages[0]
extracted_text = page.extract_text(0, visitor_text=visitor_body)

html_file.write(extracted_text)
html_file.close()
```

https://pypdf2.readthedocs.io/en/3.x/user/extract-text.html
Théoriquement d'après la doc, c'est censé être pas mal

```diff
- Honnêtement, ça marchait mieux avec les commandes bash, par conntre le parsage du text ça peut être pas mal
```

