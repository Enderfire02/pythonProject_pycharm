#====================================

nombres = range(20)
#création du dicitionnaire
dict_for = {}
for n in nombres:
    if n%2==0:
        dict_for[n] = n**2
print(dict_for)

#en utilisant la compréhention
dict_for2 = {n: n**2 for n in nombres if n%2 ==0}
print(dict_for2)

#réaliser une invertion avec la compréhention
equipe = {'Cristiano':'juve', 'Hakimi':'Dortmund', 'kante':'chelsea'}
equipe_joueur = {equipe[key]: key for key in equipe}
print(equipe)
print(equipe_joueur)

#=================EXERCICE===================
distance_m = {'v_1':100000, 'v_2':153000, 'v_3':700000}
distance_km = {key:distance_m[key]/1000 for key in distance_m}
distance_km_correction = {i:j/1000 for (i,j) in distance_m.items()}
print(distance_m)
print(distance_km)
print(distance_km_correction)

#================EXERCICE 2==================
distance_m2 = {'v_1':100, 'v_2':153000, 'v_3':700}
distance_km2 = {i: j/1000 for (i, j) in distance_m2.items() if j/1000>1}
print(distance_km2)

#imort ??
import logging
'''

logging.basicConfig(level=logging.INFO)
logging.debug('Message 1 log')
logging.warning('message')
logging.info('MM')

#fonctions

f_1 = lambda x,y:x*y
f_1(2,3)
print(f_1)
'''
d_1 = [[0], [1], [3], [10], [5]]


#exercice
def max_val(d):
    """Trouver la valeur maximale"""
    return max(d, key=lambda x:x)
max_val(d_1)
print(max_val(d_1))

