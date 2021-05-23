import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        try:
            if self.__color[0] != 'red':
                raise Exception(f'порядок цвета нарушился, должен быть красный, а у нас {self.__color[0]}')
            print('Горит красный 7 сек')
            time.sleep(7)

            if self.__color[1] != 'yellow':
                raise Exception(f'порядок цвета нарушился, должен быть желтый, а у нас {self.__color[1]}')
            print('Горит желтый 2 сек')
            time.sleep(2)

            if self.__color[2] != 'green':
                raise Exception(f'порядок цвета нарушился, должен быть зеленый, а у нас {self.__color[2]}')
            print('Горит зеленый 10 сек')
            time.sleep(6)
        except Exception as e:
            print(e)


traffic_light = TrafficLight()
traffic_light.running()
