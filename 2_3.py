while True:
    number_of_month = int(input("Введите номер месяца от 1 до 12: "))
    if 1 <= number_of_month <= 12:
        break

months_dict = dict(январь=1, февраль=2, март=3, апрель=4, май=5, июнь=6, июль=7, август=8, сентябрь=9,
                   октябрь=10, ноябрь=11, декабрь=12)
months_list = list(months_dict.keys())
season = ['зима', 'весна', 'лето', 'осень']
# оформим вывод через список months_list
if number_of_month == 12 or number_of_month == 1 or number_of_month == 2:
    print(f'{months_list[number_of_month - 1]} относися к времени года {season[0]}')
elif 3 <= number_of_month <= 5:
    print(f'{months_list[number_of_month - 1]} относися к времени года {season[1]}')
elif 6 <= number_of_month <= 8:
    print(f'{months_list[number_of_month - 1]} относися к времени года {season[2]}')
elif 9 <= number_of_month <= 11:
    print(f'{months_list[number_of_month - 1]} относися к времени года {season[3]}')

# оформим вывод через словарь months_dict
for name_of_months, number_of_months in months_dict.items():
    if number_of_months == number_of_month:
        if number_of_month == 12 or number_of_month == 1 or number_of_month == 2:
            print(f'{name_of_months} относися к времени года {season[0]}')
        elif 3 <= number_of_month <= 5:
            print(f'{name_of_months} относися к времени года {season[1]}')
        elif 6 <= number_of_month <= 8:
            print(f'{name_of_months} относися к времени года {season[2]}')
        elif 9 <= number_of_month <= 11:
            print(f'{name_of_months} относися к времени года {season[3]}')
        break  # чтобы дальше не проводить итерации для экономии операций вычисления в программе

