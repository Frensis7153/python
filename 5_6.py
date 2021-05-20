temp_mass = []  # для сепарации букв и чисел
final_dictionary = dict()  # финальный словарь
with open('syllabus.txt', 'r', encoding='utf-8') as f:
    subject = f.readlines()
    for el in subject:
        one_subject = el.split(':')  # разделяем по двоеточию
        for i in range(len(one_subject[1])):
            if one_subject[1][i].isdigit():  # ищем цыфры, чтобы потом их объединить
                temp_mass.append(one_subject[1][i])
            elif one_subject[1][i - 1].isdigit() and not one_subject[1][i].isdigit():
                temp_mass.append('-')
        temp_mass_2 = ((''.join(temp_mass)).split('-'))  # делаем массив из чисел
        temp_mass_2.pop(len(temp_mass_2) - 1)  # в конце будет мешать символ '-' его надо удалить
        temp_mass_2 = list(map(int, temp_mass_2))  # конечный список чисел для каждого предмета
        final_dictionary[one_subject[0]] = sum(temp_mass_2)
        temp_mass = []

print(final_dictionary)
