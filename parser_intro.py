import re

def extract_introduction(content: str) -> str:
    """
    Extrait la section 'Introduction' seule, jusqu'au début de la section suivante.
    Le texte est reformatté avec des retours à la ligne tous les ~100 caractères.
    """
    # Découpage du texte ligne par ligne pour faciliter le traitement
    lines = content.splitlines()

    intro_pattern = r"^\s*[IVX0-9]{0,3}\.?\s*(Introduction)\b"
    next_section_pattern = r"^\s*(?:2|II)\.?\s+[A-Z][^\n]{0,100}$"
    specific_phrase = "A noisy-channel model for sentence compression"  # Spécifique au fichier marcu_statistics_sentence_pass_one.pdf qui ne contient pas de numérotation

    start_idx = end_idx = None

    # Recherche du début de l'introduction
    for i, line in enumerate(lines):
        if re.match(intro_pattern, line.strip()):
            start_idx = i + 1 # + 1 pour ignorer le titre "Introduction" de la section
            break

    if start_idx is None:
        return None

    # Fusionner les lignes pour recherche textuelle
    full_text = " ".join(lines[start_idx:])

    # Recherche spécifique de la phrase (pour le fichier marcu_statistics... qui ne contient pas de numérotation)
    specific_match = re.search(re.escape(specific_phrase), full_text)
    if specific_match:
        # Convertir l'index brut en index de ligne approx.
        char_index = specific_match.start()
        cumulative = 0
        for j in range(start_idx, len(lines)):
            cumulative += len(lines[j]) + 1  # +1 pour le \n supprimé par join
            if cumulative >= char_index:
                end_idx = j + 1 # + 1 pour prendre le contenu de la ligne qui nous intéresse avant de supprimer le reste
                                # car une fois passé en texte, le titre de la section suivante est contenu au milieu d'une ligne.
                break

    # Sinon, recherche ligne par ligne classique
    if end_idx is None:
        for j in range(start_idx + 1, len(lines)):
            stripped_line = lines[j].strip()
            if re.match(next_section_pattern, stripped_line) and not re.search(r"Introduction", stripped_line, re.IGNORECASE) :
                end_idx = j
                break

    if end_idx is None:
        end_idx = len(lines)

    intro_text = " ".join(lines[start_idx:end_idx])
    intro_text = re.sub(r"(\s+|-?\n)", " ", intro_text).strip()

    # Reformatage ~100 caractères sans couper les mots
    formatted = ""
    i = 0
    while i < len(intro_text):
        if i + 100 >= len(intro_text):
            formatted += intro_text[i:].strip()
            break
        next_space = intro_text.find(" ", i + 100)
        if next_space == -1:
            formatted += intro_text[i:].strip()
            break
        formatted += intro_text[i:next_space].strip() + "\n\t\t"
        i = next_space + 1

    return formatted.strip()
