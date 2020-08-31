t = "a", "b", "c"
print(t)#('a', 'b', 'c') <= this is tuples

name = "Biljana"
age = 10
print(name, age, "Python", 2020) #Biljana 10 Python 2020
print((name, age, "Python", 2020)) #('Biljana', 10, 'Python', 2020)


welcome = "Welcome to the Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984
print(metallica) #('Ride the Lightning', 'Metallica', 1984)
print(metallica[0]) #Ride the Lightning
print(metallica[1]) #Metallica
print(metallica[2]) #1984

#NOTE, they are immutable, thus you can't change what is in index 1 or 2 or 0, etc...
#Lists are mutable
#Tuples are immutable


#if you want to change the data of tuples, create a list, than change it
metallica2 = list(metallica)
print(metallica2) #['Ride the Lightning', 'Metallica', 1984]
metallica2[0] = "Master of Puppets"
print(metallica2) #['Master of Puppets', 'Metallica', 1984]

