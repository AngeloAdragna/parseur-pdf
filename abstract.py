import re
import os

def abstract_file(filepath: str):
    """
        Parse the content of the file
        @param filepath: path to the file
        @return: Abstract
    """
    with open(filepath, 'r') as file:
        return get(file.read())

def get(text: str):
    """
    Returns the abstract in the raw parsed 

    Args:
        text (str): input file

    Returns:
        list(str): list of the parsed abstract
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
        # TODO: find the start
        
        
    return abstract
    pass

def get_string(text: str):
    """
    As the get(str) function, but returns a one-line string instead of a list

    Args:
        text (str): input file

    Returns:
        str: returns a one-line string of the abstract
    """
    abstract = ""
    abstract_lst = get(text)
    for i, line in enumerate(abstract_lst):
        # Traitement spécial si la ligne précédente fini par "-"
        if abstract[-1] == '-' if len(abstract) > 0 else False:
            p_index = len(abstract)-1 # Index du "-"
            
            # Extraction du mot qui a le tiret (regex équivalent : "\w+-"), sans le "-"
            p_word = abstract[:p_index].split()[-1][:-1] if p_index >= 0 else ""
            # Extraction du premier mot de la ligne suivante
            n_word = line.strip().split()[0] if line.strip() else ""
            
            # Si les deux mots ont une valeur (sinon pas de traitement à faire - prévention des erreurs)
            if p_word and n_word:
                # Création du mot sans tiret par concaténation des deux mots
                word = p_word + n_word
                
                if False: # TODO: Remplacer par un vérificateur de mot (vérifier si le mot existe)
                    abstract = abstract[:-1] + line.strip() # On ajoute la ligne, mais en retirant le "-"
                    continue # Passer à la ligne suivante
                
            # Le mot n'existe pas, ou il n'y a rien à traiter, alors ajout de la ligne sans " "
            abstract += line.strip()
            continue # Ignorer le traitement normal
        
        # Traitement normal
        abstract += " "
        abstract += line.strip()
        
    return abstract.strip()
        
        
        
        


if __name__ == "__main__":
    input_folder = "CORPUS_TXT"
    output_folder = "CORPUS_ABSTRACTS"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open("abstracts.md", 'w') as mdf:
        for filename in os.listdir(input_folder):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            
            if os.path.isfile(input_path):
                abstract = abstract_file(input_path)
                with open(output_path, 'w') as output_file:
                    output_file.write("\n".join(abstract))
                    
                a2 = " ".join(abstract).strip()
                mdf.write(f"\n## {filename}\n```\n{a2}\n```\n")

