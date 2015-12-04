from joueur import *
from bateau import *
import unittest


class TestJoueur(unittest.TestCase):
    #def test_joueur(self):
        
        #bateaux = []
        #bateaux.append(Bateau("porte-avion"))
        #bateaux.append(Bateau("croiseur"))

        #bateaux[0].set_position(1,1,"haut",
        
        #joueur = Joueur(10,10, bateaux)

    def test_bateau_touche(self):
    
        #definition de la taille des océans
        tailleX = 5
        tailleY = 5
        
        #Création du porte avion pour le joueur 1
        porteAvionJ1 = Bateau("porte-avion")
        porteAvionJ1.set_position(1,1,'haut',tailleX,tailleY)
        bateauxJ1 = []
        bateauxJ1.append(porteAvionJ1)

        #Création du porte avion pour le joueur 2
        porteAvionJ2 = Bateau("porte-avion")
        porteAvionJ2.set_position(1,1,'haut',tailleX,tailleY)
        bateauxJ2 = []
        bateauxJ2.append(porteAvionJ2)

        #Création des joueurs
        J1 = Joueur(tailleX, tailleY, bateauxJ1)
        J2 = Joueur(tailleX, tailleY, bateauxJ2)

        #Tir du joueur 1 sur le joueur 2
        J1.tirer({1,1},J2)

        #Test sur l'unique bateau du joueur 2 sur sa première position
        #il doit etre touché
        self.assertEqual(J2.flotte[0].position[0][2], True)

        
