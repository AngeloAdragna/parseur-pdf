# Sprint 3 Elvin FICHOT--CORGERON

## Récupération des auteurs

### Approche du travail :

Pour réaliser cette tâche il y avait plusieurs solutions possibles :

- Renvoyer la section entière d'auteur dans une seule chaîne
- Renvoyer un tableau de chaîne de charactère qui contient le nom de l'auteur, et les adresses associés si elles sont présentes

Après concertation la solution s'est avéré être la meilleur.

### Dévelepement

Le travail à été réalisé dans le fichier `parser_auteur`

J'ai divisé cette étape en 3 méthodes distinctes:

#### `get_list`

Dans cette méthode je m'occupe d'extraire la section qui contient les auteurs.

Cette section se trouve toujours entre la section du titre et l'abstract.

Je me suis donc servis des méthodes `parser_title.get_string` et `parser_abstract.get_string` pour les récupérer

Ensuite je recupère la section situé entre les 2.

### `mapAuteurs`

C'est dans cette méthode que je décortique la chaine passé en paramètres pour avoir l'association entre l'auteurs et ses adresses.

Le plus difficile du travail est qu'il y a bcp de cas potentielle à traiter

- Un \* à la fin du titre avec la référence qui se trouve pas dans la section d'auteur

- Les adresses mail noté de cette manière {a,b}@domaine

- Des numéros pour les auteurs

- Des noms seuls

- Une notation avec nom adresses université adresse mail

Cela a été très difficile d'avoir un résultat optimisé compte tenu des possibilités.

#### `get_string`

Cette méthode est un peu comme un main du fichier

Je fais l'extraction de la section auteurs dedans, je l'envoie dans le mapper puis je retourne le tableau avec les auteurs.

Pour le résultats en XML on obtient ceci :

![](images/AuteursXML.png)

Pour ce pdf :

![](images/AuteursPDF.png)

#### Difficultés rencontrés

Comme dit plus haut le plus durs à été d'avoir beaucoup de cas différent à traiter. Lorsque j'arrivais à résoudre un cas, il y avait fréquemment un autre où il y avait un problème j'ai donc une version qui n'a pas la meilleur optimisation mais qui renvoie les informations essentielles

Au moment de merge mon code je ne l'avais pas correctement adapté à la nouvelle norme de code qui avait été mise en place. Ce qui à causé des erreurs.

De plus pour certain fichier j'avais fait les tests sur seulement le début des fichiers comme au dernier sprint sauf que pour récupérer la bibliographie nous utilisons maintenant le fichier en entier j'ai donc limité la recherche à 50 lignes pour localiser la section des auteurs

#### Rétrospectives

Mes axes d'améliorations pourrait être d'avoir un code plus optimisé qui donnent des informations encore plus précise.

Ensuite pour ce qui est du travail d'équipe j'aurais pu mieux me coordonner pour ne pas avoir de problème avec la nouvelle norme mis en place
