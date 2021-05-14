from random import randrange

my_list = [randrange(-50, 51) for el in range(randrange(15))]  # формируем список из рандомных значений
print(f'{my_list}\n{ [my_list[i] for i in range(1, len(my_list)) if my_list[i - 1] < my_list[i]]}')
