import ocean
import joueur

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
        self.bateaux = {}
    '''
    Vérifie que les coordonées sont juste.
    Positionne un bateau sur l'océan.
    '''
    def set_position(self, x, y, orient, maxX, maxY):
        messOk = "Le bateau a bien ete place."
        messErr = "Le bateau n est pas sur le plateau!" 
        if x >= 0 or y >= 0 or x <= maxX or y <= maxY:
            
            if orient == 'haut':
                '''Test si le bateau ne sort pas de plateau  '''
                if (y-self.taille)>=0:
                    for i in range(0,self.taille-1): 
                        if self.getStatutCase(x,y-i):
                            self.position.append({x,y-i,e})
                            print(messOk)
                else:
                    print(messErr)
            elif orient == 'bas':
                if (y+self.taille)>=0:
                    for i in range(0,self.taille-1):
                        if self.getStatutCase(x,y+i):
                            self.position.append({x,y+i,e})
                            print(messOk)
                else:
                    print(messErr)    
            elif orient == 'gauche':
                if (x-self.taille)>=0:
                    for i in range(0,self.taille-1): 
                        if self.getStatutCase(x-i,y):
                            self.position.append({x-i,y,e})
                            print(messOk)
                else:
                    print(messErr)
            else:
                if (x+self.taille)>=0:
                    for i in range(0,self.taille-1): 
                        if self.getStatutCase(x+i,y):
                            self.position.append({x+i,y,e})
                            print(messOk)
                else:
                    print(messErr)
            self.bateaux.append(self.position)
            self.is_placed = True
        else:
            print("Erreur de coordonees!")

    def getStatutCase(self, x, y):
        return True
    
    def get_position(self):
        return self.position
