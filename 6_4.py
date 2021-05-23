class Car:
    def __init__(self, speed: float, color: str, name: str, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn_direction(self, turn: str):
        print(f'Машина повернула на {turn}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')


class TownCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превышение скорости, ваша скорость {self.speed}')
        else:
            print(f'Ваша скорость {self.speed}')


class SportCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости, ваша скорость {self.speed}')
        else:
            print(f'Ваша скорость {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed: float, color: str, name: str, is_police=True):
        super().__init__(speed, color, name, is_police)


work_car = WorkCar(50, 'red', 'zz')
work_car.show_speed()
work_car.go()
work_car.turn_direction('право')
print(f'Полицейская ли машина: {work_car.is_police}')
police_car = PoliceCar(70, 'black', 'Ck')
print(f'Полицейская ли машина: {police_car.is_police}')
