﻿def increment(x):
    return x + 1

increment_v2 = lambda x: x + 1 #Lamnda function is a def function reduced

result = increment(10)
print(result)

result = increment_v2(20)
print(result)

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'

text = full_name('juan', 'perez')
print(text)