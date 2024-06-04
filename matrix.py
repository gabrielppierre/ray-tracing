from vector import Vector
from point import Point

class Matrix:
    def __init__(self, matrix_values : list):
        self.values = matrix_values
        self.m = len(self.values)
        self.n = len(self.values[0])

    def dot_product(self, other):
        if isinstance(other, (Vector)):
            other_matrix = self.to_matrix(other)
            result = self.dot_product_matrix(self, other_matrix)
            return self.matrix_to(result, Vector)
        elif isinstance(other, (Point)):
            other_matrix = self.to_matrix(other)
            result = self.dot_product_matrix(self, other_matrix)
            return self.matrix_to(result, Point)
        elif isinstance(other, Matrix):
            other_matrix = other
            result = self.dot_product_matrix(self, other_matrix)
            return result
        else:
            return None
    
    @staticmethod
    def dot_product_matrix(matrix1, matrix2):
        if matrix2.m == matrix1.n:
            result = []
            for l in range(matrix1.m):
                result.append([])
                for c in range(matrix2.n):
                    position_value = 0
                    for i in range(matrix2.m):
                        position_value += matrix1.values[l][i] * matrix2.values[i][c]
                    result[l].append(position_value)
            return Matrix(result)
        else:
            return None

    @staticmethod
    def to_matrix(thing):
        values = [[thing.x], [thing.y], [thing.z], [1]]
        return Matrix(values)

    @staticmethod
    def matrix_to(matrix, to_type):
        return to_type(matrix.values[0][0], matrix.values[1][0], matrix.values[2][0])

    def __str__(self):
        values_string = ""
        for l in range(self.m):
            values_string += "["
            for c  in range(self.n):
                if c == 0:
                    values_string += f"{self.values[l][c]}"
                else:
                    values_string += f", {self.values[l][c]}"
            values_string += "]\n"
        return values_string

# Teste:
'''
m1 = [[2, 0, 0, 0],
      [0, 2, 0, 0],
      [0, 0, 2, 0],
      [0, 0, 0, 1]]

m2 = [[1, 2],
      [3, 4],
      [5, 6]]


M1 = Matrix(m1)
M2 = Matrix(m2)

print(str(M1.dot_product(Point(1, 2, 2))))


m1 = [[2, 1],
      [1, 2]]

m2 = [[1, 2],
      [3, 4]]

M1 = Matrix(m1)
M2 = Matrix(m2)

print(str(M1.dot_product(M2)))
print(str(M2.dot_product(M1)))
'''