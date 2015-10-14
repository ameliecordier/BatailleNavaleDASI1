from pprint import pprint
import unittest

def start_up(self):
    print("Bonjour et bienvenue dans ce jeu de bataille navale merveilleux !")
    print("Voulez-vous jouer avec moi ?")
    jouer = input("Répondez O pour oui, N pour non... ")

    if jouer =="O":
        print("Yeahhh !")
    else:
        print("Ohhh nonnnnn")

def saisir_params_ocean():
    print("Notre plus grand océan est de taille 10 * 10")
    print("Indiquer la taille de l'océan :")
    largeur = int(input("Quelle est la largeur de l'océan : "))
    hauteur = int(input("Quelle est la hauteur de l'océan : "))
    return hauteur, largeur

def construire_ocean(hauteur_ocean, largeur_ocean):
    ocean = []
    for liste in range(hauteur_ocean):
        ligne = []
        for case in range(largeur_ocean):
            ligne.append('O')
        ocean.append(ligne)
    return ocean


def afficher_ocean(ocean):
    pprint(ocean)



h, l = saisir_params_ocean()
o = construire_ocean(h, l)
afficher_ocean(o)


class Test_mesTests(unittest.TestCase):

    def test_stupide(self):
        self.assertEqual(1+1, 2)


unittest.main()

     

