def find_volume(lenght=1, width=1, depth=1):
    return lenght * width * depth, width, 'hola'

result = find_volume(10, 20, 30)
print(result)

result, width, text = find_volume(width=10)
print(result)
print(width)
print(text)
