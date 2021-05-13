set_of_numbers = list()
total_amount = 0
count = 0  # счетчик для отслеживания спец-символа 'Q'
while True:
    try:
        set_of_numbers_str = input('Введите строку чисел через пробел, спец-символ q: ').split()
        for el in set_of_numbers_str:  # перебираем элементы и смоттрим есть ли там Q
            if el.upper() != 'Q':
                set_of_numbers.append(el)
            else:
                count += 1
        sum_of_numbers = sum(list(map(float, set_of_numbers)))  # преобразуем элементы строки в тип float И суммируем
        total_amount += sum_of_numbers
        print(f'Общая сумма: {total_amount}')
        set_of_numbers.clear()
        if count != 0:  # если мы нашли 'Q', то выходим из программы
            break
    except Exception as e:
        print(f'Ошибка: {e}. Данные некорректны, введите повторно.')
        set_of_numbers.clear()
        count = 0
        sum_of_numbers = 0
