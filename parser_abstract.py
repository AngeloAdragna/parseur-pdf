"""Docstring for the parser_abstract.py module.

Cette partie du parser se concentre sur l'extraction et le traitement de l'abstradct.

Elle permet d'extraire l'abstract dd'un fichier, et au besoin, de faire en sorte de le mettre sur une seule ligne

"""
import re
import parser_utils

def get_list(text: str):
    """
    Retourne l'abstract dans le texte brut de l'article, en une liste de lignes
    ⚠️ Ne doit pas être utilisé en même temps que get_string 

    Parameters
    ----------
    text: string
        Article ou partie de l'article en texte brut

    Returns
    -------
    list(string)
        Liste de lignes contenant l'abstract
    """
    abstract = text.split("\n")
    begin_found = end_found = False
    i=0
    while i<len(abstract):
        # regex : Commence par "abstract", potentiellement précédé d'espace.s
        if not(begin_found) and re.match(r"^ *Abstract", abstract[i], re.IGNORECASE):
            abstract[i] = re.sub(r"^ *Abstract\W*", "", abstract[i], flags=re.IGNORECASE)
            abstract = abstract[i:]
            begin_found = True
            i=0
        # Considering that it's unlikely for a line to start with the word abstract
        
        # regex : Commence par "Introduction", potentiellement précédé d'espace.s
        # ou d'une numérotation
        if not(end_found) and re.match(r"^([1I]\.?)? ?Introduction", abstract[i], re.IGNORECASE):
            abstract = abstract[:i]
            end_found = True
            break # No need to continue the script
        
        i+=1 
        
    if not begin_found:
        # On essaie de trouver un début de façon heuristique
        abstract = abstract[3:] if len(abstract)>3 else abstract # On retire les 3 premières lignes - généralement le titre de l'article, pour éviter des faux positifs
        for i, line in enumerate(abstract):
            # regex : Commence par un mot significatif d'un abstract, potentiellement précédé d'espace.s
            if re.match(r"^.*(paper|article|presents?|examines?)", line, re.IGNORECASE):
                abstract = abstract[i:]
                break
        
        
    return abstract
    pass

import json
def get_string(text: str):
    """
    Retourne l'abstract dans le texte brut de l'article, en une seule ligne, en enlevant les retours à la ligne
    ⚠️ Ne doit pas être utilisé en même temps que get_list 

    Parameters
    ----------
    text: string
        Article ou partie de l'article en texte brut

    Returns
    -------
    list(string)
        Texte en une ligne contenant l'abstract
    """
    txt_lower = text.lower()
    abstract = ""
    abstract_lst = get_list(text)
    for i, line in enumerate(abstract_lst):
        # Traitement spécial si la ligne précédente fini par "-"
        if abstract[-1] == '-' if len(abstract) > 0 else False:
            p_index = len(abstract) # Index du "-"
            
            # Extraction du mot qui a le tiret (regex équivalent : "\w+-")
            p_word = abstract[:p_index].split()[-1] if p_index >= 0 else ""
            # Extraction du premier mot de la ligne suivante
            n_word = line.strip().split()[0] if line.strip() else ""
            
            if parser_utils.check_nl(p_word, n_word):
                abstract = abstract[:-1] # On ajoute la ligne, mais en retirant le "-"
                
            # Le mot n'existe pas, ou il n'y a rien à traiter, alors ajout de la ligne sans " "
            abstract += line.strip()
            continue # Ignorer le traitement normal
        
        # Traitement normal
        abstract += " "
        abstract += line.strip()
        
    return abstract.strip()
        
        
        


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
            Abstract extrait du fichier passé en argument       
        
        Raises
        ------
        FileNotFoundError
            Quand l'ouverture du fichier n'a pas réussi
        """
        with open(filepath, 'r', encoding="utf-8") as file:
            print(f"Ouverture du fichier {filepath}")
            parser_utils.set_content(file.read())
            return get_list(file.read())
        raise FileNotFoundError(filepath)
    
    input_folder = "CORPUS_TXT"
    output_folder = "CORPUS_ABSTRACTS"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open("abstracts.md", 'w', encoding="utf-8") as mdf:
        for filename in os.listdir(input_folder):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            
            if os.path.isfile(input_path):
                abstract = test_gettxt(input_path)
                with open(output_path, 'w', encoding="utf-8") as output_file:
                    output_file.write("\n".join(abstract))
                    
                a2 = " ".join(abstract).strip()
                mdf.write(f"\n## {filename}\n```\n{a2}\n```\n")

