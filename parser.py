# ------------------------------- Dépendances -------------------------------

import subprocess
import sys
import shutil
from pathlib import Path
import time

from getTitle import extraire_titre_intelligent
import abstract as abstract_extractor

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

def list_pdfs(repertoire: Path) -> list:
    '''
        Liste les documents pdf contenus dans un répertoire, SUPPOSE VALIDE.

        Args:
            repertoire (Path): le chemin du répertoire à lister (DOIT ETRE VALIDE)
        Returns: 
            list: la liste des fichiers pdf contenus dans le répertoire
    '''
    chemin = Path(repertoire)
    return list(chemin.glob("*.pdf"))


def pdfs_to_plain_texts(repertoire_entree: Path, repertoire_sortie: str):
    '''
        Crée le répertoire de sortie contenant les plaintext correspondant
        au parsing des pdf du répertoire

        Args:
            repertoire_entree (Path): le chemin du répertoire d'entrée
            repertoire_sortie (str): le chemin du répertoire de sortie
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

    # Pour chaque pdf, on le convertit en texte
    for pdf in pdfs:
        convert_pdf_file_to_plain_text(pdf, repertoire_sortie)

def convert_pdf_file_to_plain_text(fichier_pdf: Path, repertoire_sortie: Path):
    ''' 
        Transforme un fichier pdf en plain text en l'intégrant au répertoire de sortie.
        Une fois transformé, le fichier texte est modifié pour ne contenir que le nom du fichier,
        le titre et l'abstract.

        Args:
            fichier_pdf (Path): le chemin du fichier pdf
            repertoire_sortie (Path): le chemin du répertoire de sortie
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

    # Overwrite le fichier texte avec les nouvelles informations
    add_infos_to_file(fichier_sortie)


def get_file_name(fichier_txt : Path) -> str:
    '''
        Ajoute le nom du fichier à la première ligne du fichier texte.

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
    title = extraire_titre_intelligent(fichier_txt)
    
    with open(fichier_txt, "r", encoding="utf-8") as f:
        content = f.read()
    abstract = abstract_extractor.get_string(content)

    # Overwrite le fichier texte avec les nouvelles informations
    with open(fichier_txt, "w", encoding="utf-8") as f:
        f.write(f"Nom du fichier : {filename}\n")
        f.write(f"Titre : {title}\n")
        f.write(f"Abstract : {abstract}\n")

def log_execution_time(duration: float, log_file: Path = Path("exec_time.log")) -> None:
    """
    Enregistre le temps d'exécution dans un fichier de log et affiche la moyenne des temps.

    Args:
        duration (float): Le temps d'exécution en secondes.
        log_file (Path): Le chemin du fichier de log.
    """
    try:
        # Ajouter le temps d'exécution au fichier de log
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"{duration:.2f}\n")

        # Lire tous les temps d'exécution du fichier de log
        with open(log_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Calculer la moyenne des temps d'exécution
        times = []
        for line in lines:
            try:
                times.append(float(line.strip()))
            except ValueError:
                print(f"Ligne ignorée dans le fichier de log : {line.strip()}")

        if times:
            average_time = sum(times) / len(times)
            print(f"Moyenne des temps d'exécution : {average_time:.2f} secondes")
        else:
            print("Aucune donnée valide dans le fichier de log.")

    except Exception as e:
        print(f"Erreur lors de la gestion du fichier de log : {e}")

def main():

    # Exemple d'utilisation:
    # python script.py CORPUS_TRAIN/ CORPUS_TXT/
    
    # Résultat attendu:
    # Le répértoire CORPUS_TXT/ contiendra les fichiers texte
    # avec uniquement le nom du fichier, le titre et l'abstract

    # Début de la mesure du temps
    start_time = time.time()

    if len(sys.argv) < 3:
        print("Erreur : Veuillez fournir les chemins du répertoire d’entrée et de sortie.")
        print("Exemple : python script.py dossier_entree/ dossier_sortie/")
        sys.exit(1)

    dossier_entree = sys.argv[1]
    dossier_sortie = sys.argv[2]
    chemin_entree = Path(dossier_entree)

    # Génère une erreur si le répertoire d'entrée n'existe pas ou n'est pas un répertoire
    if not chemin_entree.exists() or not chemin_entree.is_dir():
        print(f"Erreur : Le chemin fourni n'existe pas ou n'est pas un répertoire : {chemin_entree}")
        sys.exit(1)

    # Si au moins un fichier pdf est trouvé, on continue
    pdfs = list_pdfs(chemin_entree)
    if not pdfs:
        print("Aucun fichier PDF trouvé dans ce répertoire.")
    else:
        print("Fichiers PDF trouvés :")
        for pdf in pdfs:
            print(" -", pdf.name)

    # Convertir les fichiers PDF en texte
    pdfs_to_plain_texts(chemin_entree, dossier_sortie)

    # Fin de la mesure du temps
    end_time = time.time()
    # Log de la durée d'exécution
    log_execution_time(end_time - start_time)

if __name__ == "__main__":
    main()