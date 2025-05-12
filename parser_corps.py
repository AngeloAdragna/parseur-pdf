import re

def get_string(content: str) -> str:
    """
    TODO: docu à faire
    Cette version considère le corps comme étant le texte de l'intro (incluse) à la dernière 
    section (soit Conclusion, Discussion, Future Work ou Evaluation).
    Il faudrait que l'intro soit ignorée et que l'on considère la partie juste après l'intro comme le début du corps.
    """
    # Nettoyage du texte
    cleaned = content.replace("-\n", "")            # fusion des mots coupés par un saut de ligne
    cleaned = re.sub(r"\n", " ", cleaned)           # suppression des sauts de ligne
    cleaned = re.sub(r"\s+", " ", cleaned).strip()  # suppression des espaces multiples

    # Détecter la position du header de l'introduction
    intro_match = re.search(r"\bIntroduction\b.*?", cleaned, re.IGNORECASE)

    # Nettoyage en lignes pour trouver la position de fin (dernière section considérée)
    lines = content.splitlines()

    # Patternes de fin
    # Pas de IgnoreCase car on veut matcher exactement les majuscules en début de mot
    end_patterns = [
        r"^\s*\d{1,2}\.?\s+(Conclusion|Discussion|Future Work|Evaluation|Conclusions|CONCLUSIONS|DISCUSSION|FUTURE WORK|EVALUATION)\b",
        r"^\s*[IVX]+\.\s+(CONCLUSIONS?|DISCUSSION|FUTURE WORK|EVALUATION)\b",
        r"^\s*(Conclusion|Discussion|Future Work|Evaluation)\s*$"
    ]

    # Trouver la position de fin
    end_pos = len(cleaned)
    for i, line in enumerate(lines):
        for pattern in end_patterns:
            if re.match(pattern, line.strip()):
                # Convertir la position ligne -> index brut
                snippet = line.strip()
                match = re.search(re.escape(snippet), cleaned)
                if match:
                    end_pos = match.start()
                    break
        if end_pos != len(cleaned):
            break

    start_pos = intro_match.start()
    body = cleaned[start_pos:end_pos].strip()

    # Tous les ~100 caractères, on ajoute un saut de ligne et des tabulations (aucun mot n'est coupé en deux)
    formatted = ""
    i = 0
    while i < len(body):
        if i + 100 >= len(body):
            formatted += body[i:].strip()
            break
        next_space = body.find(" ", i + 100)
        if next_space == -1:
            formatted += body[i:].strip()
            break
        formatted += body[i:next_space].strip() + "\n\t\t"
        i = next_space + 1

    return formatted.strip()
