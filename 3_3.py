def my_func(var_1, var_2, var_3):
    """
    Возвращает сумму наибольших двух из трех чисел.

    (number, number, number) -> number

    >>> my_func(8, 5, 10)
    15
    """
    values = [var_1, var_2, var_3]
    values.sort()
    return values[1] + values[2]


while True:
    try:
        value1, value2, value3 = map(float, input('Введите 3 числа через пробел: ').split())
        print(my_func(value1, value2, value3))
        break
    except Exception as e:
        print(f'Ошибка: {e}')
