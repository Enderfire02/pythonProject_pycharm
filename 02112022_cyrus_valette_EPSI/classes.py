class felins :
    famille ="mamifères placentaires"
    ordre = "carnivores"
    sous_ordre = "féliniformes"

    def mam_plac(self):
        "cosntructeur"
        print(self.famille)
def main():
    tigre = felins()
    tigre.mam_plac()

if  __name__ =='__main__':main()

#héritage
class tigres(felins):
    def __init__(self, type_felin, vitesse):
        self.type_felin = type_felin
        self.vitesse = vitesse
#méthode
T_1 = tigres("tigre", "100km/h")
T_2 = tigres("tigre", "110km/h")
print(T_1.vitesse)
print(T_2.famille)

print(issubclass(tigres,felins))
