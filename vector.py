import numpy as np
import vg

INT_ARR_LIKE_ERR = 'Value should be of int type or array-like'
SIZE_ERR = 'Vector or array-like should be same size'
NUM_TYPE_ERR = 'Value should be of numeric type'


class Vector():
    def __init__(self, coordinates):
        self.vector = np.array(coordinates, dtype=float)

    def __repr__(self):
        return ', '.join([str(i) for i in self.vector])

    def __str__(self):
        return ', '.join([str(i) for i in self.vector])

    def __len__(self):
        return len(self.vector)

    def __neg__(self):
        return -self.vector

    def __pos__(self):
        return +self.vector

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.vector + other
        elif isinstance(other, Vector):
            if len(self.vector) == len(other.vector):
                return self.vector + other.vector
            else:
                raise ValueError(SIZE_ERR)
        elif isinstance(other, (list, tuple)):
            if len(self.vector) == len(other):
                return self.vector + other
            else:
                raise ValueError(SIZE_ERR)
        else:
            raise ValueError(INT_ARR_LIKE_ERR)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self.vector - other
        elif isinstance(other, Vector):
            if len(self.vector) == len(other.vector):
                return self.vector - other.vector
            else:
                raise ValueError(SIZE_ERR)
        elif isinstance(other, (list, tuple)):
            if len(self.vector) == len(other):
                return self.vector - other
            else:
                raise ValueError(SIZE_ERR)
        else:
            raise ValueError(INT_ARR_LIKE_ERR)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.vector * other
        else:
            raise ValueError(NUM_TYPE_ERR)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.vector / other
        else:
            raise ValueError(NUM_TYPE_ERR)

    def __pow__(self, p):
        if isinstance(p, (int, float)):
            return self.vector ** p
        else:
            raise ValueError(NUM_TYPE_ERR)

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def module(self):
        return np.linalg.norm(self.vector)

    def is_collinear(self, other):
        if isinstance(other, Vector):
            return vg.almost_collinear(self.vector, other.vector)
        elif isinstance(other, (list, tuple)):
            if len(self.vector) == len(other):
                return vg.almost_collinear(self.vector, other)
            else:
                raise ValueError(SIZE_ERR)
        else:
            raise ValueError(INT_ARR_LIKE_ERR)

    def distance(self, other):
        if isinstance(other, Vector):
            return np.linalg.norm(self.vector - other.vector)
        elif isinstance(other, (list, tuple)):
            if len(self.vector) == len(other):
                return np.linalg.norm(self.vector - other)
            else:
                raise ValueError(SIZE_ERR)
        else:
            raise ValueError(INT_ARR_LIKE_ERR)

    def scalar_mult(self, other):
        if isinstance(other, Vector):
            return np.dot(self.vector, other.vector)
        elif isinstance(other, (list, tuple)):
            if len(self.vector) == len(other):
                return np.dot(self.vector, other)
            else:
                raise ValueError(SIZE_ERR)
        else:
            raise ValueError(INT_ARR_LIKE_ERR)

    def vector_mult(self, other):
        if isinstance(other, Vector):
            return np.cross(self.vector, other.vector)
        elif isinstance(other, (list, tuple)):
            if len(self.vector) == len(other):
                return np.cross(self.vector, other)
            else:
                raise ValueError(SIZE_ERR)
        else:
            raise ValueError(INT_ARR_LIKE_ERR)
