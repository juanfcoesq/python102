'''
numbers = []
for element in range(1,11): # fill the list duplicated
    numbers.append(element * 2)
print(numbers)

numbers_v2 = [element * 2 for element in range(1,11)] # fill the list duplicated
print(numbers_v2)
'''
numbers = []
for i in range(1,11): # add condition (just pair numbers)
    if i % 2 == 0:
        numbers.append(i * 2)
print(numbers)

numbers_v2 = [i * 2 for i in range(1,11) if i % 2 == 0] # add condition (just pair numbers)
print(numbers_v2)