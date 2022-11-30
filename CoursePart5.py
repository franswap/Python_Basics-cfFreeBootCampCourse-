#Functions

#def de la fonction
def say_hi (name, age) :
    print("hello" + name + ", tu as " + age + " ans.")

#appel de la fonction
say_hi(" Mike", "12")

print("top")
say_hi(" Yolo", "8")
print("bottom")

print("\n")
print("**********************************************")
print("**********************************************")
print("**********************************************")
print("\n")

#Return statement in a fonction, le return execute seulement la ligne et break le reste de la fonction
def cube(num):
    return num*num*num

result = cube(4)
print(result)

print("\n")
print("**********************************************")
print("**********************************************")
print("**********************************************")
print("\n")

#Les boucles


is_male = False
is_tall = True

#if n°1
if is_male:
    print("you are a male")
else:
    print("you are a women")

#if n°2 avec 2 var + condition or et and et el
if is_male and is_tall:
    print("good job you win !")
elif is_male and not(is_tall):
    print("tu es petit !")
else:
    print("lets surrender !")

#comparaison
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3 :
        return num2
    else:
        return num3

print(max_num(3,40,5))

# Les classes et les objets

# Les classes

class fruits:

    def __init__(self, gout, forme, couleur, poids):
        self.gout = gout
        self.forme = forme
        self.couleur = couleur
        self.poids = poids