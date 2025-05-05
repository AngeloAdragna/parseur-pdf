"""Docstring for the parser_title.py module.

Extraction du titre d'un article à partir de son texte brut.

Permet de récupérer le titre d'un article à partir des premières lignes de son texte brut. 
Au besoin, des potentielles information avant le titre (auteurs, date, ville) sont supprimées. 
Le titre est ensuite validé pour s'assurer qu'il respecte certaines conditions de longueur et de contenu.

"""

import re

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

def get_string(text: str, max_lignes: int = 15) -> str:
    """
    Récupère le titre d'un article à partir d'un texte brut.

    Parameters
    ----------
    text: string
        Article ou partie de l'article en texte brut
    max_lignes: int, optional
        Nombre maximum de lignes à analyser (15 par défaut)

    Returns
    -------
    string
        Titre de l'article sur une ligne

    Raises
    ------
    ValueError
        Le titre n'a pas été trouvé ou est invalide
    """
    # Supression lignes techniques
    lignes = text.split("\n")[:max_lignes]
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
            
    raise ValueError("Titre non trouvé ou invalide")





# Fonction de test locale
if __name__ == "__main__":
    input_folder = "CORPUS_TXT"
    output_folder = "CORPUS_TITLES"
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
            Titre extrait du fichier passé en argument       
        
        Raises
        ------
        FileNotFoundError
            Quand l'ouverture du fichier n'a pas réussi
        """
        with open(filepath, 'r', encoding="utf-8") as file:
            print(f"Ouverture du fichier {filepath}")
            return get_string(file.read())
        raise FileNotFoundError(filepath)
    

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open("titles.md", 'w', encoding="utf-8") as mdf:
        for filename in os.listdir(input_folder):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            
            if os.path.isfile(input_path):
                try:
                    title = test_gettxt(input_path)
                except ValueError as e:
                    print(f"Erreur lors de l'extraction du titre de {filename} : {e}")
                    title = "⚠️ Titre non trouvé ou invalide"
                with open(output_path, 'w', encoding="utf-8") as output_file:
                    output_file.write(title)
                    
                a2 = " ".join(title).strip()
                mdf.write(f"\n## {filename}\n```\n{a2}\n```\n")

