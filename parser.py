# ------------------------------- Dépendances -------------------------------

import subprocess
import sys
import argparse
import shutil
from pathlib import Path
import time

import parser_title
import parser_abstract
import parser_biblio
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


def pdfs_to_format(repertoire_entree: Path, repertoire_sortie: str, args):
    '''
        Crée le répertoire de sortie contenant les plaintext (ou xml) correspondant
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
        convert_pdf_file(pdf, repertoire_sortie, args)


def convert_pdf_file(fichier_pdf: Path, repertoire_sortie: Path, args):
    ''' 
        Transforme un fichier pdf en plain text (ou xml) en l'intégrant au répertoire de sortie.
        Une fois transformé, le fichier texte (ou xml) est modifié pour ne contenir que les éléments demandés par le client.

        Args:
            fichier_pdf (Path): le chemin du fichier pdf
            repertoire_sortie (Path): le chemin du répertoire de sortie
    '''
    fichier_sortie = None
    if args.t or args.r :
        # Génèrer le chemin du fichier de sortie .txt
        fichier_sortie = Path(repertoire_sortie) / (fichier_pdf.stem + ".txt")
    elif args.x :
        # Génèrer le chemin du fichier de sortie .xml
        fichier_sortie = Path(repertoire_sortie) / (fichier_pdf.stem + ".xml")

    try:
        subprocess.run(
            ["pdftotext", "-raw", str(fichier_pdf), str(fichier_sortie)],
            check=True
        )
        print(f"{fichier_pdf.name} converti en {fichier_sortie.name}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la conversion de {fichier_pdf.name} : {e}")

    # Overwrite le fichier de sortie avec les nouvelles informations
    add_infos_to_file(fichier_sortie, args)


def get_file_name(fichier : Path) -> str:
    '''
        Ajoute le nom du fichier à la première ligne du fichier texte (ou xml).

        Args:
            fichier (Path): le chemin du fichier texte (ou xml)
        Returns:
            str: le nom du fichier texte (ou xml) sans l'extension
        
    '''
    return fichier.stem
    

def add_infos_to_file(fichier: Path, args) -> None:
    """"
        Ajoute les informations dans fichier texte (ou xml).

        Le fichier contiendra :
        - Fichier texte :
            . nom du fichier
            . titre
            . abstract

        - Fichier xml :
            . nom du fichier
            . titre
            . auteurs
            . abstract
            . références

        Args:
            fichier (Path): le chemin du fichier texte
    """
    filename = get_file_name(fichier)
    with open(fichier, "r", encoding="utf-8") as f:
        content = f.read()
    title = parser_title.get_string(content)   
    abstract = parser_abstract.get_string(content)

    # si r en argument, on veut laisser la sortie de pdftotext -raw dans les fichiers de sortie
    if not args.r :

        # Overwrite le fichier texte avec les nouvelles informations
        with open(fichier, "w", encoding="utf-8") as f:
            if args.t :
                # CAS DU PARSING AU FORMAT PLAIN TEXT
                f.write(f"Nom du fichier : {filename}\n")
                f.write(f"Titre : {title}\n")
                f.write(f"Abstract : {abstract}\n")
            elif args.x :
                # CAS DU PARSING AU FORMAT XML
                # TODO : Récupérer le tableau d'auteurs
                auteur = []
                # Récupérer la bibliographie
                biblio = parser_biblio.get_list(content)

                f.write("<article>\n")

                f.write(f"\t<preamble>\n\t\t{filename}\n\t</preamble>\n")

                f.write(f"\t<titre>\n\t\t{title}\n\t</titre>\n")
                
                f.write("\t<auteur>\n")
                for a in auteur:
                    f.write(f"\t\t{a}\n")
                f.write("\t</auteur>\n")

                f.write(f"\t<abstract>\n\t\t{abstract}\n\t</abstract>\n")

                f.write("\t<biblio>\n")
                for b in biblio:
                    f.write(f"\t\t{b}\n")
                f.write("\t</biblio>\n")

                f.write("</article>")


def log_execution_time(duration: float, log_file: Path = Path("exec_time_py.log")) -> None:
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

def parse_arguments():
    """
    Parse les arguments de la ligne de commande pour inclure les options -t et -x.
    Assure que les options -t et -x ne sont pas cumulables, et que -t est sélectionné par défaut si aucun n'est passé.

    Returns:
        Namespace: Les arguments parsés.
    """
    parser = argparse.ArgumentParser(description="Script de conversion de PDF en texte avec options.")
    parser.add_argument("dossier_entree", type=str, help="Chemin du répertoire d'entrée contenant les fichiers PDF.")
    parser.add_argument("dossier_sortie", type=str, help="Chemin du répertoire de sortie pour les fichiers parsés.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-t", action="store_true", help="Parser en plain text (par défaut).")
    group.add_argument("-x", action="store_true", help="Parser en XML.")
    group.add_argument("-r", action="store_true", help="Les fichiers texte contiennent la sortie de pdftotext -raw (pour tests)" )
    args = parser.parse_args()

    # Si aucune option n'est spécifiée, -t est sélectionné par défaut
    if not args.t and not args.x and not args.r:
        args.t = True

    return args

def main():

    # Exemples d'utilisation:
    #  Format txt sans option  : python parser.py CORPUS_TRAIN/ CORPUS_TXT/
    #  Format txt avec option  : python parser.py -t CORPUS_TRAIN/ CORPUS_TXT/
    #  Format xml              : python parser.py -x CORPUS_TRAIN/ CORPUS_XML/
    #  Format txt non formaté  : python parser.py -r CORPUS_TRAIN/ CORPUS_TXT/
    
    # Résultats attendus:
    # Le répértoire CORPUS_TXT/ contiendra les fichiers texte avec uniquement le nom du fichier, le titre et l'abstract
    # (ou le texte brut si -r est spécifié)
    # Le répértoire CORPUS_XML/ contiendra les fichiers texte avec toutes les infos demandées pour le xml

    # Début de la mesure du temps
    start_time = time.time()

    args = parse_arguments()

    dossier_entree = args.dossier_entree
    dossier_sortie = args.dossier_sortie
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
    pdfs_to_format(chemin_entree, dossier_sortie, args)

    # Fin de la mesure du temps
    end_time = time.time()
    # Log de la durée d'exécution
    log_execution_time(end_time - start_time)

if __name__ == "__main__":
    main()