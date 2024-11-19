class Matrix2D:
    def __init__(self, cells):
        if cells:
            self.__m = len(cells)
            self.__n = len(cells[0])
            self.__cells = cells
        else:
            raise ValueError("Incorrect parameters!")
        for cell in cells:
            if len(cell) != self.__n:
                raise ValueError("Incorrect parameters!")

    @property
    def m(self):
        return self.__m

    @property
    def n(self):
        return self.__n

    @property
    def cells(self):
        return self.__cells

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            nl = []
            for cell in self.__cells:
                ml = []
                for column in cell:
                    ml.append(column * other)
                nl.append(ml)
            return Matrix2D(nl)

    def matrix_product(self, other):
        if isinstance(other, Matrix2D) and self.__n <= other.m:
            new_cells = []
            for i in range(self.__m):
                new_line = []
                for j in range(other.n):
                    current_cell = 0
                    for k in range(self.__n):
                        current_cell += self.cells[i][k] * other.cells[k][j]
                    new_line.append(current_cell)
                new_cells.append(new_line)

            return Matrix2D(new_cells)

    def __str__(self):
        result = ''
        for cell in self.__cells:
            for column in cell:
                result += str(column) + ' '
            result += '\n'
        return result


a = [[1, 1, 0],
     [1, 0, 2]]

b = [[1, 0, 2, 1],
     [2, 1, 2, 0],
     [1, 1, 0, 3]]

matr1 = Matrix2D(a)
matr2 = Matrix2D(b)

print(matr1.matrix_product(matr2))
