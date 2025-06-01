set_countries = {"China", "India", "USA", "Indonesia", "China"} # if are duplicate values, only one will be stored
print(set_countries) # print variable
print(type(set_countries)) # print type

set_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set_numbers)

set_types = {"string", 100, 10.5, False} # it can store different data types
print(set_types)

set_from_string = set("Hello World") # convert string to set
print(set_from_string)

set_from_tuples = set(("abc","cbv","as","abc"))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4,]
set_numers = set(numbers) # convert list to set
print(set_numers)
unique_numbers = list(set_numers) # convert set to list
print(unique_numbers)
