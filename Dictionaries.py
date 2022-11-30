#dictionaries est une structure key value pair, avec un mot associé à une def pour le dico, une valeur à une chaine de caractere etc.

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])

#mieux de faire appel avec get qui a une valeur par default
print(monthConversions.get("Dec", "Not a valid key"))


