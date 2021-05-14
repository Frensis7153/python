from random import randrange

my_list = [randrange(0, 44) for i in range(13)]
print(my_list)
print([el for el in my_list if my_list.count(el) == 1])
