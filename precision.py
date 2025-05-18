import argparse
import xml.etree.ElementTree as ET

def compute_precisions(xml_file_path: str) -> None:
    """
    Calcule la précision de la détection de frontières à partir d'un fichier XML devant respecter un format spécifique.
    Le fichier XML doit contenir des éléments <document> avec des attributs et des sous-éléments spécifiques.
    La précision est calculée comme le rapport entre le nombre de frontières correctes et le nombre de frontières trouvées.

    Parameters
    ----------
    xml_file_path : str
        Chemin vers le fichier XML à analyser.

    Returns
    -------
    None
        Affiche la précision pour chaque document dans le fichier XML.
    """
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        results = []
        global_precision = 0
        
        # On cherche les balises <document> et les balises enfants <frontieres-trouvees> et <frontieres-correctes>
        for doc in root.findall("document"):
            nom = doc.attrib.get("nom", "Nom inconnu")
            ft_elem = doc.find("frontieres-trouvees")
            fc_elem = doc.find("frontieres-correctes")

            if ft_elem is None or fc_elem is None:
                results.append((nom, "Balises manquantes"))
                continue

            try:
                # On récupère les valeurs des balises <frontieres-trouvees> et <frontieres-correctes>
                frontieres_trouvees = int(ft_elem.text.strip())
                frontieres_correctes = int(fc_elem.text.strip())

                if frontieres_trouvees == 0:
                    results.append((nom, "Précision indéfinie (0 trouvées)"))
                else:
                    # Calcul de la précision
                    precision = frontieres_correctes / frontieres_trouvees
                    global_precision += precision
                    results.append((nom, f"{precision:.2%} ({frontieres_correctes}/{frontieres_trouvees})"))
            except ValueError:
                results.append((nom, "Valeurs non entières"))
        
        # Alignement pour l'affichage des résultats
        max_name_length = max(len(nom) for nom, _ in results)
        for nom, precision_str in results:
            print(f"{nom.ljust(max_name_length)} : {precision_str}")

        # Affichage de la précision globale
        global_precision = global_precision / len(results)
        print(f"\nPrécision globale : {global_precision:.2%}")

    except FileNotFoundError:
        print(f"Erreur : fichier non trouvé : {xml_file_path}")
    except ET.ParseError:
        print(f"Erreur : fichier XML mal formé : {xml_file_path}")

if __name__ == "__main__":
    # python precision.py frontieres.xml

    parser = argparse.ArgumentParser(description="Calcule la précision à partir d’un fichier XML.")
    parser.add_argument("xml_file", type=str, help="Chemin vers le fichier XML à analyser.")
    args = parser.parse_args()

    compute_precisions(args.xml_file)
