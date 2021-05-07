# В данной задаче я применли вставку элемента через insert, так как я не знаю точно какой
# будет элемент по счету (то есть, если число маркировать), если его просто сначала
# включить в список, а потом отсортировать однако в задаче требудется чтобы
# элемент шел именно после ему идентичных.
my_list = list(map(int, input("Введите список: ").split()))
my_list.sort(reverse=True)
print(my_list)
el = int(input('Введите элемент рейтинга: '))
if my_list.count(el):  # вставляем элемент после ему индентичных
    my_list.insert(my_list.index(el) + my_list.count(el), el)
else:
    my_list.append(el)
    my_list.sort(reverse=True)
print(my_list)
