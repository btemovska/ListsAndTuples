shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

another_list = shopping_list
print(id(shopping_list)) #1696247908992
print(id(another_list)) #1696247908992

#lets attempt to mutate the list (we've added it)
shopping_list += ["cookies"]
print(shopping_list) #['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies']
print(id(shopping_list)) #1696247908992 id is the same bc lists are mutable
    #python was able to add a new item without creating a new list
print(another_list) #['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies']

print("------")

a = b = c = d = e = f = another_list #chain assigments
print(a) #['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies']
print("Adding cream") #Adding cream
a.append("Cream")
print(c) #['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies', 'Cream']
print(d) #['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies', 'Cream']

print(e)  #yes it is same
print(f)

