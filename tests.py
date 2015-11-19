import unittest
from intro import Fonctions


class Test_mesTests(unittest.TestCase):
    def test_ocean(self):
        ocean_test = Fonctions.construire_ocean(3, 4)

        self.assertEqual(len(ocean_test), 3)
        self.assertEqual(len(ocean_test[0]), 4)


unittest.main()
