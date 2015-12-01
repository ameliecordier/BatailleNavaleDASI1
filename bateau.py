import ocean
import player

types_bateau = {
    'porte-avion': 5,
    'croiseur': 4,
    'sous-marin': 3,
    'contre-torpilleur': 3,
    'torpilleur': 2
}

class Bateau:
    def __init__(self, type):
        self.type = type
        self.taille = types_bateau[type]
	self.is_placed = False
	self.position = {}
	self.etat = True

    def set_position(self, x, y, orient, ocean):
    '''
    Positionne un bateau sur l'océan.
    '''
        
        if x >= 0 or y >= 0 or x <=  or y <= 10:
             
            if orient == 'haut':
                if (y-self.taille)>=0:
                    for i in range(0,self.taille-1) 
                        if ocean.getStatutCase(x,y-i):
                            self.position = {{x,y,orient}}
                            print("Le bateau a bien été placé.")
                else:
                    print("Le bateau n'est pas sur le plateau!")
            elif orient == 'bas':
                
            elif orient == 'gauche':
            else:
                
            self.is_placed = True
        else:
            print("Erreur de coordonées!")
        
        
        
    
