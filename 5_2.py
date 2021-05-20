from re import split, escape

count = 0  # счетчик для подсчета количества строк
delimiter = []
with open('database.txt', 'r', encoding='utf-8') as f:
    file = f.readlines()
    for el in file:  # тут мы проверять на наличие букв в строках, и искать разделители слов
        for not_letter in el:
            if not not_letter.isalpha() and not_letter != '\n':
                delimiter.append(not_letter)
    delimiter = list(set(delimiter))  # уменьшим наш список, через множэество, так у нас будет экономия памяти.
    regexPattern = '|'.join(map(escape, delimiter))  # создадим шаблон разделителей.
    for el in file:
        count += 1
        mass_of_words = split(regexPattern, el)
        if el[0] != "\n":  # проверка на пустоту строки
            print(f'Число слов в {count} строке: {len(mass_of_words)}')
        else:
            print(f'Число слов в {count} строке: {0}')
print(f'Число строк: {count}')
