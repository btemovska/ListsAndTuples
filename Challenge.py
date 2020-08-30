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

#white code to print out all meals in the menu but with spam removed

for meal in menu:
    for index in range(len(meal) - 1, - 1, - 1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)

# ['egg', 'bacon']
# ['egg', 'sausage', 'bacon']
# ['egg']
# ['egg', 'bacon']
# ['egg', 'bacon', 'sausage']
# ['bacon', 'sausage']
# ['sausage', 'bacon', 'tomato']
# ['egg', 'bacon']
