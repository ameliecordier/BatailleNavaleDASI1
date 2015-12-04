class Ocean:
    def __init__(self, hauteur=0, largeur=0):
        """
        Utilisation : mon_ocean = Ocean(hauteur, largeur)
        :param hauteur:
        :param largeur:
        :return: un ocean
        """
        self.ocean = self.construire_ocean(hauteur,
                                           largeur)

    def __len__(self):
        """
        s'utilise avec len(ocean)
        :return: la hauteur de l'ocean
        """
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
        """
        s'utilise : ocean.largeur()
        :return: la largeur de l'ocean.
        """
        if len(self.ocean) > 0:
            return len(self.ocean['A'])
        else:
            return 0

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
        return {chr(y + 65): ['O' for x in range(largeur_ocean)] for y in range(hauteur_ocean)}

    def afficher_ocean(self):
        # On affiche les chiffres.
        for x in range(self.largeur() + 1):
            if x == 0:
                print("   ", end="")
            elif x < 10:
                print(x, end="  ")
            else:
                print(x, end=" ")
        print("")

        for cle in [chr(y + 65) for y in range(len(self))]:
            ligne_a_afficher = cle + "  " + "  ".join(self.ocean[cle])
            print(ligne_a_afficher)
