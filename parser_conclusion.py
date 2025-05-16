"""Docstring for the paser_conclusion.py module.

Cette partie du parser se charge de l'extraction de la conclusion.

Elle permet de récupérer la conclusion à partir des sections 'Conclusion' et/ou 'Future Work'.
"""

import re
import parser_utils

def get_string(content: str) -> str:
    """
    Extrait la section de conclusion du texte brut et retourne une chaîne formatée.

    Parameters
    ----------
    content : str
        Texte brut du document.

    Returns
    -------
    str
        Texte de conclusion nettoyé et formaté (~100 caractères par ligne).
    """
    mots_stop = ["Acknowledgements", "Acknowledgments", "References", "Acknowledgment"]

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
    result_lines = []
    current_section_lines = []
    inside_section = False

    for line in lines:
        stripped = line.strip()

        if section_pattern.match(stripped):
            if current_section_lines:
                result_lines.extend(current_section_lines)
                current_section_lines = []

            inside_section = True
            continue

        elif stripped in mots_stop:
            if current_section_lines:
                result_lines.extend(current_section_lines)
                current_section_lines = []
            inside_section = False
            continue

        elif re.match(r"^\s*(\d{1,2}|[IVXLCDM]+)?[.\)]?\s*[A-Z][A-Za-z\s]{1,50}$", stripped) and len(stripped.split()) <= 6:
            if current_section_lines:
                result_lines.extend(current_section_lines)
                current_section_lines = []
            inside_section = False
            continue

        if inside_section:
            current_section_lines.append(line)

    if current_section_lines:
        result_lines.extend(current_section_lines)

    return parser_utils.clean_and_format(result_lines)

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
