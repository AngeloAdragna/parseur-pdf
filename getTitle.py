import re

def est_ligne_auteur(ligne, is_first_line=False):
    """
    Récupère le titre d'un fichier
    
    Args:
        fichier_txt (str): Chemin vers le fichier texte
        
    Returns:
        str: Titre du fichier
    """
    ligne = ligne.strip()
    if not ligne:
        return False

    if is_first_line:
        return False

    # Détection des and et et 
    if re.search(r'\b(and|et)\b', ligne, re.IGNORECASE):
        mots = ligne.split()
        if all(re.match(r'^[A-Z][a-z\-]+$', mot) or mot.lower() in ('and', 'et') for mot in mots):
            return True

    # Détection de noms 
    noms = re.findall(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)?', ligne)
    if len(noms) >= 2:
        return True

    if '@' in ligne or 'university' in ligne.lower():
        return True

    return False

def extraire_titre_intelligent(fichier_txt, max_lignes=15):
    """
    Extrait le titre du fichier texte.
    """
    try:
        with open(fichier_txt, 'r', encoding='utf-8') as f:
            lignes = [l.strip() for l in f.readlines()[:max_lignes]]
        
        bloc_titre = []
        for idx, ligne in enumerate(lignes):
            if not ligne:
                continue

            is_first_line = (idx == 0)

            # Arrête l'analyse si une ligne ressemble à un auteur ou "abstract"
            if est_ligne_auteur(ligne, is_first_line=is_first_line) or ligne.lower().startswith("abstract"):
                break

            bloc_titre.append(ligne)

        titre = " ".join(bloc_titre).strip()
        return titre if titre else None

    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {fichier_txt}: {e}")
        return None

# === Exemple d'utilisation ===
if __name__ == "__main__":
    fichier_exemple = "Torres.txt" 
    titre = extraire_titre_intelligent(fichier_exemple)

    if titre:
        print(f"Titre extrait: {titre}")
    else:
        print("Titre non trouvé")