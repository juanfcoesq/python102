import random
contries = ['col', 'mex', 'bol', 'pe']

population_v2 = {country: random.randint(1,10000000) for country in contries} # fill population dict with random numbers in each country
print(population_v2)

result = {country: population for (country,population) in population_v2.items() if population > 5000000} # filter result with population > 5000000
print(result)

text = 'Hola, soy Juan'
print(text)
unique = {c:c.upper() for c in text if c in 'aeiou'} # filter unique with a,e,i,o,u
print(unique)