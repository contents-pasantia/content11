my_list   = [2,2,2,2,2]

all_multiplied = 1

for i in my_list:
    all_multiplied *= i

print(all_multiplied)

# recuce
from functools import reduce

reduced = reduce(lambda x, y: x*y, my_list)
print(reduced)