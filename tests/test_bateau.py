from bateau import *
import unittest

class TestBateau(unittest.TestCase):
    def test_bateau(self):
        bateau = Bateau('porte-avion')
        self.assertEqual(bateau.taille, 5)

    def test_not_a_boat(self):
        self.assertRaises(KeyError, Bateau, 'pas_un_bateau')
        
    def test_get_statut_case(self):
        bateau = Bateau('porte-avion')
        self.assertEqual(bateau.getStatutCase(1,1),True)

    def test_set_position(self):
        bateau = Bateau('porte-avion')
        self.assertEqual(bateau.set_position(1,1,"droite",10,10),True)

    def test_bad_position(self):
        bateau = Bateau('porte-avion')
        self.assertEqual(bateau.set_position(1,1,"gauche",10,10),False)
        
    

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

