from pprint import pprint
#from bateau import types_bateau



class Fonctions:
    def start_up():

        ok = False
        while (ok == False) :
            jouer = input(" Bonjour et bienvenue... voulez-vous jouer ? (o/n) : ")
                    
            if (jouer =="O" or jouer =="o"): 
                ok = True
                print("jouer !")
                b = True
            elif(jouer =="N" or jouer == "n") :
                ok = True
                print("Ohhh nonnnnn")
                b = False
        return b    

    def saisir_params_ocean():
        ok = False 
        print("Notre plus grand océan est de taille 26 * 26")
        print("Notre plus petit océan est de taille 5 * 5")
        print("Indiquer la taille de l'océan :")
        while (ok == False) :
            largeur = int(input("Quelle est la largeur de l'océan ? : "))
            hauteur = int(input("Quelle est la hauteur de l'océan ? : "))
            if( 5 < largeur < 26 and 5 < hauteur < 26 ):
                ok = True
            else :
                print("Valeur > 5 ou <26 attention")
        return hauteur, largeur

    def saisir_params_bateau():
        ok = False
        while (ok == False) :
            default_set =input("Voulez vous  jouer avec un set par default  ? (o/n) : ")
            if (default_set == "o" or default_set == "O"):
                ok = True
                print("Vous avez choisie un set par defaults \n *** set par défaut ** \n  1 porte-avions (5 cases) \n  1 croiseur (4 cases) \n  1 contre-torpilleurs (3 cases) \n  1 sous-marin (3 cases) \n  1 torpilleur (2 cases)  \n ******")
                #appeler la fonction creer set default#
            elif (default_set =="n" or default_set == "N"):
                for untype in types_bateau:
                   nombreBateau =input("Combien de ce type de bateau ( " +untype +") ? :" )
                   #if (nombreBateau > 0 ) :#
                       #int i = 1#
                       #while ( i <= nombreBateau)#
                           #Bateau b = Bateau.__init__(untype)#
                           #liste_bateaux.add(b)#
                           #i = i+1#
                 #ok = True
    
            else :
                ok = False
            


        return True
    def construire_ocean(hauteur_ocean, largeur_ocean):
        ocean = []
        for liste in range(hauteur_ocean):
            ligne = []
            for case in range(largeur_ocean):
                ligne.append('O')
            ocean.append(ligne)

        print("len(ocean) :" + str(len(ocean)))
        print("len(ocean[0]) :" + str(len(ocean[0])))

        return ocean

    def afficher_ocean(ocean):
        pprint(ocean)
