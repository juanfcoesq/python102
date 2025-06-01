def increment(x):
    return x+1

increment_v2 = lambda x: x + 1

def high_ors_func(x, func):
    return x + func(x)

high_ors_func_v2 = lambda x, func: x + func(x)

result = high_ors_func(2, increment)
# 2 + (2 + 1)
print(result)

result = high_ors_func_v2(2, increment_v2)
# 2 + (2 + 1)
print(result)
result = high_ors_func_v2(2, lambda x: x + 2)
print(result)
# Change in lambda function
result = high_ors_func_v2(2, lambda x: x * 5)
print(result)