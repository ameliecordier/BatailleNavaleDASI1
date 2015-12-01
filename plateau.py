from intro import Fonctions
from ocean import Ocean

class Joueur:
    
    def __init__(self, tailleoceanx, tailleoceany):
        
        ocean1 = Ocean(tailleoceanx,tailleoceany)
        #flotte1 = Fonctions.creeFlotte()
        
    def jouer(self, position):
        #parcours de la liste des bateaux adverses pour voir si touché
        #si touché: X à la position dans l'océan
        #si tir manqué: I
        
        
    def afficherAdversaire(self):
        #afficher océan connu de l'adversaire
        ocean1.afficher_ocean()

    def afficherSoi(self):
        #afficher océan du joueur actif
        ocean_temporaire = Ocean(tailleoceanx,tailleoceany)

        #for bateau in flotte1:
            #i est un bâteau
         #   for ObjetPos in bateau.listepos:
          #      if ObjetPos.etat:
           #         ocean_temporaire[ObjetPos.x][ObjetPos.y] = '\'
            #    else:
             #       ocean_temporaire[ObjetPos.x][ObjetPos.y] = '€'
                    
        ocean_temporaire.afficher_ocean()
                    
        
