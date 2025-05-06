"""Docstring for the parser_auteur.py module.

Cette partie du parser se charge de l'extraction des auteurs à partir du texte brut d'un document.

Elle requiert le titre de l'article pour identifier la section des auteurs, qui se trouve entre le titre et l'abstract.

"""


def get_list(text, titre, abstract="Abstract"):
    """
    Extrait la section auteurs entre le titre et l'abstract.

    Parameters
    ----------
    content : str
        Texte brut du document.
    titre : str
        Titre de l'article.
    abstract : str, optionnel
        Mot clé pour identifier le début de l'abstract (par défaut "Abstract").
    Returns
    -------
    list
        Section auteurs extraite, nettoyée et séparée par ligne.
    """

    # Normalisation pour recherche insensible à la casse
    content_lower = text.lower()
    titre_lower = titre.lower()
    abstract_lower = abstract.lower()

    # Recherche du titre (peut être sur plusieurs lignes)
    titre_pos = content_lower.find(titre_lower)
    if titre_pos == -1:
        # Essai avec titre partiel (20 premiers caractères)
        titre_pos = content_lower.find(titre_lower[:20])
        if titre_pos == -1:
            return f"Erreur: Titre '{titre[:20]}...' non trouvé"

    # Position de départ après le titre
    start_pos = titre_pos + len(titre)

    # Recherche de l'abstract avec plusieurs stratégies
    abstract_pos = -1
    # 1. Essaye avec le mot abstract complet
    abstract_pos = content_lower.find(abstract_lower, start_pos)
    
    # 2. Si non trouvé, essaye avec début du mot abstract
    if abstract_pos == -1:
        abstract_pos = content_lower.find(abstract_lower[:5], start_pos)
    
    # 3. Si toujours non trouvé, cherche la première ligne vide double
    if abstract_pos == -1:
        abstract_pos = text.find("\n\n", start_pos)
    
    # 4. Si tout échoue, prend jusqu'à la fin du fichier
    if abstract_pos == -1:
        abstract_pos = len(text)

    # Extraction de la section
    auteurs_section = text[start_pos:abstract_pos].strip()

    # Nettoyage en conservant tous les emails
    cleaned_lines = []
    for line in auteurs_section.split('\n'):
        line = line.strip()
        if not line:
            continue
        
        # Suppression spécifique du mot abstract (toutes variantes)
        line = ' '.join(word for word in line.split() 
                        if word.lower() != abstract_lower)
        
        if line:  # Conserve toutes les lignes non vides
            cleaned_lines.append(line)

    return cleaned_lines if cleaned_lines else ["Aucun auteur trouvé"]

def get_string(content, titre, abstract="Abstract"):
    """
    Extrait la section auteurs entre le titre et l'abstract.

    Parameters
    ----------
    content : str
        Texte brut du document.
    titre : str
        Titre de l'article.
    abstract : str, optionnel
        Mot clé pour identifier le début de l'abstract (par défaut "Abstract").
    Returns
    -------
    string
        Section auteurs extraite, nettoyée et séparée par ligne.
    """
    return '\n'.join(get_list(content, titre, abstract))


# Fonction de test locale
if __name__ == "__main__":
    import os
    
    def test_gettxt(filepath: str):
        """
        Fonction de test :
            Ouvrir le fichier

        Parameters
        ----------
        filepath: string
            chemin vers le fichier
        
        Returns
        -------
        array
            Auteurs extraits du fichier passé en argument       
        
        Raises
        ------
        FileNotFoundError
            Quand l'ouverture du fichier n'a pas réussi
        """
        with open(filepath, 'r', encoding="utf-8") as file:
            print(f"Ouverture du fichier {filepath}")
            return get_list(file.read())
        raise FileNotFoundError(filepath)
    
    input_folder = "CORPUS_TXT"
    output_folder = "CORPUS_AUTHORS"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open("authors.md", 'w', encoding="utf-8") as mdf:
        for filename in os.listdir(input_folder):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            
            if os.path.isfile(input_path):
                abstract = test_gettxt(input_path)
                with open(output_path, 'w', encoding="utf-8") as output_file:
                    output_file.write("\n".join(abstract))
                    
                a2 = " ".join(abstract).strip()
                mdf.write(f"\n## {filename}\n```\n{a2}\n```\n")

