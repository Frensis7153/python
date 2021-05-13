def int_func(wrd):
    """Принимает слово нижнем регистре и возвращает его же, где первая буква - заглавная"""
    return wrd.capitalize()


def capitalize_text(text):
    """Принимает текст со словами в нижнем регистре, возвращает тот же текст, где
     каждое слово начинается с заглавной буквы.

     str -> str

     >>>capitalize_text('привет мир')
     'Привет Мир'
     """
    words_real = text.split()
    words_copy = list()
    for elem in words_real:
        words_copy.append(int_func(elem))
    return ' '.join(words_copy)


while True:
    try:
        words = input('Введите текст: ').split()
        for el in words:
            if not el.isalpha():
                raise Exception('В словах должны быть только буквы, произведите ввод повторно.')
        break
    except Exception as e:
        print(e)
        
print(capitalize_text(' '.join(words)))
