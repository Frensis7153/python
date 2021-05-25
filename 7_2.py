from abc import ABC, abstractmethod


class AbsForClothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def tissue_consumption(self):
        """подсчет расхода определенного материала по определенным формулам"""
        pass


class Clothes:
    dict_of_costumes = list()  # Список из пар название одежды и расхода материала,

    # чтобы потом узнать общий расход одежды

    def __init__(self, name=''):
        self.name = name

    @property
    def tissue_consumption_all(self):
        tissue = [el[1] for el in Clothes.dict_of_costumes]
        return sum(tissue)


class Coat(Clothes, AbsForClothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
        Coat.dict_of_costumes.append([self.name, self.size / 6.5 + 0.5])

    @property
    def tissue_consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes, AbsForClothes):

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height
        Costume.dict_of_costumes.append([self.name, 2 * self.height + 0.3])

    @property
    def tissue_consumption(self):
        return 2 * self.height + 0.3


a = Costume('r', 3)
b = Costume('g', 1)
c = Coat('s', 4)

print(c.tissue_consumption)
print(Clothes().dict_of_costumes)
print(Clothes().tissue_consumption_all)
