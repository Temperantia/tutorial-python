# coding=UTF-8

# ceci est un commentaire
""" Ceci est commentaire
multiligne """

# types
"""
Python est typé dynamiquement
le type des variables est déduit lors de l'éxécution du script
"""
print('types :')

a = 3 # déclaration d'une variable a de valeur de type int valant 3
b = "hello" # déclaration d'une variable b de valeur de type str valant "hello"
c = 'world' # une string également
d = 3.2
print(b, a)
print(type(b))
print('a={:d} et b={:s}'.format(a, b)) # possibilité d'insertion dans la string principale

# cast
print('cast :')

e = int('3')
f = str(3)
g = float('3.2')

# string
print('string :')

h = 'test_string  '
print(h[0]) # affiche le premier caractère de la string
print(h[2:5]) # affiche les caractères entre 2 et 5
print(h.strip()) # affiche la string sans espace au début ni à la fin
print(len(h)) # affiche le nombre de caractères
