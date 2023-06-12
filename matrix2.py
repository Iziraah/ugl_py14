# Создайте класс Матрица. Добавьте методы для:
#   * вывода на печать,
#   * сравнения,
#   * сложения,
#   * *умножения матриц

class Matrix:

    def __init__(self, a_matrix: list[list[int, float]]) -> None:
        if not self.check(a_matrix):
            raise ValueError("Matrix of wrong dimensions")
        self._rows = len(a_matrix)
        self._cols = len(a_matrix[0])
        self._matrix = a_matrix

    @staticmethod
    def check(a_matrix):
        for row in a_matrix:
            if len(row) != len(a_matrix[0]):
                return False
        return True

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Not a matrix type!")
        if self._rows != other._rows or self._cols != other._cols:
            raise ValueError("Matrices are to be equal dimensions")
        new_matrix = [[0] * self._cols for _ in range(self._rows)]
        for i in range(self._rows):
            for j in range(self._cols):
                new_matrix[i][j] = self._matrix[i][j] + other._matrix[i][j]
        return Matrix(new_matrix)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        if self._rows != other._rows or self._cols != other._cols:
            return False
        for i in range(self._rows):
            for j in range(self._cols):
                if self._matrix[i][j] != other._matrix[i][j]:
                    return False
        return True

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return self.__rmul__(other)
        if isinstance(other, (int, float)):
            new_matrix = [[0] * self._cols for _ in range(self._rows)]
            for i in range(self._rows):
                for j in range(self._cols):
                    new_matrix[i][j] = self._matrix[i][j] * other
            return Matrix(new_matrix)
        else:
            raise TypeError("Unsupported type of operand")

    def __rmul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Not a matrix type!")
        if self._cols != other._rows:
            raise ValueError("Matrices rows amt is to be equal other matrix cols amt")
        new_matrix = [[0] * other._rows for _ in range(self._rows)]
        for i in range(self._rows):
            for j in range(other._rows):
                new_matrix[i][j] = self._matrix[i][j] * other._matrix[j][i]
        return Matrix(new_matrix)

    def __str__(self):
        return '\n'.join(''.join([f'{x:^5}' for x in row]) for row in self._matrix) + '\n'

    def __repr__(self):
        """String object representation method"""
        return f'Matrix({self._matrix})'

if __name__ == '__main__':

    mtx_a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    mtx_b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    print(mtx_a + mtx_b)

    print(f'{mtx_a == mtx_b=}\n')
    mtx_c = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    mtx_d = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

    print(mtx_c * mtx_d)
    print(mtx_d * mtx_c)

    try:
        print(mtx_d * mtx_d)
    except (TypeError, ValueError) as exc:
        print(f'\033[31m{exc.__class__.__name__}: {exc}\033[0m')

    print(f'{mtx_a * 10=}')



