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