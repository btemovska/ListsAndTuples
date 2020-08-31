for index, character in enumerate("abcdefgh"):
    print(index, character)
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e
# 5 f
# 6 g
# 7 h

for t in enumerate("abcdefgh"):
    print(t)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
# (5, 'f')
# (6, 'g')
# (7, 'h')

index, character = (0, 'a')
print(index) #0
print(character) #a

print()

for a in enumerate("abcdefgh"):
    index2, character2 = a
    print(index2, character2)
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e
# 5 f
# 6 g
# 7 h
