from collections import OrderedDict

__author__ = 'phylante'
from pprint import pprint


class Ocean:
    def __init__(self, hauteur=0, largeur=0):
        self.ocean = self.construire_ocean(hauteur,
                                           largeur)

    def __len__(self):
        return len(self.ocean)

    def __getitem__(self, coords):
        """
        Permet d'adresser une case de l'ocean.
        Permet de demander une case avec la formulation ligne[pos]
        :param coords: un tuple style (A, 8)
        utilisation : ocean[('A', 8)]
        """
        lettre = coords[0]
        chiffre = coords[1]
        return self.ocean[lettre][chiffre]

    def largeur(self):
        if len(self.ocean) > 0:
            return len(self.ocean['A'])

    @staticmethod
    def saisir_params_ocean():
        try:
            print("Taille de l'océan ?")
            largeur_ocean = int(input("Largeur  :"))
            hauteur_ocean = int(input("Longueur : "))
            return hauteur_ocean, largeur_ocean
        except ValueError:
            return Ocean.saisir_params_ocean()

    def construire_ocean(self, hauteur_ocean, largeur_ocean):
        return [OrderedDict({chr(y + 65): ['O' for x in range(largeur_ocean)] for y in range(hauteur_ocean)})]

    def afficher_ocean(self):
        # On affiche les chiffres.
        for x in range(self.largeur() + 1):
            if x == 0:
                print("   ", end="")
            print(x, end=" ")

        # On affiche chaque ligne précédée de sa lettre.
        for key, ligne in self.ocean.items():
            ligne_a_afficher = key + " " + " ".join(ligne)
            print(ligne_a_afficher)

