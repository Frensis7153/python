def my_func_1(x, y):
    """
    Возвращает возведение вещественного числа в степень целого отрицательного числа

    (number, number) -> number

     >>> my_func(2, -2)
     0.25
    """
    return x ** y


def my_func_2(x, y):
    """
    Возвращает возведение вещественного числа в степень целого отрицательного числа

    (number, number) -> number

     >>> my_func(2, -2)
     0.25
    """

    temp = 1 / x
    for i in range(abs(y) + 1):
        x *= temp
    return x


while True:
    try:
        val_1 = float(input('Введите действительное положительное число: '))
        val_2 = int(input('Введите целое отрицательное число: '))
        if val_1 * val_2 < 0:
            print(f'При помощи оператора ** : {my_func_1(val_1, val_2)}')
            print(f'При помощи цикла: {my_func_2(val_1, val_2)}')
        else:
            print('Введите то, что просят.\n')
            continue
        break
    except Exception as e:
        print(f'Ошибка: {e}')
        print('Введите то, что просят.\n')
