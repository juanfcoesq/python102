dict = {}
for i in range(1,11): # fill the dict with key value pairs
    dict[i] = i*2
print(dict)

dict_v2 = {i:i*2 for i in range(1,11)} # fill the dict with key value pairs
print(dict_v2)

import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1,10000000) # fill population dict with random numbers in each country
print(population)

population_v2 = {country: random.randint(1,10000000) for country in countries} # fill population dict with random numbers in each country
print(population_v2)

names = ['John', 'Jane', 'Jeremy', 'Jessica']
ages = [12, 56,  98, 43]

print(list(zip(names, ages)))

new_dict = {name:age for (name,age) in zip(names, ages)}
print(new_dict)