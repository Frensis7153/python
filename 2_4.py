words = input("Введите строку: ").split()
for ind, word in enumerate(words, 1):
    print(ind, word[:10])
