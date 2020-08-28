even = [2, 4, 5, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print(even) #[2, 4, 5, 8, 1, 3, 5, 7, 9] but note they are not in order

even.sort()
print(even) #[1, 2, 3, 4, 5, 5, 7, 8, 9]

even.sort(reverse=True)
print(even) #[9, 8, 7, 5, 5, 4, 3, 2, 1]

print()

another_even = even
print(another_even) #[9, 8, 7, 5, 5, 4, 3, 2, 1] makes it 2x
