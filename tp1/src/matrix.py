from fractions import Fraction
import numpy as np


class Matrix:
    A = 0
    b = 0
    c = 0
    tableau = 0
    base = []

    def init(self, matrix, row, col):
        aux1 = np.matrix(matrix, dtype='object')
        aux2 = aux1.reshape(row + 1, col + 1)

        self.A = np.matrix(aux2[1:, 0:-1], dtype='object')
        self.b = np.matrix(aux2[:, -1], dtype='object')
        self.c = np.matrix(aux2[0, 0:-1], dtype='object')

    def tableau(self):
        zeros = np.zeros((1, self.A.shape[0]), dtype='object')
        identity = np.identity(self.A.shape[0], dtype='object')

        c1 = -1 * self.c
        c2 = np.concatenate((zeros, c1, zeros), axis=1)
        a1 = np.concatenate((identity, self.A, identity), axis=1)
        a2 = np.concatenate((c2, a1), axis=0)
        self.tableau = np.concatenate((a2, self.b), axis=1)

        self.updateFractions()

        for i in range(0, self.getGap().shape[0]):
            for j in range(0, self.getGap().shape[1]):
                if(self.getGap()[i, j] == 1):
                    self.base.append((i + 1, self.A.shape[0] + self.c.shape[1] + j))

    def updateFractions(self):
        for i in range(0, self.tableau.shape[0]):
            for j in range(0, self.tableau.shape[1]):
                self.tableau[i, j] = Fraction(self.tableau[i, j], 1)

    def updateBase(self, row, col):
        for i in self.base:
            if(i[0] == row):
                self.base.remove(i)
                break
        self.base.append((row, col))

    def pivoting(self, row, col):
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

        self.updateBase(row, col)

    def extendAuxiliary(self):
        zeros = np.zeros((1, self.getC().shape[1]), dtype='object')
        ones = np.ones((1, self.getGap().shape[1]), dtype='object')
        identity = np.identity(self.A.shape[0], dtype='object')

        c1 = np.concatenate((zeros, ones), axis=1)
        a1 = np.concatenate((self.getA(), identity), axis=1)
        a2 = np.concatenate((c1, a1), axis=0)
        self.tableau = np.concatenate((self.getMem(), a2, self.getB()), axis=1)
        self.updateFractions()

    def destroyAuxiliary(self):
        zeros = np.zeros((1, self.A.shape[0]), dtype='object')

        c1 = -1 * self.c
        c2 = np.concatenate((c1, zeros), axis=1)
        aux1 = np.concatenate((c2, self.getA()[:, :-self.A.shape[0]]), axis=0)
        self.tableau = np.concatenate((self.getMem(), aux1, self.getB()), axis=1)
        self.updateFractions()

    def getA(self):
        return self.tableau[1:, self.A.shape[0]:-1]

    def getB(self):
        return self.tableau[:, -1]

    def getC(self):
        return self.tableau[0, self.A.shape[0]:-1]

    def getMem(self):
        return self.tableau[:, 0:self.A.shape[0]]

    def getGap(self):
        return self.tableau[1:, self.A.shape[0] + self.c.shape[1]:-1]
