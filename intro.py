from pprint import pprint


class Fonctions:
    def start_up(self):
        print("Bonjour et bienvenue dans ce jeu de bataille navale merveilleux !")
        print("Voulez-vous jouer avec moi ?")
        jouer = input("Répondez O pour oui, N pour non... ")

        if jouer == "O":
            print("Yeahhh !")
        else:
            print("Ohhh nonnnnn")
