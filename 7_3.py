class Cell:
    def __init__(self, quantity_cell: int):
        self.cell = '*' * quantity_cell

    def __add__(self, other):
        return Cell(len(self.cell) + len(other.cell))

    def __sub__(self, other):
        if len(self.cell) > len(other.cell):
            return Cell(len(self.cell) - len(other.cell))
        else:
            return Cell(0)

    def __mul__(self, other):
        return Cell(len(self.cell) * len(other.cell))

    def __truediv__(self, other):
        if len(other.cell) != 0:
            return Cell(len(self.cell) // len(other.cell))
        else:
            return Cell(len(self.cell))

    def make_order(self, number_of_cell_in_a_row: int):
        whole_part = len(self.cell) // number_of_cell_in_a_row
        remainder = len(self.cell) % number_of_cell_in_a_row
        for i in range(whole_part):
            for j in range(number_of_cell_in_a_row):
                print('*', end='')
            print()
        for i in range(remainder):
            print('*', end='')

    def __str__(self):
        return f'{self.cell}'


a = Cell(7)
b = Cell(5)
print(f'клетка 1 - {a}')
print(f'клетка 2 - {b}')
print(f'сумма - {a + b}')
print(f'разность - {a - b}')
print(f'умножение - {a * b}')
print(f'деление - {a / b}')
(a + b).make_order(5)
