empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers) #[2, 4, 6, 8, 1, 3, 5, 7, 9]

sorted_numbers = sorted(numbers)
print(sorted_numbers) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

digits = sorted("432985617")
print(digits) #['1', '2', '3', '4', '5', '6', '7', '8', '9']
#note it prints it just as they were inputed, String = string, int = int

digits_two = list("432985617")
print(digits_two) #['4', '3', '2', '9', '8', '5', '6', '1', '7']


more_numbers = list(numbers)
print(more_numbers) #[2, 4, 6, 8, 1, 3, 5, 7, 9]
print(numbers is more_numbers) #False they are not the same lists
print(numbers == more_numbers) #True they contain same values
#OR

print()

more_numbers_two = numbers[:]
print(more_numbers_two) #[2, 4, 6, 8, 1, 3, 5, 7, 9]
print(numbers is more_numbers_two) #False
print(numbers == more_numbers_two) #True
#OR

print()

more_numbers_three = numbers.copy()
print(more_numbers_three) #[2, 4, 6, 8, 1, 3, 5, 7, 9]
print(numbers is more_numbers_three) #False
print(numbers == more_numbers_three) #True
