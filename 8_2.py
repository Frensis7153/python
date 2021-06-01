import traceback


class Crash(Exception):
    def __init__(self, txt):
        self.txt = txt


sample = list(map(float, input('Введите числитель и знаменатель через пробел: ').split()))
try:
    if sample[1] == 0:
        raise Crash('ошибка: знаментель не может быть равен нулю')
    else:
        print(f'Результат деления - {sample[0]/sample[1]}')
except Crash as e:
    print(traceback.format_exc())

