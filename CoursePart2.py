# input from user (l'utilisateur peut interargir avec nous)

# intro input

name = input("Quel est ton nom: ")
age = input("Tu as quel age: ")
print("Bonjour " + name + "! Tu as " + age + " ans")

#use case: calculator

num1 = input("Enter a number:")
num2 = input("Enter another number:")

# la console converti les nombres en string, il faut donc les reconvertir en nombre, ici on utilise la focntion interger (int)
result = int(num1) + int(num2)
print(result)

# pb: ca marche pas pour les nombres decimaux, on doit donc utiliser float

num1 = input("Enter a number:")
num2 = input("Enter another number:")

result = float(num1) + float(num2)
print(result)