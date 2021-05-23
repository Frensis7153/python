class Stationery:
    def __init__(self):
        pass

    def title(self, name):
        self.name = name

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        super().__init__()

    def draw(self):
        print('Отрисовка Pen')


class Pencil(Stationery):
    def __init__(self):
        super().__init__()

    def draw(self):
        print('Отрисовка Pencil')


class Handle(Stationery):
    def __init__(self):
        super().__init__()

    def draw(self):
        print('Отрисовка Handle')


appliance = Stationery()
appliance_1 = Pen()
appliance_2 = Pencil()
appliance_3 = Handle()

appliance.draw()
appliance_1.draw()
appliance_2.draw()
appliance_3.draw()

appliance_2.title('pencil')
print(appliance_2.name)
