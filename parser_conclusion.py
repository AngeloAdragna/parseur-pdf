"""Docstring for the paser_conclusion.py module.

Cette partie du parser se charge de l'extraction de la conclusion.

Elle permet de récupérer la conclusion à partir des sections 'Conclusion' et/ou 'Future Work'.

"""


def get_string(content: str) -> str:
    """
    Extrait automatiquement la conclusion à partir des section 'Conclusion' et/ou 'Future Work'.

    Parameters
    ----------
    content : str
        Texte brut du document.

    Returns
    -------
    str
        Références extraites, nettoyées et séparées par ligne.
    """
    mots_stop = ["Acknowledgements","References"]
    return ""