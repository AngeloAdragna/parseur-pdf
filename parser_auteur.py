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
    lignes = [line.strip() for line in auteurs.split('\n') if line.strip()]
    profils = []
    email_regex = r'[\w\.-]+@[\w\.-]+\.\w+'

    #{a,b}@domaine
    for idx, line in enumerate(lignes):
        match = re.search(r'\{(.+?)\}@([\w\.-]+\.\w+)', line)
        if match:
            ids = [ident.strip() for ident in match.group(1).split(',')]
            domaine = match.group(2)
            emails = [f"{ident}@{domaine}" for ident in ids]

            noms = []
            for i in range(idx):
                if not re.search(email_regex, lignes[i]) and not lignes[i].isdigit():
                    noms.append(lignes[i])

            noms_final = []
            for nom_line in noms:
                noms_final.extend(re.split(r'\s*[,;]?\s*(?:and|&)\s*|,', nom_line))

            affil_lines = []
            for i in range(idx + 1, len(lignes)):
                if not re.search(email_regex, lignes[i]):
                    affil_lines.append(lignes[i])
                else:
                    break

            full_affil = "\n".join(affil_lines)
            for k, nom in enumerate(noms_final):
                if k < len(emails):
                    profils.append(f"{nom.strip()}\n{full_affil.strip()}\n{emails[k]}")
            return profils

    # indiv
    email_positions = [(i, re.findall(email_regex, lignes[i])) for i in range(len(lignes)) if re.search(email_regex, lignes[i])]
    
    for i, emails in email_positions:
        bloc = []
        for j in range(i - 1, -1, -1):
            if re.search(email_regex, lignes[j]):
                break
            bloc.insert(0, lignes[j])
        
        nom = bloc[0] if bloc else f"Auteur{i+1}"
        affil = "\n".join(bloc[1:]) if len(bloc) > 1 else ""

        for email in emails:
            profils.append(f"{nom.strip()}\n{affil.strip()}\n{email.strip()}")

    if profils:
        return profils

    # Numéros
    if any(re.match(r'^\d$', line) for line in lignes):
        affiliations = {}
        current_id = None
        auteurs_data = []

        for line in lignes:
            if re.match(r'^\d$', line):
                current_id = line
                affiliations[current_id] = []
            elif current_id and not re.search(email_regex, line):
                affiliations[current_id].append(line)
            elif re.search(email_regex, line):
                for email in re.findall(email_regex, line):
                    auteurs_data.append({'affil': current_id, 'email': email})

        for i, auteur in enumerate(auteurs_data):
            nom = f"Auteur{i+1}"
            affil = "\n".join(affiliations.get(auteur['affil'], []))
            profils.append(f"{nom}\n{affil}\n{auteur['email']}")

        return profils

    #Nom seuls
    noms = []
    for line in lignes:
        if not re.search(email_regex, line):
            noms.append(line)

    if noms:
        if len(noms) == 1:
            return [n.strip() for n in re.split(r'\s*[,;]?\s*(?:and|&)\s*|,', noms[0])]
        return noms

    return profils if profils else ["\n".join(lignes)]

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
    return '\n'.join(get_list(content, titre, abstract))


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

