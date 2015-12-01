from intro import Fonctions
from ocean import Ocean

class Joueur:
    
    def __init__(self, tailleoceanx, tailleoceany):
        
        ocean1 = Ocean(tailleoceanx,tailleoceany)
        flotte1 # = Fonctions.creeFlotte()
        
    def jouer(self, position, adversaire):
        
        #for bateau in adversaire.flotte1:
         #   for ObjetPos in bateau.listepos:
          #      if ObjetPos.x == position.posX and ObjetPos.y == position.posY:
           #         ObjetPos.etat = True
            #        ocean1[position.x][position.y] = 'X'
             #      return
             #ocean1[position.x][position.y] = 'I'

             
        
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

         #   for ObjetPos in bateau.listepos:
          #      if ObjetPos.etat:
           #         ocean_temporaire[ObjetPos.x][ObjetPos.y] = '\'
            #    else:
             #       ocean_temporaire[ObjetPos.x][ObjetPos.y] = '€'
                    
        ocean_temporaire.afficher_ocean()
                    
        
