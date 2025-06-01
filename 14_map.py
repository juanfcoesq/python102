numbers = [1, 2, 3, 4, 5]
numbers_v2 = []

for i in numbers:
    numbers_v2.append(i * 2)

numbers_v3 = list(map(lambda x: x * 2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8]

print(numbers_1)
print(numbers_2)
result = map(lambda x, y: x + y, numbers_1, numbers_2) # Suma las dos listas con su respectivo indice y respeta el tamaño de la mas pequeña
print(list(result))
