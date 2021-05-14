from itertools import count, cycle

while True:
    try:
        generator_list = list(map(int, input('с какого по какое число начинать генерацию: ').split()))
        if len(generator_list) != 2:
            raise Exception('Введите то, что просят')
        for el in count(generator_list[0]):
            if el > generator_list[1]:
                break
            else:
                print(el, end=' ')
        print()
        break
    except Exception as e:
        print('Ошибка:', e)

my_list = ['a', True, 4]
while True:
    try:
        finish = int(input('Сколько нужно повторений: '))
        if finish < 0:
            raise Exception('Число повторений не может быть меньше 0')
        break
    except Exception as e:
        print('Ошибка:', e)
counter = 0
for el in cycle(my_list):
    if counter > len(my_list) * finish - 1:
        break
    else:
        print(el, end=' ')
        counter += 1
