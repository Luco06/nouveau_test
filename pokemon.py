class pokemon():
    def __init__(self, nom, taille, couleur, evolution, rugissement, attaque1, attaque2):
        self.nom = nom
        self.taille = taille
        self.couleur = couleur
        self.evolution = evolution
        self.rug = rugissement
        self.attak1 = attaque1
        self.attak2 = attaque2
        
        
    def rugisement(self):
        print("Le pokemon crie " + self.rug)
    
    def metamorphose(self):
        self.nom = self.evolution
        print("Quoi !!! Mon pokemon evolue ")
        
    def pokemon_attaque1(self):
        print(self.nom + " Lance attaque " + self.attak1 + " !")
        
    def pokemon_attaque2(self):
        print(self.nom + " Lance attaque " + self.attak2 + " !")
    
    
    def getter_nom(self):
        return self.nom
    
    def setter_nom(self, nouveau_Nom):
        self.nom = nouveau_Nom
        
        