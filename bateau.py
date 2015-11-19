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
