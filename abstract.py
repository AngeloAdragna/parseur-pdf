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
        text (str): _description_

    Returns:
        str: _description_
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
        pass
        # TODO: find the start
        
        
    return abstract
    pass


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
                abstract = " ".join(abstract_file(input_path)).strip()
                with open(output_path, 'w') as output_file:
                    output_file.write(abstract)
                    
                mdf.write(f"\n## {filename}\n```\n{abstract}\n```\n")

