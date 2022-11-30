# hello world

print("hello world")

# drawing a shape

print("    /|")
print("   / |")
print("  /  |")
print(" /___|")

# Variable and data

character_name = "George"
character_age = 70

print(f"There once was a man named {character_name},")
print(f"he was {character_age} years old.")

# differentes manieres d'ecrire des variables et chronologie des variables

character_name = "John"
print(f"He really liked the name " + character_name + " ,")
print(f"but didn't like being {character_age}")

# Working with strings

# saut de ligne \n

print("Poney\ncheval")

# \" pour utiliser une "

print("\" Poney \"")

phrase = "J'aime le python"
print(phrase + " ehe ")

# Avec notre variable, on peut utiliser des fontions avec un . à la suite du nom de notre variable

# exemple, .isupper verifie si notre variable est en majuscule, et rep avec un booleen
print(phrase.isupper())

# dans cet exemple, .upper met en majuscule notre variable.
print(phrase.upper())
# chronologie et execution des fonctions et variables ligne par ligne.
print(phrase.isupper())

print(phrase.upper().isupper())

# combien de caracteres avec length
print(len(phrase))

# position d'une lettre, tabulation et indexe (un index part de 0 en Python)
print(phrase[0])

print(phrase.index("a"))

print(phrase.replace("J'aime", "Je deteste"))

# Working with numbers

# On peut faire des nombre entier, decimal etc. addition soustraction multiplication etc.

print(-2.0365+ 4 * 2)

# diviseur commun

print(10 % 3)

# var nombre

my_num = 5
print(my_num)

# on doit convertir un nombre en string avec str pour l'entourer de texte
print(str(my_num) + "my fav number")

# valeur absolue
my_num = -5
print(abs(my_num))

# pow nous permet de faire des squat, dans cet exemple 3^2
print(pow(3,2))

# comparaison
print(max(3,2))
print(min(3,2))

# les arrondis
print(round(3.2))

# bibli math rajoute des fonctions mathematiques

from math import *

my_num = 3.4

#arrondi par le bas
print(floor(my_num))

#arrondi par le haut
print(ceil(my_num))

# square
print(sqrt(36))

