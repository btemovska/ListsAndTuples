pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram)
print(letters) #[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
            # 'T', 'a', 'b', 'c', 'd', 'e', 'e', 'e', 'f', 'g', 'h', 'h', 'i','j', 'k', 'l', 'm', 'n',
            #  'o', 'o', 'o', 'o', 'p', 'q', 'r', 'r', 's', 't', 'u', 'u','v', 'w', 'x', 'y', 'z']

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers) #[1.6, 2.3, 3.1, 4.5, 8.7, 9.2]

#What is the difference between sort and sorted?
numbers.sort()
print(numbers) #[1.6, 2.3, 3.1, 4.5, 8.7, 9.2]

#line 8 we made a new variable passed it 'sorted' (new list that is sorted)
#line 12 did not have a new variable declared, we just simply sort the list



#how to compare items
missin_letter = sorted("The quick brown fox jumped over the lazy dog",
                       key=str.casefold)
print(missin_letter) #it moves the T where it needs go be towards the end

names = ["Graham", "John", "terry", "eric", "Terry", "michael"]
names.sort()
print(names) #['Graham', 'John', 'Terry', 'eric', 'michael', 'terry']

names.sort(key=str.casefold)
print(names) #['eric', 'Graham', 'John', 'michael', 'Terry', 'terry']