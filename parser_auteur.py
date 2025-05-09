"""Docstring for the parser_auteur.py module.

Cette partie du parser se charge de l'extraction des auteurs à partir du texte brut d'un document.

Elle requiert le titre de l'article pour identifier la section des auteurs, qui se trouve entre le titre et l'abstract.

"""
import re


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

def mapAuteurs(auteurs):
    if not auteurs.strip():
        return []

    auteurs = auteurs.replace('\\', '').replace('\x01', '')
    auteurs = re.sub(r'\[|\]', '', auteurs) 
    lignes = [line.strip() for line in auteurs.split('\n') if line.strip()]
    profils = []
    email_regex = r'[\w\.-]+@[\w\.-]+\.\w+'

    # Cas nom avec *
    asterisk_nom = None
    asterisk_affil = []
    asterisk_email = None

    for i, line in enumerate(lignes):
        if re.search(r'[∗\*]$', line.strip()):
            asterisk_nom = re.sub(r'[∗\*]$', '', line.strip())
        
        # Trouver la ligne commençant par ∗ ou *
        if re.match(r'^[∗\*]\s', line.strip()) or line.strip().startswith('∗') or line.strip().startswith('*'):
            # On récupère les lignes suivantes jusqu’à trouver un email
            for j in range(i, len(lignes)):
                l = lignes[j].strip()
                if re.search(email_regex, l):
                    asterisk_email = re.search(email_regex, l).group()
                    reste = re.sub(email_regex, '', l).strip().replace('E-mail:', '')
                    if reste:
                        asterisk_affil.append(reste)
                    break
                else:
                    asterisk_affil.append(l.replace('∗', '').replace('*', '').strip())
            break

    if asterisk_nom and asterisk_email:
        profil = f"{asterisk_nom} {' '.join(asterisk_affil).strip()} {asterisk_email}"
        profils.append(profil)
        return profils

    # Cas {a,b}@domaine
    for idx, line in enumerate(lignes):
        match = re.search(r'\{(.+?)\}@([\w\.-]+\.\w+)', line)
        if match:
            ids = [ident.strip() for ident in re.split(r'[;,]', match.group(1))]
            domaine = match.group(2)
            emails = [f"{ident}@{domaine}" for ident in ids]

            noms_final = []
            for i in range(idx):
                if not re.search(email_regex, lignes[i]) and not lignes[i].isdigit():
                    noms_final.extend(re.split(r'\s*[,;]?\s*(?:and|&)\s*|,', lignes[i]))

            affil_lines = []
            for i in range(idx + 1, len(lignes)):
                if not re.search(email_regex, lignes[i]):
                    affil_lines.append(lignes[i])
                else:
                    break

            full_affil = " ".join(affil_lines).strip()
            for k, nom in enumerate(noms_final):
                if k < len(emails):
                    entry = f"{nom.strip()}"
                    if full_affil:
                        entry += f" {full_affil}"
                    entry += f" {emails[k]}"
                    profils.append(entry)
            return profils

    # Cas numérotées avec les noms
    num_affils = {}
    nom_ligne_idx = []
    for i, line in enumerate(lignes):
        if re.search(r'\d$', line):  # ex: David Zajic1
            nom_ligne_idx.append(i)
            match = re.findall(r'([^\d]+?)(\d)', line)
            if match:
                for nom, id_ in match:
                    id_ = id_.strip()
                    num_affils.setdefault(id_, []).append(nom.strip())

    affils = {}
    current_id = None
    for i, line in enumerate(lignes):
        if re.match(r'^\d$', line):
            current_id = line.strip()
            affils[current_id] = []
        elif current_id and not re.search(email_regex, line):
            affils[current_id].append(line.strip())

    # Emails individuels
    email_lines = [i for i, line in enumerate(lignes) if re.search(email_regex, line)]
    for i in email_lines:
        emails = re.findall(email_regex, lignes[i])
        bloc = []
        for j in range(i - 1, -1, -1):
            if re.search(email_regex, lignes[j]):
                break
            bloc.insert(0, lignes[j])
        affil = " ".join([line for line in bloc if not re.search(r'\d$', line)]).strip()
        noms_raw = [line for line in bloc if line and (re.search(r'\d$', line) or not re.search(email_regex, line))]
        noms_clean = []
        for l in noms_raw:
            noms_clean.extend(re.split(r'\s*[,;]?\s*(?:and|&)\s*|,', l))
        noms_clean = [n.strip() for n in noms_clean if n.strip()]

        for k, email in enumerate(emails):
            nom = noms_clean[k] if k < len(noms_clean) else f"Auteur{k+1}"
            profils.append(f"{nom} {affil} {email}")

    if profils:
        return profils

    # Cas noms seuls avec emails en dessous
    temp_bloc = []
    current_noms = []
    current_affil = []
    for i, line in enumerate(lignes):
        if re.search(email_regex, line):
            emails = re.findall(email_regex, line)
            for idx, email in enumerate(emails):
                nom = current_noms[idx] if idx < len(current_noms) else f"Auteur{idx+1}"
                affil = " ".join(current_affil).strip()
                profil = f"{nom}"
                if affil:
                    profil += f" {affil}"
                profil += f" {email}"
                profils.append(profil)
            current_noms = []
            current_affil = []
        elif not current_noms:
            current_noms.extend(re.split(r'\s*[,;]?\s*(?:and|&)\s*|,', line))
            current_noms = [n.strip() for n in current_noms if n.strip()]
        else:
            current_affil.append(line)

    if not profils and len(lignes) == 1 and ',' in lignes[0]:
        raw_line = lignes[0].replace(' and ', ',')
        noms = [nom.strip().strip(',') for nom in raw_line.split(',')]
        profils = [nom for nom in noms if nom]

    if profils:
        return profils

    return [" ".join(lignes)]

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
    auteursSection = get_list(titre,abstract)
    auteurs = mapAuteurs(auteursSection)
    return auteurs


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
            Auteurs extraits du fichier passé en argument       
        
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
    output_folder = "CORPUS_AUTHORS"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open("authors.md", 'w', encoding="utf-8") as mdf:
        for filename in os.listdir(input_folder):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            
            if os.path.isfile(input_path):
                abstract = test_gettxt(input_path)
                with open(output_path, 'w', encoding="utf-8") as output_file:
                    output_file.write("\n".join(abstract))
                    
                a2 = " ".join(abstract).strip()
                mdf.write(f"\n## {filename}\n```\n{a2}\n```\n")

