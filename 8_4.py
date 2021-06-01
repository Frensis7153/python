class OfficeEquipment:  # общий функционал всех классов
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age


class Printer(OfficeEquipment):
    __dict_of_equipment_printer = dict()

    def print_print(self):
        print('Пошла печать')


class Scanner(OfficeEquipment):
    __dict_of_equipment_scanner = dict()

    def print_print(self):
        print('Сканирвание пошло')


class Xerox(OfficeEquipment):
    __dict_of_equipment_xerox = dict()

    def print_print(self):
        print('Ксерокопирование пошло')


b = Xerox()
c = Printer()
a = Scanner()
b.print_print()
