"""Docstring for the parser_discussion.py module.

Cette partie du parser se concentre sur l'extraction et le traitement de la partie discussion.

Elle permet d'extraire la partie discussion d'un article, et au besoin, de faire en sorte de le mettre sur une seule ligne

"""
# AJOUTER PARTIES EVALUATION
import re
import parser_utils

def get_list(text: str):
    """
    Retourne la partie discussion dans le texte brut de l'article, en une liste de lignes
    ⚠️ Ne doit pas être utilisé en même temps que get_string 

    Parameters
    ----------
    text: string
        Article ou partie de l'article en texte brut

    Returns
    -------
    list(string)
        Liste de lignes contenant la partie discussion
    """
    discussions = text.split("\n")
    begin_found = False
    i=0
    # print(f"len discussions: {len(discussions)}")
    while i<len(discussions):
        if not(begin_found) and re.match(r"^[0-9XVI]*\.? *\w*Discussions?", discussions[i], re.IGNORECASE):
            # print(f"Begin found at {i}: {discussions[i]}")
            discussions = discussions[i+1:]
            begin_found = True
            i=0
        # Considering that it's unlikely for a line to start with the word abstract

        if begin_found and re.match(r"^[0-9XVI]*\.? *\w*(Acknowledgments?|Appendix|References?|Conclusions?)", discussions[i], re.IGNORECASE):
            # print(f"End found at {i}: {discussions[i]}")
            discussions = discussions[:i]
            break # No need to continue the script
        
        i+=1 
    
    if not begin_found:
        return []
        
        
    return discussions

def get_string(text: str):
    """
    Retourne la partie discussion dans le texte brut de l'article, sur plusieurs lignes formatées (~100 caractères).
    ⚠️ Ne doit pas être utilisé en même temps que get_list 

    Parameters
    ----------
    text: string
        Article ou partie de l'article en texte brut

    Returns
    -------
    str
        Texte formaté contenant la partie discussion
    """
    lines = get_list(text)
    return parser_utils.clean_and_format(lines)
        
        
        
        

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
            La partie discussion extrait du fichier passé en argument       
        
        Raises
        ------
        FileNotFoundError
            Quand l'ouverture du fichier n'a pas réussi
        """
        # if not(filepath.__contains__("mikheev")):
        #     return []
        with open(filepath, 'r', encoding="utf-8") as file:
            print(f"Ouverture du fichier {filepath}")
            c = file.read()
            parser_utils.set_content(c)
            return get_list(c)
            return get_string(c)
        raise FileNotFoundError(filepath)
    
    input_folder = "CORPUS_TXT"
    output_folder = "CORPUS_DISCUSSIONS"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open("discussions.md", 'w', encoding="utf-8") as mdf:
        for filename in os.listdir(input_folder):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            
            if os.path.isfile(input_path):
                abstract = test_gettxt(input_path)
                with open(output_path, 'w', encoding="utf-8") as output_file:
                    # output_file.write("\n".join(abstract))
                    output_file.write("\n".join(abstract))
                    
                # a2 = " ".join(abstract).strip()
                a2 = abstract
                a2 = "\n".join(abstract).strip()
                mdf.write(f"\n## {filename}\n```\n{a2}\n```\n")

