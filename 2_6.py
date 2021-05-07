products = []
product_number = 1
while True:
    print("Введите данные продукта")
    name_product = input("Название: ")
    product_price = int(input("Цена: "))
    number_of_product = int(input("Количество: "))
    unit = input("Единица измерения: ")
    counter = int(input("Если больше нет продуктов для ввода, наберите цифру 0 "))
    products.append((product_number, dict(название=name_product, цена=product_price, количесвто=number_of_product,
                                          ед=unit)))
    product_number += 1
    if counter == 0:
        break

product_keys = list(products[0][1].keys())  # создаем список из ключей
product_analytics_dict = {}
for el in product_keys:  # будем заходить в каждый словарик списка продуктов и вычленять от туда ключи
    product_analytics_dict[el] = []  # для каждого ключа списка создадим пустой массив
for el in products:
    for inner_el in el[1]:
        product_analytics_dict[inner_el].append(el[1].get(inner_el))  # заполняем для каждого ключа массив

product_analytics_dict['ед'] = list(set(product_analytics_dict['ед']))  # чтобы ед. измерения были без повторений

print('[', end='')
for i in range(len(products)):
    if i == len(products) - 1:
        print(f'{products[i]}]')
    else:
        print(products[i])

print(product_analytics_dict)
