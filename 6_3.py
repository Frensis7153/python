class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, income: dict):
        super().__init__(name, surname, position, income)
        self.__income = income

    def get_full_name(self):
        print(f'Ф.И.О - {self.surname} {self.name}\nдолжность - {self.position}')

    def get_total_income(self):
        print(f"Доход с учетом премии: {self.__income.get('wage') + self.__income.get('bonus')}")


worker = Position('Роман', 'Некрасов', 'Бухгалтер', {'wage': 200, 'bonus': 50})
print('проверка значений методов', '-'*50)
worker.get_full_name()
worker.get_total_income()
print('проверка значений атрибутов', '-'*50)
print(f'position - {worker.position}')
print(f'name - {worker.name}')
print(f'surname - {worker.surname}')
print(worker.__dict__)
