from bateau import *
import unittest

class TestBateau(unittest.TestCase):
    def test_bateau(self):
	    bateau = Bateau('porte-avion')
	    self.assertEqual(bateau.taille, 5)
		
    def test_not_a_boat(self):
	    self.assertRaises(KeyError, Bateau, 'pas_un_bateau')
