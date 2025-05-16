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

def clean_and_format(lines: list[str]) -> str:
    """
    Nettoie une liste de lignes de texte et la formate à ~100 caractères par ligne avec indentations.

    Parameters
    ----------
    lines : list[str]
        Lignes extraites d'une section d'un document.

    Returns
    -------
    str
        Texte propre et reformatté.
    """
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        line = re.sub(r"-\s*$", "", line)            # Suppression des coupures de mots
        line = re.sub(r"[\x00-\x1F]+", "", line)     # Suppression des caractères de contrôle
        cleaned_lines.append(line)

    raw_text = " ".join(cleaned_lines)
    raw_text = re.sub(r"\s+", " ", raw_text).strip()

    # Reformater tous les ~100 caractères
    formatted = ""
    i = 0
    while i < len(raw_text):
        if i + 100 >= len(raw_text):
            formatted += raw_text[i:].strip()
            break
        next_space = raw_text.find(" ", i + 100)
        if next_space == -1:
            formatted += raw_text[i:].strip()
            break
        formatted += raw_text[i:next_space].strip() + "\n\t\t"
        i = next_space + 1

    return formatted.strip()

