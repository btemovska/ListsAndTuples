name = "Biljana"
age = 29

print(name, age, "Python", 2020) #Biljana 29 Python 2020
print(name, age, "Python", 2020, sep=", ") #Biljana, 29, Python, 2020 each value is separated by comma
#sep = separator, it is used when we have more then one value to pass in print

menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"]
]

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=" ") #items on same line
    print()
# egg bacon
# egg sausage bacon
# egg
# egg bacon
# egg bacon sausage
# bacon sausage
# sausage bacon tomato
# egg bacon

#note we used end this time because we only are passing one value, sep cannot be used here
