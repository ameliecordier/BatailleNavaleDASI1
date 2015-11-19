from bateau import *
import unittest

class TestBateau(unittest.TestCase):
    def test_bateau(self):
	    bateau = Bateau('porte-avion')
	    self.assertEqual(bateau.taille, 5)
		
    def test_not_a_boat(self):
	    self.assertRaises(KeyError, Bateau, 'pas_un_bateau')


### Test créer bateau
##a = creerBateau("Porte-Avion")
##assertEqual(a.longueur, 5)
##
##b = creerBateau("Croiseur")
##assertEqual(b.longueur, 4)
##
##c = creerBateau("Radeau")
##assertEqual(c.longueur, 1)
##
##d = creerBateau("Tank")
##assertRaises(ValueError)
##
##e = creerBateau(42)
##assertRaises(TypeError)
##
##
### Test ajouterBateaux
##
### Test 1
##armada = []
##monBateau = creerBateau("Porte-Avion")
##armada.ajouterBateau(monBateau)
##assertEqual(armada.len, 1)
##
### Test 2
##armada = []
##monBateau = creerBateau("Porte-Avion")
##armada.ajouterBateau(monBateau)
##assertEqual(armada.len, 1)
##monAutreBateau = creerBateau("Porte-Avion")
##armada.ajouterBateau(monAutreBateau)
##assertEqual(armada.len, 2)
##
##
###... et quoi d'autre ? 
##
