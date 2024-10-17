from random import *


def lecture_valeurs(filename: str) -> list:
    """
    Fonction qui ouvre le fichier designe par la string nomFichier,
    lit les valeurs numeriques du fichier et retourne la liste
    de ces valeurs.
    """
    with open(filename, "r") as f:
        # liste qui contiendra les valeurs numeriques du fichier
        l = []
        for ligne in f:
            # on convertit la ligne en float et on l'ajoute a notre liste
            l.append(float(ligne))

        # Remarque : on aurait aussi pu lire le fichier avec fichier.read() ou ficher.readline()
    return l


def source_aleatoire():
    """
    Fonction retournant une valeur aléatoire entre -1 et 1 choisie uniformément
    """
    return uniform(-1, 1)