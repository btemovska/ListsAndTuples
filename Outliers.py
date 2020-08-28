data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

del data[0:2]
print(data)
#[104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]

#note, now the list is updated and there are 16 out of the 18 initial
#so if you want to remove the last two start at 14
del data[14:]
print(data) #[104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191]

#make it automatically
data_two = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200
for index, value in enumerate(data_two):
    if(value < min_valid) or (value > max_valid):
        del data_two[index]
print(data_two) #[5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 360]
#note this did not work because it skips through 5 as the value of 5 on the updated list is at index 0
# BE CAREFUL!
print("Make it automatic the right way")
#make it automatically the right way
data_three = [4, 5, 104, 105, 110, 120, 130, 130, 150,
            160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid_three = 100
max_valid_three = 200

stop = 0
for index_three, value in enumerate(data_three):
    if value >= min_valid_three:
        stop = index_three
        break
print(stop) #2
del data_three[:stop]
print(data_three) #[104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
#deleted the values up to but not indlucing 2

# process the high values in the list
start = 0
for index_four in range(len(data_three) -1, -1, -1):
    if data_three[index_four] <= max_valid_three:
        start = index_four
        break
print(start) #13
del data_three[start:]
print(data_three) #[104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188]
#deleted everything from position 13 through the end




