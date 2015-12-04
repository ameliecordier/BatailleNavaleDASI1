import unittest
from interface import *


class Test_interface(unittest.TestCase):
    def test_start_up_mecanic(self):
        self.assertEqual(Interface.start_up_mecanic("O"), True)
        self.assertEqual(Interface.start_up_mecanic("n"), False)

    def test_saisir_params_ocean_mecanic(self):
        self.assertEqual(Interface.saisir_params_ocean_mecanic(5,5), True)
        self.assertEqual(Interface.saisir_params_ocean_mecanic(26,26), True)



