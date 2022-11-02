while True:
    try:
        x = int(input("id : "))
        break
    except ValueError:
        print("entrée invalide")
    finally:
        print("ok")
#====================================
try:
    2/0
except ZeroDivisionError:
    pass

#====================================
div = input()
try:
    div = int(div)
    if div == 1:
        raise ValueError()
except ValueError:
    print("Valeur saisie inutile, pas besoin de cet ordi")
else:
    print("le résutat est bon", 7/div)

#====================================
liste=range(20)
liste_1=[]
for x in liste:
    if x % 2 == 0:
        liste_1.append(x)
print(liste_1)

liste_2 = [x for x in liste if x % 2 == 0]
print(liste_2)

liste_3 = [str(x) for x in liste_2]
print(liste_3)

    #affichage des carrés de la liste 2
liste_4 = map(lambda num: num**2, liste_2)
print(liste_4)
for item in liste_4:
    print(item)

        #option 2 plus sympa
liste_5 = [num**2 for num in liste_2]
print(liste_5)

    #création d'un filtre
filtre_1 = [item for item in liste_2 if item]
print(filtre_1)

