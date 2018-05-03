import numpy as np
from fractions import Fraction


class Matrix:
    A = 0
    b = 0
    c = 0
    tableau = 0
    base = []
    parts = {'A': 0, 'b': 0, 'c': 0, 'mem': 0, 'gap': 0}

    def init(self, m, r, c):
        aux1 = np.matrix(m, dtype="object")
        aux2 = aux1.reshape(r + 1, c + 1)

        self.A = np.matrix(aux2[1:, 0:-1], dtype="object")
        self.b = np.matrix(aux2[:, -1], dtype="object")
        self.c = np.matrix(aux2[0, 0:-1], dtype="object")

    def tableau(self):
        zeros = np.zeros((1, self.A.shape[0]), dtype="object")
        identity = np.identity(self.A.shape[0], dtype="object")

        c1 = -1 * self.c
        c2 = np.concatenate((zeros, c1, zeros), axis=1)
        a1 = np.concatenate((identity, self.A, identity), axis=1)
        a2 = np.concatenate((c2, a1), axis=0)
        self.tableau = np.concatenate((a2, self.b), axis=1)

    def auxiliary(self):
        zeros = np.zeros((1, self.A.shape[0]), dtype="object")
        identity = np.identity(self.A.shape[0], dtype="object")

        c1 = np.ones((1, self.A.shape[0]), dtype="object")
        c2 = np.zeros((1, self.c.shape[1]), dtype="object")
        c3 = np.concatenate((zeros, c2, c1), axis=1)
        a1 = np.concatenate((identity, self.A, identity), axis=1)
        a2 = np.concatenate((c3, a1), axis=0)
        self.tableau = np.concatenate((a2, self.b), axis=1)

    def pivot(self, row, col):
        if(row > self.tableau.shape[0] or col > self.tableau.shape[1]):
            print("Invalid position in tableau!")
            return

        multiplier = Fraction(1, self.tableau[row, col])

        for i in range(0, self.tableau.shape[1]):
            self.tableau[row, i] = self.tableau[row, i] * multiplier

        for i in range(0, self.tableau.shape[0]):
            if(i != row):
                multiplier = -1 * Fraction(self.tableau.T[col, i], self.tableau.T[col, row])

                for j in range(0, self.tableau.shape[1]):
                    self.tableau[i, j] = self.tableau[i, j] + self.tableau[row, j] * multiplier

    def updateFractions(self):
        for i in range(0, self.tableau.shape[0]):
            for j in range(0, self.tableau.shape[1]):
                self.tableau[i, j] = Fraction(self.tableau[i, j], 1)

    def divide(self):
        self.parts['A'] = self.tableau[1:, self.A.shape[0]: 2 * self.A.shape[0] + 1]
        self.parts['b'] = self.tableau[:, -1]
        self.parts['c'] = self.tableau[0, self.A.shape[0]: 2 * self.A.shape[0] + 1]
        self.parts['mem'] = self.tableau[:, 0:self.A.shape[0]]
        self.parts['gap'] = self.tableau[:, self.parts['mem'].shape[1] + self.parts['c'].shape[1]: -1]

    def updateBase(self):
        print("oi")
