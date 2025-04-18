import re

def extraire_titre(fichier_txt, max_lignes=15):
    """
    Récupère le titre d'un fichier
    
    Args:
        fichier_txt (str): Chemin vers le fichier texte
        
    Returns:
        str: Titre du fichier
    """
    try:
        with open(fichier_txt, 'r', encoding='utf-8') as f:
            lignes = [l.strip() for l in f.readlines()[:max_lignes]]

        # Supression lignes techniques
        lignes_propres = []
        for l in lignes:
            if not l or \
               l.startswith(('Abstract', 'Keywords', '©', 'c', '')) or \
               re.search(r'\d{4} Association|Proceedings|pages? \d+', l) or \
               est_ligne_date_ville(l):
                continue
            lignes_propres.append(l)

        # Étape 2: Trouver le bloc de titre
        titre = []
        mots_continuation = ['for', 'in', 'to', 'of', 'and', 'on', 'with']
        
        for i in range(len(lignes_propres)):
            ligne = lignes_propres[i]
            
            # Condition d'arrêt
            if len(titre) >= 1 and (est_ligne_auteur(ligne) or ligne[0].islower()):
                break
                
            # Détection titre
            if (len(ligne.split()) >= 2 and ligne[0].isupper() and
                not any(c in ligne for c in ['@', '©'])):
                
                titre.append(ligne)
                
                # Vérifier titre multiligne
                if i+1 < len(lignes_propres):
                    next_line = lignes_propres[i+1]
                    derniers_mots = ligne.lower().split()[-1]
                    premiers_mots = next_line.lower().split()[0] if next_line else ''
                    
                    if (derniers_mots in mots_continuation or 
                        premiers_mots in mots_continuation):
                        titre.append(next_line)
                break

        # Validation finale
        if titre:
            titre_final = ' '.join(titre).strip()
            if (15 <= len(titre_final) <= 200 and 
                sum(c.isalpha() for c in titre_final) > 10):
                return titre_final
                
        return None

    except Exception as e:
        print(f"Erreur: {str(e)}")
        return None

def est_ligne_auteur(ligne):
    """Détecte les auteurs du doc"""
    if not ligne.strip():
        return False
    return (re.search(r'@|\.edu|university|inc\.|laboratory', ligne.lower()) or
            re.fullmatch(r'^([A-Z][a-z]+ )+[A-Z][a-z]+$', ligne.strip()))

def est_ligne_date_ville(ligne):
    """Détecte les lignes de type 'Ville, Mois Année'"""
    mois = r'(January|February|March|April|May|June|July|August|September|October|November|December)'
    return bool(re.fullmatch(r'[A-Z][a-z]+, ' + mois + r' \d{4}', ligne))





# === Exemple d'utilisation ===
if __name__ == "__main__":
    fichier = "ACL2004-HEADLINE.txt"  # Ton fichier .txt
    titre = extraire_titre(fichier)
    print("Titre extrait:", titre if titre else "Titre non trouvé")