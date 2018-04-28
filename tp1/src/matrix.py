import numpy as np


class Matrix:
    row = 0
    col = 0
    A = 0
    b = 0
    c = 0
    matrix = 0
    tableau = 0
    auxiliary = 0

    def __init__(self, m, row, col):
        self.row = row
        self.col = col

        self.A = np.matrix(m[1:, 0:-1])
        self.b = np.matrix(m[:, -1])
        self.c = np.matrix(m[0, 0:-1])

    def fpi(self):
        zeros = np.zeros((1, self.row))
        identity = np.matrix(np.identity(self.row))
        c1 = np.concatenate((self.c, zeros), axis=1)
        a1 = np.concatenate((self.A, identity), axis=1)
        a2 = np.concatenate((c1, a1), axis=0)
        self.matrix = np.concatenate((a2, self.b), axis=1)

    def tableau(self):
        zeros = np.zeros((1, self.row))
        identity = np.matrix(np.identity(self.row))
        c1 = -1 * self.c
        c2 = np.concatenate((zeros, c1, zeros), axis=1)
        a1 = np.concatenate((identity, self.A, identity), axis=1)
        a2 = np.concatenate((c2, a1), axis=0)
        self.tableau = np.concatenate((a2, self.b), axis=1)

    def auxiliary(self):
        zeros = np.zeros((1, self.row))
        identity = np.matrix(np.identity(self.row))
        c1 = np.ones((1, self.col - 1))
        c2 = np.zeros((1, self.col))
        c3 = np.concatenate((zeros, c2, c1), axis=1)
        a1 = np.concatenate((identity, self.A, identity), axis=1)
        a2 = np.concatenate((c3, a1), axis=0)
        self.auxiliary = np.concatenate((a2, self.b), axis=1)
