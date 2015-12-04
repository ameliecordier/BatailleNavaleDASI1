import ocean
#import joueur

#Pour lancer le test
#import unittest
#unittest.main(None, argv=['', 'discover', 'tests'])
#unittest.main(None, argv=['', 'test_bateau', 'tests'])

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
        self.position = []
        self.etat = True
        self.bateaux = []
    '''
    Vérifie que les coordonées sont juste.
    Positionne un bateau sur l'océan.
    '''
    def set_position(self, x, y, orient, maxX, maxY):
        messOk = "Le bateau a bien ete place."
        messErr = "Le bateau n est pas sur le plateau!"
        Ok = True
        if x >= 0 or y >= 0 or x <= maxX or y <= maxY or self.is_placed == False:
            
            if orient == 'haut':
                '''Test si le bateau ne sort pas de plateau  '''
                if (y-self.taille)>=0:
                    for i in range(0,self.taille-1): 
                        if self.getStatutCase(x,y-i):
                            e = True
                            unePos = [x,y-i,e]
                            self.position.append(unePos)
                else:
                    Ok = False
            elif orient == 'bas':
                if (y+self.taille)>=0:
                    for i in range(0,self.taille-1):
                        if self.getStatutCase(x,y+i):
                            e = True
                            unePos = [x,y+i,e]
                            self.position.append(unePos)
                else:
                    Ok = False
            elif orient == 'gauche':
                if (x-self.taille)>=0:
                    for i in range(0,self.taille-1): 
                        if self.getStatutCase(x-i,y):
                            e = True
                            unePos = [x-i,y,e]
                            self.position.append(unePos)
                else:
                    Ok = False
            else:
                if (x+self.taille)>=0:
                    for i in range(0,self.taille-1): 
                        if self.getStatutCase(x+i,y):
                            e = True
                            unePos = [x+i,y,e]
                            self.position.append(unePos)
                else:
                    Ok = False
                    
            self.bateaux.append(self.position)
            self.is_placed = True
        else:
            return "Erreur de coordonees!"

        return Ok

    def getStatutCase(self, x, y):
        return True
    
    def get_position(self):
        return self.position
