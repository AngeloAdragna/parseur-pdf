"""Docstring for the paser_biblio.py module.

Cette partie du parser se charge de l'extraction des références bibliographiques à partir du texte brut d'un document.

Elle permet de récupérer les références bibliographiques à partir de la dernière section 'References' ou 'Bibliography'.

"""

import re

def get_string(content: str) -> str:
    """
    Extrait automatiquement les références bibliographiques à partir de la dernière section
    'References' ou 'Bibliography'.

    Parameters
    ----------
    content : str
        Texte brut du document.

    Returns
    -------
    str
        Références extraites, nettoyées et séparées par ligne.
    """
    return "\n".join(get_list(content))


def get_list(content: str) -> str:
    """
    Extrait automatiquement les références bibliographiques à partir de la dernière section
    'References' ou 'Bibliography'.

    Parameters
    ----------
    content : str
        Texte brut du document.

    Returns
    -------
    list
        Références extraites, nettoyées et séparées par ligne.
    """
    # on trouve la dernière section "References" ou "Bibliography"
    section_match = None
    for match in re.finditer(r"^\s*(\d+\.\s*)?(References|Bibliography)\s*$", content, flags=re.IGNORECASE | re.MULTILINE):
        section_match = match

    if not section_match:
        return["Aucune section de références détectée."]

    # on extrait le contenu qui nous intéresse
    refs_raw = content[section_match.end():].strip()

    # on nettoie le texte brut
    refs_raw = re.sub(r"-\n", "", refs_raw)      # jointure des mots cassés
    refs_raw = re.sub(r"\n", " ", refs_raw)      # suppression des sauts de ligne
    refs_raw = re.sub(r"\s+", " ", refs_raw).strip()

    # il faut détecter le format utilisé
    has_bracket = re.search(r"\[\d+\]", refs_raw)               # format '[n]'
    has_dot = re.search(r"(?:^|\n)\s*\d{1,3}\.\s", content)     # format numéroté 'n.'

    # on extrait les références selon le format détecté
    if has_bracket:
        return extract_references_bracket(refs_raw)
    elif has_dot:
        return extract_references_dot(refs_raw)
    else:
        return extract_initial_based_references(refs_raw)

def extract_references_bracket(text: str) -> list:
    """
    Extrait les références de type [n].

    Parameters
    ----------
    text : str
        Texte brut de la section références.

    Returns
    -------
    list[str]
        Liste des références extraites.
    """
    references = []
    pattern = re.compile(r"\[\d+\]\s*(.*?)(?=\[\d+\]|$)", re.DOTALL)
    matches = pattern.findall(text)
    for body in matches:
        references.append(body.strip())
    return references

def extract_references_dot(text: str) -> list[str]:
    """
    Extrait les références de type n.

    Parameters
    ----------
    text : str
        Texte nettoyé après la section "References".

    Returns
    -------
    list[str]
        Liste des références extraites sans le numéro.
    """
    references = []
    pattern = re.compile(r"\b(\d{1,3})\.\s+(.*?)(?=\b\d{1,3}\.\s+|$)", re.DOTALL)
    matches = pattern.findall(text)
    for _, body in matches:
        references.append(body.strip())
    return references

def extract_initial_based_references(text: str) -> list[str]:
    """
    Extrait les références non numérotées à partir de motifs d'initiales de prénom (ex: 'E. Brill').

    Parameters
    ----------
    text : str
        Texte brut de la section références.

    Returns
    -------
    list[str]
        Liste des références extraites.
    """
    # Liste pour stocker les débuts de référence
    starts = [m.start() for m in re.finditer(r"\b[A-Z]\.\s+[A-Z][a-z]", text)]
    starts.append(len(text))  # Ajouter fin du texte comme borne

    references = []
    for i in range(len(starts) - 1):
        ref = text[starts[i]:starts[i+1]].strip()
        if len(ref) > 20:
            references.append(ref)

    return references

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
            Bibliographie extraite du fichier passé en argument       
        
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
    output_folder = "CORPUS_BIBLIOS"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open("biblios.md", 'w', encoding="utf-8") as mdf:
        for filename in os.listdir(input_folder):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            
            if os.path.isfile(input_path):
                abstract = test_gettxt(input_path)
                with open(output_path, 'w', encoding="utf-8") as output_file:
                    output_file.write("\n".join(abstract))
                    
                a2 = " ".join(abstract).strip()
                mdf.write(f"\n## {filename}\n```\n{a2}\n```\n")

