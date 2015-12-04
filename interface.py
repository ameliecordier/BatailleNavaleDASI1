# -*- coding: utf-8 -*-

from pprint import pprint
#from bateau import types_bateau



class Interface:
    def start_up():
        jouer = input(" Bonjour et bienvenue... voulez-vous jouer ? (o/n) : ")      
        start = Interface.start_up_mecanic(jouer)
           
        return start    

    def start_up_mecanic(jouer):
        if (jouer.lower()=="o"): 
            print("jouer !")
            start = True
            
        elif(jouer.lower() == "n") :
            print("Ohhh nonnnnn")
            start = False
        else :
            Interface.start_up()
        return start
    
    def saisir_params_ocean(first_try):
        if (first_try == True):
            print("Notre plus grand océan est de taille 26 * 26")
            print("Notre plus petit océan est de taille 5 * 5")
            print("Indiquer la taille de l'océan :")
        else :
            print("Valeur >= 5 ou <26 attention")
        largeur = int(input("Quelle est la largeur de l'océan ? : "))
        hauteur = int(input("Quelle est la hauteur de l'océan ? : "))
        Interface.saisir_params_ocean_mecanic(largeur, hauteur)
        return hauteur, largeur

    def saisir_params_ocean_mecanic(largeur, hauteur):
        if( 4 < largeur < 27 and 4 < hauteur < 27 ):
            ok = True
        else :
            Interface.saisir_params_ocean(False)
        return ok
        
    def saisir_set_bateaux(ocean):
        ok = False
        while (ok == False) :
            x = len(ocean)
            y =ocean.largeur()
            nbre_bateaux_max = x/5*y-1
            default_set =input("Voulez vous  jouer avec un set par default  ? (o/n) : ")
            if (default_set == "o" or default_set == "O"):
                ok = True
                print("Vous avez choisie un set par defaults \n *** set par défaut ** \n  1 porte-avions (5 cases) \n  1 croiseur (4 cases) \n  1 contre-torpilleurs (3 cases) \n  1 sous-marin (3 cases) \n  1 torpilleur (2 cases)  \n ******")
                #appeler la fonction creer set default#
            elif (default_set =="n" or default_set == "N"):
                nbre_bateaux = input("Combien de bateaux voulez vous pour votre set (min: 1, max: " + str(nbre_bateaux_max) + " ? : " )
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
   

