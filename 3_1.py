def division_of_numbers(val_1, val_2):
    """Возвращает частное от деления

    (number, number) -> number

    #>>> division_of_numbers(10, 5)
    2
    """
    try:
        res = val_1 / val_2
        return res
    except Exception as e:
        return e


numerator = float(input('числитель: '))
denominator = float(input('знаменатель: '))
print(division_of_numbers(numerator, denominator))
