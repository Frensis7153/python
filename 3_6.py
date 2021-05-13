def int_func(text):
    """Принимает слово нижнем регистре и возвращает его же, где первая буква - заглавная"""
    return text.capitalize()


while True:
    try:
        word = input('Введите слово: ').split()
        if len(word) > 1:
            raise Exception('Вы ввели больше 1 слова, произведите ввод повторно.')
        if not word[0].isalpha():
            raise Exception('В слове должны быть только буквы, произведите ввод повторно.')
        break
    except Exception as e:
        print(e)
print(int_func(word[0]))
