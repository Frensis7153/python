from copy import deepcopy


class Matrix:
    def __init__(self, list_of_list: list):
        self.list_of_lists = deepcopy(list_of_list)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.list_of_lists)

    def __getitem__(self, ind):
        return self.list_of_lists[ind]

    def __add__(self, other):
        # other = Matrix(other)
        res = []
        numb = []
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[i])):
                summ = other[i][j] + self.list_of_lists[i][j]
                numb.append(summ)
                if len(numb) == len(self.list_of_lists[i]):
                    res.append(numb)
                    numb = []
        return Matrix(res)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix_2 = Matrix([[4, 5, 6], [7, 8, 9]])
print(f'{matrix_1}\n\n{matrix_2}\n')

print(matrix_1 + matrix_2)
