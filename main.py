from intro import Fonctions

testJouer = Fonctions.start_up()
if testJouer == True:
    h, l = Fonctions.saisir_params_ocean()
    o = Fonctions.construire_ocean(h, l)
    Fonctions.afficher_ocean(o)

else:
    print("au revoir")
    ## Quitter le programme
