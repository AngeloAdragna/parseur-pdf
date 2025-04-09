# ------------------------------- Dépendances -------------------------------

import subprocess
import sys
import shutil
from pathlib import Path

import re

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

def list_pdfs(repertoire):
    '''
        Liste les documents pdf contenus dans un répertoire SUPPOSE VALIDE

        Entrée : repertoire, le nom d'un répertoire valide

        Sortie : Liste des fichiers pdf contenus dans le répertoire
    '''
    chemin = Path(repertoire)
    return list(chemin.glob("*.pdf"))


def pdfs_to_plain_texts(repertoire_entree: Path, repertoire_sortie: str):
    '''
        Crée le répertoire de sortie contenant les plaintext correspondant
        au parsing des pdf du répertoire

        Entrée : repertoire, le nom d'un répertoire valide

        Sortie : booléen indiquant la bonne exécution
    '''
    # D'abord vérifier que le répertoire d'entrée est bien différent de celui de sortie (il ne faut pas écraser l'entrée)
    if str(repertoire_entree) == repertoire_sortie:
        raise ValueError("Le repertoire d'entree et celui de sortie doivent etre differents")
    
    # Récupérer la liste des fichiers pdfs
    pdfs = list_pdfs(repertoire_entree)
    
    # Création du répertoire de sortie
    chemin = Path(repertoire_sortie)
    if chemin.exists():
        shutil.rmtree(chemin)                   # Supprime tout le répertoire existant
    chemin.mkdir(parents=True, exist_ok=True)   # Crée le répertoire de sortie

    for pdf in pdfs:
        convert_pdf_file_to_plain_text(pdf, repertoire_sortie)

def convert_pdf_file_to_plain_text(fichier_pdf: Path, repertoire_sortie: Path):
    ''' 
        Transforme un fichier pdf en plain text en l'intégrant au répertoire de sortie
    '''

    # Génèrer le chemin du fichier de sortie .txt
    fichier_sortie = Path(repertoire_sortie) / (fichier_pdf.stem + ".txt")

    try:
        subprocess.run(
            ["pdftotext", "-raw", str(fichier_pdf), str(fichier_sortie)],
            check=True
        )
        print(f"{fichier_pdf.name} converti en {fichier_sortie.name}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la conversion de {fichier_pdf.name} : {e}")



def get_file_name(fichier_txt : Path) -> str:
    '''
        Ajoute le nom du fichier à la première ligne du fichier texte

        Args:
            fichier_txt (Path): le chemin du fichier texte
        Returns:
            str: le nom du fichier texte sans l'extension
        
    '''
    return fichier_txt.stem
    

def add_infos_to_file(fichier_txt: Path) -> None:
    """"
        Ajoute les informations dans fichier texte. Le fichier ne contiendra
        que le nom du fichier, le titre et l'abstract.

        Args:
            fichier_txt (Path): le chemin du fichier texte
    """
    filename = get_file_name(fichier_txt)
    abstract = ""
    title = ""

    # ovewrite le fichier texte avec les nouvelles informations
    with open(fichier_txt, "w", encoding="utf-8") as f:
        f.write(f"Nom du fichier : {filename}\n")
        f.write(f"Titre : {title}\n")
        f.write(f"Abstract : {abstract}\n")

def main():
    if len(sys.argv) < 3:
        print("Erreur : Veuillez fournir les chemins du répertoire d’entrée et de sortie.")
        print("Exemple : python script.py dossier_entree/ dossier_sortie/")
        sys.exit(1)

    dossier_entree = sys.argv[1]
    dossier_sortie = sys.argv[2]
    chemin_entree = Path(dossier_entree)

    if not chemin_entree.exists() or not chemin_entree.is_dir():
        print(f"Erreur : Le chemin fourni n'existe pas ou n'est pas un répertoire : {chemin_entree}")
        sys.exit(1)

    pdfs = list_pdfs(chemin_entree)
    if not pdfs:
        print("Aucun fichier PDF trouvé dans ce répertoire.")
    else:
        print("Fichiers PDF trouvés :")
        for pdf in pdfs:
            print(" -", pdf.name)

    pdfs_to_plain_texts(chemin_entree, dossier_sortie)

if __name__ == "__main__":
    main()