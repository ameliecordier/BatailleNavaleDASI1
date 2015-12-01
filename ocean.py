__author__ = 'phylante'
from pprint import pprint


class Ocean:
    def __init__(self, hauteur=0, largeur=0):
        self.ocean = self.construire_ocean(hauteur,
                                           largeur)

    def __len__(self):
        return len(self.ocean)

    def __getitem__(self, pos):
        """
        Permet d'adresser une case de l'ocean.
        Permet de demander une case avec la formulation ligne[pos]
        :param pos: selectionne la case de la ligne
        :return: la case pos de la ligne passée
        """
        return self.ocean[pos]

    def largeur(self):
        if len(self.ocean) > 0:
            return len(self.ocean[0])

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
        return [['O' for x in range(largeur_ocean)] for y in range(hauteur_ocean)]

    def afficher_ocean(self):
        for x in range(len(self.ocean)):
            print(" ".join(self.ocean[x]))
