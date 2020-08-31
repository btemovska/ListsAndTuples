albums = [("Welcome to the Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]
print(len(albums))  # 5 there are 5 tuples, each contain 3 items

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))
# Album: Welcome to the Nightmare, Artist: Alice Cooper, Year: 1975
# Album: Bad Company, Artist: Bad Company, Year: 1974
# Album: Nightflight, Artist: Budgie, Year: 1981
# Album: More Mayhem, Artist: Emilda May, Year: 2011
# Album: Ride the Lightning, Artist: Metallica, Year: 1984


