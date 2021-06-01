class Crash(Exception):
    def __init__(self, txt='dfds'):
        self.txt = txt

    def is_number(self, word):
        try:
            float(word)
            return True
        except ValueError:
            return False


mass_of_number = []
count = 0
while True:
    word = input('Введите число или слово stop: ')
    if word == 'stop':
        print(mass_of_number)
        break
    elif Crash().is_number(word):
        mass_of_number.append(word)
    else:
        print('вы ввели не число')
