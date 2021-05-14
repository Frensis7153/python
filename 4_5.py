from functools import reduce

print(reduce(lambda x1, x2: x1 * x2, [el for el in range(100, 1001) if el % 2 == 0]))
