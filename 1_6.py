a = int(input("a = "))
b = int(input("b = "))
i = 1

while a < b:
    i += 1
    a += a / 10
print(f"На {i}-й день спортсмен достиг результата - не менее {b} км")
