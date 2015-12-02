from plateau import *
from bateau import *
import unittest


class TestPlateau(unittest.TestCase):
    def test_plateau(self):
        
        bateaux = []
        bateaux.append(Bateau("Porte-avion"))
        bateaux.append(Bateau("Croiseur"))
        
        plateau = Joueur(10,10, bateaux)
