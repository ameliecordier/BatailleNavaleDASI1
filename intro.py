from pprint import pprint
def start_up(self):
    print("Bonjour et bienvenue dans ce jeu de bataille navale merveilleux !")
    print("Voulez-vous jouer avec moi ?")
    jouer = input("Répondez O pour oui, N pour non... ")

    if jouer =="O":
        print("Yeahhh !")
    else:
        print("Ohhh nonnnnn")

print("Indiquer la taille de l'océan :")
largeur_ocean = int(input("Quelle est la largeur de l'océan : "))
hauteur_ocean = int(input("Quelle est la hauteur de l'océan : "))

ocean = []
for liste in range(hauteur_ocean):
    ligne = []
    for case in range(largeur_ocean):
        ligne.append('O')
    ocean.append(ligne)
pprint(ocean)
     
