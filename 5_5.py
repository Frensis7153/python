with open('numberss.txt', 'w+', encoding='utf-8') as f:
    f.write('12 2 3 4.2 4')
    f.seek(0)
    numbers = f.read()
print(numbers, type(numbers))
mass_numbers = list(map(float, numbers.split()))
print(sum(mass_numbers))
