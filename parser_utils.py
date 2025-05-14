"""Docstring for the parser_utils.py module.

Cette partie du parser se concentre sur l'extraction et le traitement de l'abstradct.

Elle permet d'extraire l'abstract dd'un fichier, et au besoin, de faire en sorte de le mettre sur une seule ligne

"""
import re

content = False
def set_content(c):
    """
    Setter pour le contenu du module
    """
    global content
    content = c.lower()

def check_word(word: str):
    """
    Vérifie si le mot est présent dans le texte brut de l'article
    Cette fonction est utilisée pour vérifier si un mot existe, en se servant du texte brut de l'article

    Parameters
    ----------
    word: string
        Mot à vérifier

    Returns
    -------
    bool
        True si le mot est présent dans le texte, False sinon
        True permet d'assumer que le mot existe
        
    Raises
    ------
    AssertionError
        Si le contenu n'a pas été défini à l'avance
    """
    global content
    if not content:
        raise AssertionError("Le contenu n'est pas défini. Veuillez d'abord définir le contenu.")
    word_lower = word.lower()
    return word_lower in content
        
        
def check_nl(before, after):
    """
    Vérifie si les parties du mot avant et après sont présentes dans le texte brut de l'article
    Cette fonction est utilisée pour vérifier si un mot existe, en se servant du texte brut de l'article
    
    Parameters
    ----------
    before: string
        Première partie du mot à vérifier
    after: string
        Deuxième partie du mot à vérifier
        
    Returns
    -------
    bool
        True si le mot est présent dans le texte, False sinon
        True permet d'assumer que le mot existe
    """
    word = re.sub(r"\W", "", before+after)
    return check_word(word)

def return_word(before, after):
    """
    Retourne le mot complet en vérifiant les deux parties
    Si le mot complet existe, il est retourné tel quel
    Sinon, il est retourné avec un tiret entre les deux parties
    
    Parameters
    ----------
    before: string
        Première partie du mot à vérifier
    after: string
        Deuxième partie du mot à vérifier
        
    Returns
    -------
    string
        Mot complet, séparé par un tiret si nécessaire
    """
    if check_nl(before, after):
        return before + after
    return f"{before}-{after}"
