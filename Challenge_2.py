#use a for loop to produe a list of ints, rather than strings.
# you can either modify hte contents of the 'values_list' list in place,
# or create a new list of ints

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values) #9 223 372 036 854 775 807

values_list = values.split()
print(values_list) #['9', '223', '372', '036', '854', '775', '807']

# 1 way
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])
print(values_list) #[9, 223, 372, 36, 854, 775, 807]

# 2 way
integer_values = []
for value in values_list:
    integer_values.append(int(value))
print(integer_values) #[9, 223, 372, 36, 854, 775, 807]

