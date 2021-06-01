class OfficeEquipment:  # общий функционал всех классов
    __dict_of_equipment = dict()

    def __init__(self, name='', age=0):
        try:
            if type(name) == str and type(age) == int:
                self.name = name
                self.age = age
            else:
                raise Exception('Неверные данные')
        except Exception as e:
            print(e)

    def add_to_stok(self, kwargs: dict):
        """просто склад"""
        self.__dict_of_equipment.update(kwargs)

    @staticmethod
    def show_stok():
        for el_1, el_2 in OfficeEquipment.__dict_of_equipment.items():
            print(f'{el_1} - {el_2}')


class Printer(OfficeEquipment):
    __dict_of_equipment_printer = dict()

    def print_print(self):
        print('Пошла печать')

    def add_to_stok_printer(self, kwargs: dict):
        """склад принтеров"""
        try:
            if len(*kwargs.values()) == 2 and type(list(*kwargs.values())[0]) == str and type(
                    list(*kwargs.values())[1]) == int:
                if list(kwargs.keys())[0] == 'printer':
                    self.__dict_of_equipment_printer.update(kwargs)
                    self.add_to_stok(kwargs)
                else:
                    raise Exception('Такого принтера нет')
            else:
                raise Exception('Неверно введенные данные')
        except Exception as e:
            print(e)

    @staticmethod
    def show_stok_printer():
        print('Printer:')
        for el_1, el_2 in Printer.__dict_of_equipment_printer.items():
            print(f'{el_1} - {el_2}', end=' ')
        print()


class Scanner(OfficeEquipment):
    __dict_of_equipment_scanner = dict()

    def print_print(self):
        print('Сканирвание пошло')

    def add_to_stok_scanner(self, kwargs: dict):
        """склад сканеров"""
        try:
            if len(*kwargs.values()) == 2 and type(list(*kwargs.values())[0]) == str and type(
                    list(*kwargs.values())[1]) == int:
                if list(kwargs.keys())[0] == 'scanner':
                    self.__dict_of_equipment_scanner.update(kwargs)
                    self.add_to_stok(kwargs)
                else:
                    raise Exception('Такого сканера нет')
            else:
                raise Exception('Неверно введенно данные')
        except Exception as e:
            print(e)

    @staticmethod
    def show_stok_scanner():
        print('Scanner:')
        for el_1, el_2 in Scanner.__dict_of_equipment_scanner.items():
            print(f'{el_1} - {el_2}', end=' ')
        print()


class Xerox(OfficeEquipment):
    __dict_of_equipment_xerox = dict()

    def print_print(self):
        print('Ксерокопирование пошло')

    def add_to_stok_xerox(self, kwargs):
        """склад ксероксов"""
        try:
            if len(*kwargs.values()) == 2 and type(list(*kwargs.values())[0]) == str and type(
                    list(*kwargs.values())[1]) == int:
                if list(kwargs.keys())[0] == 'xerox':
                    self.__dict_of_equipment_xerox.update(kwargs)
                    self.add_to_stok(kwargs)
                else:
                    raise Exception('Такого ксерокса нет')
            else:
                raise Exception('Неверно введенные данные')
        except Exception as e:
            print(e)

    @staticmethod
    def show_stok_xerox():
        print('Xerox:')
        for el_1, el_2 in Xerox.__dict_of_equipment_xerox.items():
            print(f'{el_1} - {el_2}', end=' ')
        print()


b = Xerox('df', 4)
c = Printer()
a = Scanner()
c.add_to_stok_printer({'printer': ['name', 4]})
b.add_to_stok_xerox({'xerox':['ndsf', 6]})
a.add_to_stok_scanner({'scanner': ['sdasdsame', 4]})
b.show_stok()
