a = int(input("Введите целое положительное число "))
m = a % 10  # берем последнюю цифру от числа а и принимаем его за max
a //= 10  # убираем последнее число для работы с этим остатком
while a:  # если этот остаток не нулевой
    if m < a % 10:  # если наш максимум меньше следующего числа, то заменим максимум
        m = a % 10
    a //= 10
print(m)
