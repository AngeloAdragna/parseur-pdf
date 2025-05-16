import re

def get_string(content: str) -> str:
    """
    Extrait le texte du corps d'un document à partir de son contenu brut.
    Dans un premier temps, on cherche la section d'introduction. Une fois trouvée,
    on cherche la section suivante. Une fois la section suivante trouvée, on
    cherche le header de la dernière section à considérer (Conclusion, Discussion, etc.).
    On renvoie le texte entre la section après l'introduction et la section de fin.
    Le corps est nettoyé des espaces multiples et des caractères illisibles, puis il est 
    formaté pour être plus lisible (environ 100 caractères par ligne + 2 tabulations).
    
    Parameters
    ----------
    content : str
        Le contenu brut du document.
    
    Returns
    -------
    str
        Le texte du corps du document, nettoyé et formaté.
    """
    # Nettoyage en lignes pour trouver la position de fin (dernière section considérée)
    lines = content.splitlines()
    
    # Paterne du header de l'introduction
    intro_patterns = [
        r"^\s*\d{0,2}\.?\s*(Introduction|INTRODUCTION)\b",
        r"^\s*[IVX]{0,3}\.?\s*(Introduction|INTRODUCTION)\b"
    ]

    # Motif générique pour la section suivante (numérotée)
    next_section_pattern = r"^\s*(?:2|II)\.?\s+[A-Z][^\n]{0,100}$"

    # Cas particulier (marcu_statistics_sentence_pass_one.pdf)
    specific_phrase = "A noisy-channel model for sentence compression"

    start_idx = end_idx = intro_idx = None

    # Trouver l'index de l'introduction
    for i, line in enumerate(lines):
        if any(re.match(pat, line.strip()) for pat in intro_patterns):
            intro_idx = i
            break

    if intro_idx is None:
        return "Section non trouvée"
    
    # # Fusionner les lignes pour recherche textuelle
    full_text = " ".join(lines[intro_idx:])

    # Recherche spécifique de la phrase (pour le fichier marcu_statistics... qui ne contient pas de numérotation)
    specific_match = re.search(re.escape(specific_phrase), full_text)
    if specific_match:
        # Convertir l'index brut en index de ligne approx.
        char_index = specific_match.start()
        cumulative = 0
        for j in range(intro_idx, len(lines)):
            cumulative += len(lines[j]) + 1     # +1 pour le \n supprimé par join
            if cumulative >= char_index:
                start_idx = j + 1               # + 1 pour prendre le contenu de la ligne qui nous intéresse avant de supprimer le reste
                                                # car une fois passé en texte, le titre de la section suivante est contenu au milieu d'une ligne.
                break

    # Dans le cas général, recherche ligne par ligne classique
    if start_idx is None:
        for j in range(intro_idx + 1, len(lines)):
            stripped_line = lines[j].strip()
            if re.match(next_section_pattern, stripped_line) and not re.search(r"Introduction", stripped_line, re.IGNORECASE) :
                start_idx = j
                break

    if start_idx is None:
        return "La section suivante n'a pas été trouvée"

    # Patternes de fin
    # Pas de IgnoreCase car on veut matcher exactement les majuscules en début de mot
    end_keywords = [
        "Conclusion", "Discussion", "Future Work", "Conclusions", "Evaluation",
        "Conclusions and Future Work", "Discussion and Future Work",
        "CONCLUSIONS", "DISCUSSION", "FUTURE WORK"]
    end_patterns = [
        rf"^\s*\d{{1,2}}\.?\s+({'|'.join(re.escape(keyword) for keyword in end_keywords)})\s*$",
        rf"^\s*[IVX]+\.\s+({'|'.join(re.escape(keyword.upper()) for keyword in end_keywords)})\s*$",
        rf"^\s*({'|'.join(re.escape(keyword) for keyword in end_keywords)})\s*$"
    ]

    # Trouver l'index de la fin (avec les patternes de fin)
    for i in range(len(lines) - 1, start_idx, -1):
        line = lines[i].strip()
        if any(re.match(pat, line) for pat in end_patterns):
            end_idx = i
            break

    # Si aucun paterne de fin n'est trouvé, on prend la fin du fichier
    if end_idx is None:
        end_idx = len(lines)

    # Concaténer les lignes de start_idx à end_idx (exclu)
    corps = " ".join(lines[start_idx:end_idx]).replace("\n", " ").replace("- ", "")
    corps = re.sub(r"\s+", " ", corps).strip()
    corps = re.sub(r"[\x00-\x1F]+", "", corps)    # suppression des caractères illisibles

    # Reformater tous les ~100 caractères
    formatted = ""
    i = 0
    while i < len(corps):
        if i + 100 >= len(corps):
            formatted += corps[i:].strip()
            break
        next_space = corps.find(" ", i + 100)
        if next_space == -1:
            formatted += corps[i:].strip()
            break
        formatted += corps[i:next_space].strip() + "\n\t\t"
        i = next_space + 1

    return formatted.strip()