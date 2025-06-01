set_countries = {"China", "India", "USA", "Indonesia", "China"}

size = len(set_countries) # size of the set
print(size)

print("USA" in set_countries) # know if USA is in the set
print("Japan" in set_countries) # know if Japan is in the set

#add
set_countries.add("Japan")
print(set_countries)
set_countries.add("Japan") # doesn't add if already in the set
print(set_countries)

#update
set_countries.update(["Japan", "Korea", "France"]) # add multiple items
print(set_countries)

#remove
set_countries.remove("Japan") # removes the first item that matches
print(set_countries)
set_countries.discard("Japan") # doesn't raise an error if not found'
print(set_countries)
set_countries.pop() # removes the last item
print(set_countries)
set_countries.clear() # removes all items
print(set_countries)
