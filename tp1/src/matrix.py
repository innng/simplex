from fractions import Fraction
import numpy as np


class Matrix:
    A = 0
    b = 0
    c = 0
    matrix = 0
    tableau = 0

    def init(self, m, row, col):
        aux1 = np.matrix(m, dtype="object")
        aux2 = aux1.reshape((row + 1, col + 1))

        self.A = np.matrix(aux2[1:, 0:-1], dtype="object")
        self.b = np.matrix(aux2[:, -1], dtype="object")
        self.c = np.matrix(aux2[0, 0:-1], dtype="object")

        zeros = np.zeros((1, self.A.shape[0]), dtype="object")
        identity = np.identity(self.A.shape[0], dtype="object")

        c1 = np.concatenate((self.c, zeros), axis=1)
        a1 = np.concatenate((self.A, identity), axis=1)
        a2 = np.concatenate((c1, a1), axis=0)
        self.matrix = np.concatenate((a2, self.b), axis=1)

    def default(self):
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

        multiplier = np.zeros(self.tableau.shape[0], dtype="object")
        multiplier[row] = Fraction(1, self.tableau[row, col])

        for i in range(0, self.tableau.shape[1]):
            self.tableau[row, i] = self.tableau[row, i] * multiplier[row]

        for i in range(0, self.tableau.shape[0]):
            if(i != row):
                multiplier[i] = -1 * Fraction(self.tableau.T[col, i], self.tableau.T[col, row])

        for i in range(0, self.tableau.shape[0]):
            if(i != row):
                for j in range(0, self.tableau.shape[1]):
                    self.tableau[i, j] = self.tableau[i, j] + self.tableau[row, j] * multiplier[i]

    def solution(self):
        print("sol")

    def updateFractions(self):
        for i in range(0, self.tableau.shape[0]):
            for j in range(0, self.tableau.shape[1]):
                self.tableau[i, j] = Fraction(self.tableau[i, j], 1)

    def updateBase(self):
        print("base")
