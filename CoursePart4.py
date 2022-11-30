# working with list

#creation d'une liste
friends = ["John","Bernard","Oscar","Alice"]

#appel des données dune liste
print(friends[2])
print(friends[-1])
print(friends[1:3])

#trier la liste dans l'ordre alphabetique
friends.sort()
print(friends)

#inverser l'ordre d'une liste
friends.reverse()
print(friends)

# modif de données dans une liste
friends[1] = "Mike"
print(friends[1])

# fonction with list
lucky_numbers = [4,3,6,8,52,46]
lucky_numbers.sort()
print(lucky_numbers)
friends = ["John","Bernard","Oscar","Alice"]

print(friends)

# fonction ajout avec append
friends.append("Creed")
print(friends)

# fonction ajout avec insert et la position de linsert

friends.insert(2,"John")
print(friends)

# fonction supprimer avec remove

friends.remove("John")
print(friends)

#recherche dans la liste avec index
print(friends.index("Creed"))

#pop un element random hors de la liste
friends.pop()
print(friends)

#suppr toute la liste
friends.clear()
print(friends)

#compter le nombre d'elements similaires
similar = ["Alice","Alice","Alice"]
print(similar.count("Alice"))

#copier une liste
numbers2 =lucky_numbers.copy()
print(numbers2)

#Tuples (similar to list) pas modifiable
coordinates = (3,6,7,8,9,4)
print(coordinates[3])