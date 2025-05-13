"""Docstring for the paser_conclusion.py module.

Cette partie du parser se charge de l'extraction de la conclusion.

Elle permet de récupérer la conclusion à partir des sections 'Conclusion' et/ou 'Future Work'.

"""

import re

def get_string(content: str) -> list[str]:
    """
    Extrait toutes les sections pertinentes du texte et retourne un tableau de lignes.

    Parameters
    ----------
    content : str
        Texte brut du document.

    Returns
    -------
    list[str]
        Liste des lignes extraites des sections cibles.
    """
    # Sections à exclure (titre qui marquent la fin de section utile)
    mots_stop = ["Acknowledgements", "Acknowledgments", "References", "Acknowledgment"]

    # Sections qu'on veut extraire
    sections_cibles = [
        "Conclusion", "Conclusions",
        "Future Work",
        "Conclusion and Future Work",
        "Conclusions and Future Work",
        "Discussion and Future Work",
        "Follow-Up Work",
        "Follow Up Work"
    ]

    section_pattern = build_section_regex(sections_cibles)
    stop_pattern = build_section_regex(mots_stop)

    lines = content.splitlines()
    result_lines = []  # Liste qui contiendra toutes les lignes du résultat
    current_section_lines = []  # Lignes de la section en cours
    inside_section = False

    for line in lines:
        stripped = line.strip()

        if section_pattern.match(stripped):
            # Si on était déjà dans une section, on sauvegarde les lignes
            if current_section_lines:
                result_lines.extend(current_section_lines)
                current_section_lines = []

            inside_section = True
            continue

        elif stripped in mots_stop:  # Modification ici: on vérifie l'égalité exacte
            # Fin de section - on sauvegarde les lignes
            if current_section_lines:
                result_lines.extend(current_section_lines)
                current_section_lines = []
            inside_section = False
            continue

        elif re.match(r"^\s*(\d{1,2}|[IVXLCDM]+)?[.\)]?\s*[A-Z][A-Za-z\s]{1,50}$", stripped) and len(stripped.split()) <= 6:
            # Nouveau titre probablement
            if current_section_lines:
                result_lines.extend(current_section_lines)
                current_section_lines = []
            inside_section = False
            continue

        if inside_section:
            current_section_lines.append(line)

    # Ajouter les dernières lignes si nécessaire
    if current_section_lines:
        result_lines.extend(current_section_lines)

    # Filtrer les lignes vides si besoin
    result_lines = [clean_string(line) for line in result_lines if line.strip()]

    return result_lines

def build_section_regex(keywords : list[str] ) ->list[str]:
    """
    
    Motif regex pour identifier les sections cibles

     Parameters
    ----------
    keywords : list[str]
        Sections cibles

    Returns
    -------
    list[str]
        Pattern de la section recherché.
    """
    return re.compile(
         r"^\s*(\d{1,2}|[IVXLCDM]+)?[.\)]?\s*(" +
        "|".join(re.escape(k) for k in keywords) +
        r")\s*$",
        re.IGNORECASE
    )



def clean_string(section: str) -> str:
    """
    Permet de nettoyer le code extrait de la conclusion.

    Parameters
    ----------
    section : str
        Texte brut de la section.

    Returns
    -------
    str
        Texte nettoyé.
    """
    cleaned_lines = []

    for line in section.splitlines():
        stripped = line.strip()

        # Ignorer les lignes vides
        if not stripped:
            continue

        # Supprimer les numéros de pages isolés
        if re.fullmatch(r"\d{1,4}", stripped):
            continue

        # Supprimer les noms d’auteurs typiques
        if re.fullmatch(r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?\s*(?:&|et|,|and)\s*)+[A-Z][a-z]+", stripped):
            continue

        # Supprimer les lignes très courtes sans signification
        if len(stripped) <= 2:
            continue

        cleaned_lines.append(stripped)

    return "\n".join(cleaned_lines)
