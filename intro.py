from pprint import pprint

class Fonctions :
    def start_up():
        print("Bonjour et bienvenue dans ce jeu de bataille navale merveilleux !")
        print("Voulez-vous jouer avec moi ?")
        jouer = input("Répondez O pour oui, N pour non... ")

        if jouer =="O" or jouer =="o":
            print("Yeahhh !")
            b = True
        else:
            print("Ohhh nonnnnn")
            b = False

        return b
    def saisir_params_ocean():
        print("Notre plus grand océan est de taille 10 * 10")
        print("Indiquer la taille de l'océan :")
        largeur = int(input("Quelle est la largeur de l'océan : "))
        hauteur = int(input("Quelle est la hauteur de l'océan : "))
        return hauteur, largeur

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





     

