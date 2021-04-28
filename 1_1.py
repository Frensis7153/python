a = input("Введите какую-либо строку ")
print(a)

b = float(input("Введите число с плавующей точкой "))
print(f"{b:.6f}")

a = list(input("Введите список "))
print(a)
c = dict()

k = input("Введите ключ ")
c[k] = input("Введите строковое значение ключа ")
print(c)

a, b, c = list(map(float, input("Введите через пробел три числа формата float ").split()))
# Ввывод в различных форматах
print("%.2f, %f, %f" % (a, b, c))
print(f"{a:.5f} {b} {c}")
print("{1:.3f} {0} {2}".format(a, b, c))
