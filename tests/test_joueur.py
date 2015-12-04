from joueur import *
from bateau import *
import unittest

class TestJoueur(unittest.TestCase):
    def setUp(self):
        #definition de la taille des océans
        self.tailleX = 5
        self.tailleY = 5
        
        #Création du porte avion pour le joueur 1
        self.porteAvionJ1 = Bateau("porte-avion")
        self.porteAvionJ1.set_position(1,1,'haut',self.tailleX,self.tailleY)
        self.bateauxJ1 = []
        self.bateauxJ1.append(self.porteAvionJ1)

        #Création du porte avion pour le joueur 2
        self.porteAvionJ2 = Bateau("porte-avion")
        self.porteAvionJ2.set_position(1,1,'haut',self.tailleX,self.tailleY)
        self.bateauxJ2 = []
        self.bateauxJ2.append(self.porteAvionJ2)

        #Création des joueurs
        self.J1 = Joueur(self.tailleX, self.tailleY, self.bateauxJ1)
        self.J2 = Joueur(self.tailleX, self.tailleY, self.bateauxJ2)
        
    #def test_joueur(self):
        
        #bateaux = []
        #bateaux.append(Bateau("porte-avion"))
        #bateaux.append(Bateau("croiseur"))

        #bateaux[0].set_position(1,1,"haut",
        
        #joueur = Joueur(10,10, bateaux)

    def test_bateau_touche(self):

        #Tir du joueur 1 sur le joueur 2
        self.J1.tirer({1,1},J2)

        #Test sur l'unique bateau du joueur 2 sur sa première position
        #il doit etre touché
        self.assertEqual(self.J2.flotte[0].position[0][2], True)

