#Reading Files

#avec r on est en read
readingFile = open("reading.txt", "r")

#avec w on est en write
# readingFile = open("reading.txt", "w")

#avec r+ on est en write + read
# readingFile = open("reading.txt", "r+")

print(readingFile.read())
# on peut aussi lire une seul ligne avec readline
print(readingFile.readline())

#test pour savoir si on peut lire le fichier
print(readingFile.readable())

# tout mettre dans une liste avec readlines
# print(readingFile.readlines())

# on lit la valeur de la liste
# print(readingFile.readlines()[1]

# On ferme le fichier
readingFile.close()

# on append / ajoute du texte
writeFile = open("reading.txt", "a")
writeFile.write("\npomme 2 terre")

# ecriture dans le file -> contrairement au a le w ecrase toute les données du fichier pour reecrire dessus
writeFile = open("reading.txt", "w")
writeFile.write("\npomme 2 terre")

#on peut aussi creer un new fichier
writeFile = open("reading2.txt", "w")
writeFile.write("\npomme 2 terre")