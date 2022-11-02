print(max("python"))
print(max(1,7,2))

class felins:
    def __init__(self, type_felin="tigre", couleur="orange" ):
        self.type_felin= "tigre"
        self.couleur = "orange"

class felins2:
    def __init__(self, type_felin="tigre", couleur="orange"):
        self.type_felin = type_felin
        self.couleur = couleur
    def __str__(self):
        return (" Le félin est de type {} et de couleur {}".format(self.couleur, self.type_felin))
    def def_couleur(self):
        return self.couleur
    def ch_couleur(self, valeur):
        self.couleur = valeur
    def def_type_felin(self):
        return self.type_felin
    def ch_type_felin(self, valeur):
        if valeur == "serpent":
            raise ValueError("non")
        self.type_felin = valeur
