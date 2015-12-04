# -*- coding: utf-8 -*-

from interface import Interface
from ocean import Ocean

testJouer = Interface.start_up()
if testJouer == True:
    h, l = Interface.saisir_params_ocean(True)
    o1 = Ocean()
    o1.construire_ocean(h, l)
    #o1.afficher_ocean()
    #Interface.saisir_params_bateau(o1)

else:
    print("au revoir")
    ## Quitter le programme
