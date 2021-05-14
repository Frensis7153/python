from math import factorial


def fact(val):
    num = 1
    while num <= val:
        yield num
        num += 1


while True:
    try:
        n = int(input('Введите целое число больше 0: '))
        if n <= 0:
            raise Exception('Введите то, что просят.')
        break
    except Exception as e:
        print(e)

for el in fact(n):
    print(f'{el}-{factorial(el)}')
