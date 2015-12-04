import unittest
from ocean import *


class TestOcean(unittest.TestCase):
    def test_ocean_construire_ocean(self):
        """
        construire_ocean n'est pas une methode statique, on doit donc instancier un ocean,
        et constuire_ocean est la seule methode appelee dans le constructeur, on va donc tester en instanciant l'ocean,
        puis on regarde si on obtient bien un ocean à la bonne taille.
        """
        self.assertIsInstance(self.o, Ocean)
        self.assertEqual(len(self.o), 12)
        self.assertEqual(self.o.largeur(), 14)

    def test_ocean_largeur(self):
        """
        On teste la methode largeur()
        """
        self.assertEqual(self.o.largeur(), 12)

    def test_ocean_longueur(self):
        """
        On teste la redefinition de __len__
        """
        self.assertEqual(len(self.o), 14)

    def test_param_negatifs(self):
        """
        Si on essaye de creer un ocean de taille negative, on doit ne rien renvoyer.
        """
        o2 = Ocean(-1, -1)
        self.assertIsNone(o2)
        del o2

    def test_ocean_getitem(self):
        """
        teste l'acces à une case.
        :return:
        """
        self.assertEqual(self.o[('A', 1)], 'O')

    def setUp(self):
        self.o = Ocean(12, 14)

    def tearDown(self):
        """
        On pourrait se passer du tearDown, mais c'est pour être explicite
        :return:
        """
        del self.o

    def __main__(self):
        self.test_ocean_construire_ocean()
        self.test_ocean_largeur()
        self.test_ocean_longueur()
        self.test_param_negatifs()
        self.test_ocean_getitem()
