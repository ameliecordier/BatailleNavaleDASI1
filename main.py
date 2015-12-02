from intro import Fonctions
from ocean import Ocean

testJouer = Fonctions.start_up()
if testJouer == True:
    h, l = Fonctions.saisir_params_ocean()
    o1 = Ocean()
    o1.construire_ocean(h, l)
    #o1.afficher_ocean()
    Fonctions.saisir_params_bateau(o1)

else:
    print("au revoir")
    ## Quitter le programme
