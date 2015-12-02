import unittest
from ocean import *


class Test_mesTests(unittest.TestCase):
    def test_ocean_size(self):
        o = Ocean(4, 2)
        self.assertEqual(len(o), 4)
        self.assertEqual(o.largeur(), 2)


