class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}+i*{self.y}'

    def __add__(self, other):
        el_1 = self.x + other.x
        el_2 = self.y + other.y
        return ComplexNumber(el_1, el_2)

    def __mul__(self, other):
        el_1 = self.x * other.x - self.y * other.y
        el_2 = self.x * other.y + self.y * other.x
        return ComplexNumber(el_1, el_2)


a = ComplexNumber(1, 1)
b = ComplexNumber(2, 3)
print(b)
print(a + b)
print(a * b)
