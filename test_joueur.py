from plateau import *
from bateau import *
import unittest


class TestJoueur(unittest.TestCase):
    def test_joueur(self):
        
        bateaux = []
        bateaux.append(Bateau("Porte-avion"))
        bateaux.append(Bateau("Croiseur"))

        #bateaux[0].set_position(1,1,"haut",
        
        joueur = Joueur(10,10, bateaux)

        
