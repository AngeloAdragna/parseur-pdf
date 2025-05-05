from getTitle import extraire_titre
import abstract as abstract_extractor



def getAuteursSection(fichier_txt, titre, abstract="Abstract"):
    """
    Extrait la section auteurs entre le titre et l'abstract.
    """
    try:
        with open(fichier_txt, 'r', encoding='utf-8') as file:
            content = file.read()

        # Normalisation pour recherche insensible à la casse
        content_lower = content.lower()
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
            abstract_pos = content.find("\n\n", start_pos)
        
        # 4. Si tout échoue, prend jusqu'à la fin du fichier
        if abstract_pos == -1:
            abstract_pos = len(content)

        # Extraction de la section
        auteurs_section = content[start_pos:abstract_pos].strip()

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

        return '\n'.join(cleaned_lines) if cleaned_lines else "Aucun auteur trouvé"

    except FileNotFoundError:
        return f"Erreur: Fichier {fichier_txt} non trouvé"
    except Exception as e:
        return f"Erreur inattendue: {str(e)}"


#Exemple
fichier = "hybrid_approach.txt"  # Ton fichier .txt

titre = extraire_titre(fichier)
    
with open(fichier, "r", encoding="utf-8") as f:
    content = f.read()
abstract = abstract_extractor.get_string(content)
auteurs = getAuteursSection(fichier,titre)
print("=== Auteurs ===")
print(auteurs)