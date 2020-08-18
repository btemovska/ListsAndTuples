result = True
another_result = result
print(id(result))         #140715174582096
print(id(another_result)) #140715174582096
print()
result = False
print(id(result))         #140715174582128
print(id(another_result)) #140715174582096
print()

result_2 = "Correct"
another_result_2 = result_2
print(id(result_2))          #1821481599792
print(id(another_result_2))  #1821481599792

result_2 += "ish"
print(id(result_2))         #1821481600240
print(id(another_result_2)) #1821481599792
