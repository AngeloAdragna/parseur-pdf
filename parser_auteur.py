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

