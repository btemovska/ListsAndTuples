flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily"
]

# for flower in flowers:
#     print(flower)

separator = ", "
output = separator.join(flowers)
print(output)
#Daffodil, Evening Primrose, Hydrangea, Iris, Lavender, Sunflower, Tiger Lily
#the join method iterates over the list for us

#OR
print(", ".join(flowers))
#Daffodil, Evening Primrose, Hydrangea, Iris, Lavender, Sunflower, Tiger Lily

#NOTE this only works if we have a string to our list, it will not work if we have a ints



