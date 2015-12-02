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
    Vérifie que les coordonées sont juste.
    Positionne un bateau sur l'océan.
    '''
        messOk = "Le bateau a bien été placé."
        messErr = "Le bateau n'est pas sur le plateau!"
        if x >= 0 or y >= 0 or x <=  or y <= 10:
            
            if orient == 'haut':
                if (y-self.taille)>=0:
                    for i in range(0,self.taille-1) 
                        if ocean.getStatutCase(x,y-i):
                            self.position = {{x,y-i,e}}
                            print(messOk)
                else:
                    print(messErr)
            elif orient == 'bas':
                if (y+self.taille)>=0:
                        for i in range(0,self.taille-1) 
                            if ocean.getStatutCase(x,y+i):
                                self.position = {{x,y+i,e}}
                                print(messOk)
                else:
                    print(messErr)    
            elif orient == 'gauche':
                if (x-self.taille)>=0:
                    for i in range(0,self.taille-1) 
                        if ocean.getStatutCase(x-i,y):
                            self.position = {{x-i,y,e}}
                            print(messOk)
                else:
                    print(messErr)
            else:
                if (x+self.taille)>=0:
                    for i in range(0,self.taille-1) 
                        if ocean.getStatutCase(x+i,y):
                            self.position = {{x+i,y,e}}
                            print(messOk)
                else:
                    print(messErr)
            self.is_placed = True
        else:
            print("Erreur de coordonées!")

    def get_position(self):
        return self.position
