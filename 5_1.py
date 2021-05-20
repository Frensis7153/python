with open('data.txt', 'w', encoding='utf-8') as f:
    while True:
        text = input('Введите строку: ')
        if text != '':
            f.write(text)
            f.write('\n')
        else:
            break
