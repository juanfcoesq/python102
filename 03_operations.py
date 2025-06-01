set_a = {'col','mex','bol'}
set_b = {'bol','pe'}

set_c = set_a.union(set_b) # union of two sets with metod
print(set_c)
print(set_a | set_b) # union of two sets with operator

set_c = set_a.intersection(set_b) # intersection of two sets with metod
print(set_c)
print(set_a & set_b) # intersection of two sets with operator

set_c = set_a.difference(set_b) # difference of two sets with metod
print(set_c)
print(set_a - set_b) # difference of two sets with operator
print(set_b - set_a)

set_c = set_a.symmetric_difference(set_b) # symmetric difference of two sets with metod
set_d = set_a ^ set_b
print(set_c)
print(set_d)
print(set_a ^ set_b) # symmetric difference of two sets with operator


