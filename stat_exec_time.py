import numpy as np
import matplotlib.pyplot as plt

def analyze_execution_times(times: list) -> None:
    """
    Analyse les temps d'exécution et affiche des statistiques de base.
    Ces statistiques incluent le nombre d'éxécutions, le temps minimum, le temps maximum,
    la moyenne, la médiane, l'écart-type et la variance.

    Parameters
    ----------
    times : list
        Liste des temps d'exécution à analyser.
    """
    times = np.array(times)

    labels = [
        "Nombre d'exécutions",
        "Min",
        "Max",
        "Moyenne",
        "Médiane",
        "Écart-type"
    ]
    values = [
        f"{len(times)}",
        f"{times.min():.2f}s",
        f"{times.max():.2f}s",
        f"{times.mean():.2f}s",
        # np.median trie les valeurs, pas besoin de trier manuellement
        f"{np.median(times):.2f}s",
        f"{times.std():.2f}s",
    ]
    # calculer la longueur maximale pour l'alignement de l'affichage
    max_label_len = max(len(label) for label in labels)
    for label, value in zip(labels, values):
        print(f"{label:<{max_label_len}} : {value}")

def plot_execution_times(times: list) -> None:
    """
    Trace une courbe des temps d'exécution, en fonction de l'index d'éxécution.
    Trace également une courbe lissée pour une meilleure visualisation.

    Parameters
    ----------
    times : list
        Liste des temps
    """
    plt.figure(figsize=(10, 5))
    plt.plot(times, marker='o', linestyle='-', color='b', alpha=0.2, label='Temps brut')

    # Lissage avec une moyenne glissante
    window = 10  # taille de la fenêtre de lissage, ajustable
    if len(times) >= window:
        smooth_times = np.convolve(times, np.ones(window)/window, mode='valid')
        plt.plot(range(window-1, len(times)), smooth_times, color='r', linewidth=2, label=f'Moyenne glissante ({window})')

    plt.title('Temps d\'exécution en fonction de l\'index')
    plt.xlabel('Index d\'exécution')
    plt.ylabel('Temps (s)')
    plt.grid()
    plt.legend()
    plt.show()

def get_times(file: str) -> list:
    """
    Lit un fichier de log et extrait les temps d'exécution.
    Le fichier doit contenir des nombres flottants, un par ligne.

    Parameters
    ----------
    file : str
        Chemin vers le fichier de log.

    Returns
    -------
    list
        Liste des temps d'exécution extraits du fichier.
    """
    try:
        with open(file, "r") as f:
            times = [float(line.strip()) for line in f if line.strip()]
        return times
    
    except FileNotFoundError:
        print(f"Le fichier {file} n'existe pas.")
        exit(1)
    except ValueError:
        print(f"Erreur : le fichier {file} contient des valeurs non valides.")
        exit(1)


if __name__ == "__main__":
    # Exemple d'utilisation
    # python stat_exec_time.py

    # Exemple de retour:
    """
    Nombre d'exécutions : 182
    Min                 : 0.41s
    Max                 : 1.31s
    Moyenne             : 0.72s
    Médiane             : 0.52s
    Écart-type          : 0.31s
    """
    file = "exec_time_py.log"
    times = get_times(file)

    analyze_execution_times(times)
    plot_execution_times(times)



