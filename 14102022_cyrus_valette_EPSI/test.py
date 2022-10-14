import txt as txt

# afficher le type de la variable
x = 5
print(type(x))

#spécification du type
y = int(20)

#liste
z = ["pomme", "poire", "kiwi"]
print(z)
print(type(z))


x = 3 + 5j
print(type(x))


#Convertion
x = float(1)
y=int(2.8)
z=complex(1)

print(x)
print(y)
print(z)

a = float(x)
b = int(y)
c = complex (x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# ma proposition pour l'exercice sur le random

#j'importe la biliothèque random
import random
#on initialise la variable, le choix est fait parmis 1 et 10. radint permet le choix au hazard entre deux entiers
x = random.randint(1, 10)
print(x)

#tableau de caractères
a = "Salut"
print(a[1])

#bouvcle for et identation
for x in "banane" :
    print(x)

#excercice longeur de la chaine lait
a = len("lait")
print(a)

#Exo trouver un mot dans une phrase
a = "Voila la phrase"
#on vérifie la condition
if "la" in a:
    print("trouvé")
#condition inverse
elif "la" not in a:
    print("ya pas")

#Le "slicing"

a = "exemple"
print(a[2:4])
#resultat em

#Comment afficher la position d’un caractère
print(a[3])
#il suffit d'ajouter : avant ou après une position et on peut obtenir le reste de la chaine avant ou après le mot

#si je peux afficher pl, au moins 2 solutions.. j’aimerais partir à l’envers de la chaine
print(a[-3:-1])
#en ajoutant - à la position  choisie, on part de la fin de la chaine de caractères


#tester
print(bool("hello"))
print(bool(15))
print(bool(None))
print(bool(0))
print(bool(False))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

def maFonction() :
    return True
print(maFonction())

#problème

x = random.randrange(0, 100)
x = type(x)
if x is int :
    print("c'est un entier")
else :
    print("c'est pas un entier")

#================================

x = float(1)
y = float(3.4)
z = float("6")
s = float("4.5")

#les tuples

a =(3,4,7)
print(type(a))

(b,c) = (5,6)

def test():
    return 5,6
a = test()
print(a)
#resultat: (5, 6)

b,c = test()
print(b,c)
#resultat = 5 6

for i in a:
    print(i)
#resultat: 5 (a la ligne) 6

print(a[0])
#resultat: 5

print(a[1])
#resustat: 6
b =(3,)
print(b)
print(type(b))
#resultat(3,) et tuple

#récupérer l'élément unique présent dans le tuple
c = b [0]
print(c)
d, = b
print(d)

#autre sytaxe nom_variable, =
u = [5]
v, = u
print(v)
print(type(v))

