import numpy as np


class Matrix:
    row = 0
    col = 0
    A = 0
    b = 0
    c = 0
    matrix = 0
    tableau = 0
    aux = 0

    def __init__(self, m, row, col):
        self.row = row
        self.col = col
        self.A = np.matrix(m[1:, 0:-1])
        self.b = np.matrix(m[:, -1])
        self.c = np.matrix(m[0, 0:-1])
        print(self.c)
