data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

for index in range(len(data) -1, -1, -1):
    if data[index] < min_valid or data[index] > max_valid:
        print(index, data)
        del data[index]
print(data) #[104, 101, 105, 103, 107, 100, 106, 102, 108] FINAL DATA

# 9 [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108] # at position 9 is 306 it will be deleted
# 6 [104, 101, 4, 105, 308, 103, 5, 107, 100, 106, 102, 108] # at position 6 we have 5 it will be deleted
# 4 [104, 101, 4, 105, 308, 103, 107, 100, 106, 102, 108]
# 2 [104, 101, 4, 105, 103, 107, 100, 106, 102, 108]

