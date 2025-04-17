def extraire_titre(fichier_txt):
    """
    Récupère le titre d'un fichier
    
    Args:
        fichier_txt (str): Chemin vers le fichier texte
        
    Returns:
        str: Titre du fichier
    """
    try:
        with open(fichier_txt, 'r', encoding='utf-8') as f:
            for ligne in f:
                ligne = ligne.strip()
                if ligne: 
                    return ligne
        return None
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {fichier_txt}: {e}")
        return None

#Exemple
if __name__ == "__main__":
    fichier_exemple = "hybrid_approach.txt"
    titre = extraire_titre(fichier_exemple)
    
    if titre:
        print(f"Titre extrait: {titre}")
    else:
        print("Le fichier est vide ou aucune ligne non vide trouvée")
s