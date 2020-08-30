panagram = "The qucik brown fox jums over the lazy dog"

words = panagram.split()
print(words) #['The', 'qucik', 'brown', 'fox', 'jums', 'over', 'the', 'lazy', 'dog']

numbers = "9,223, 372, 036, 854, 775, 807"
print(numbers.split(","))
# ['9', '223', ' 372', ' 036', ' 854', ' 775', ' 807']

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


