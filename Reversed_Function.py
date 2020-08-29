data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]
print(data)

# 12 108
# 11 102
# 10 106
# 9 306
# 8 100
# 7 107
# 6 5
# 5 103
# 4 308
# 3 105
# 2 4
# 1 101
# 0 104
# [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]

# after telling which ones to delete
# 9 306
# 6 5
# 4 308
# 2 4
# [104, 101, 105, 103, 107, 100, 106, 102, 108]

