import os
import sys
import re

# Dictionnaire des fichiers avec leur début et fin attendus dans la balise <corps> des fichiers XML
EXPECTED_CORPUS = {
    "ACL2004-HEADLINE.xml": {
        "start": "2 Previous Work Hedge Trimmer",
        "end": "event tracking for each method."
    },
    "Boudin-Torres-2006.xml": {
        "start": "2 Method The underlying idea",
        "end": "the DUC 2007 update corpus."
    },
    "compression_phrases_Prog-Linear-jair.xml": {
        "start": "2. Related Work In this",
        "end": "across corpora and evaluation paradigms."
    },
    "compression.xml": {
        "start": "2 Related Work We have",
        "end": "through appropriate feature weighting. 23"
    },
    "hybrid_approach.xml": {
        "start": "2 From Full Sentence to",
        "end": "the system deviced by Jing."
    },
    "marcu_statistics_sentence_pass_one.xml": {
        "start": "A noisy-channel model for sentence",
        "end": "techniques used by Magerman (1995)."
    },
    "mikheev.xml": {
        "start": "2. Performance Measure, Corpora for",
        "end": "for finding abbreviations in text."
    },
    "probabilistic_sentence_reduction.xml": {
        "start": "2 Support Vector Machine Support",
        "end": "± 0.25 8.40 ± 0.60"
    },
    "Stolcke_1996_Automatic_linguistic.xml": {
        "start": "2. THE IMPORTANCE OF LINGUISTIC",
        "end": "be modeled better this way."
    },
    "Torres.xml": {
        "start": "II. RELATED WORK One of",
        "end": "similar to the Spanish case."
    },
    "Word2Vec.xml": {
        "start": "2 Model Architectures Many different",
        "end": "be made using these techniques."
    },
}

def extract_corps_text(xml_path: str) -> str:
    """
    Extrait le texte de la balise <corps> d'un fichier XML.

    Parameters
    ----------
    xml_path : str
        Le chemin vers le fichier XML (DOIT ETRE VALIDE).

    Returns
    -------
    str
        Le texte contenu dans la balise <corps>, nettoyé des espaces multiples.

    Throws
    ------
    FileNotFoundError
        Si le fichier XML n'existe pas.
    Exception
        Pour toute autre erreur lors de l'ouverture ou de la lecture du fichier.
    """
    try:
        with open(xml_path, encoding='utf-8') as f:
            content = f.read()

        # Extraire manuellement le contenu de <corps>...</corps>
        match = re.search(r"<corps>\s*(.*?)\s*</corps>", content, re.DOTALL)
        text = match.group(1)
        text = re.sub(r"\s+", " ", text).strip()            # Nettoyage des espaces multiples
        return text
    except Exception as e:
        print(f"Erreur lors de l'ouverture de {xml_path} : {e}")
        return None


def test_corps_section(xml_folder: str):
    """
    Teste la section <corps> de chaque fichier XML dans le dossier spécifié.

    Parameters
    ----------
    xml_folder : str
        Le chemin vers le dossier contenant les fichiers XML.

    """
    all_passed = True # Variable pour suivre l'état des tests
    
    for filename, expected in EXPECTED_CORPUS.items():

        # On extrait le texte de la balise <corps> de chaque fichier XML
        xml_path = os.path.join(xml_folder, filename)
        text = extract_corps_text(xml_path)
        
        # On vérifie s'il y a du texte dans la balise <corps> de chaque fichier XML
        if not text:
            print(f"[ERREUR] Aucun contenu trouvé dans <corps> pour {filename}")
            all_passed = False
            continue

        # On récupère le début (5 premiers mots) et la fin (5 derniers mots) du texte
        first = " ".join(text.split()[:5])
        last = " ".join(text.split()[-5:])

        # On test si le début et la fin correspondent aux valeurs attendues dans le dictionnaire
        if first != expected["start"]:
            print(f"[ÉCHEC] Début incorrect dans {filename}\n  Attendu: '{expected['start']}'\n  Obtenu : '{first}'")
            all_passed = False
        if last != expected["end"]:
            print(f"[ÉCHEC] Fin incorrecte dans {filename}\n  Attendu: '{expected['end']}'\n  Obtenu : '{last}'")
            all_passed = False

    if all_passed:
        print("Tous les tests ont réussi !")
        exit(0)
    else:
        print("Des erreurs ont été détectées.")
        exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python test_parser_corps.py <dossier_xml>")
        sys.exit(1)

    xml_folder = sys.argv[1]
    test_corps_section(xml_folder)
