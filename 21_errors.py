print('Hola')

suma = lambda x,y: x + y
assert suma(2,2) == 4

print('Hola 2')

x = 10
if x < 18:
    raise Exception('No se permiten menores de edad')