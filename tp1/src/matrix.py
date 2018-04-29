import numpy as np


class Matrix:
    A = ""
    b = ""
    c = ""
    base = ""
    fpi = ""
    tableau = ""
    auxiliary = ""

    def init(self, m, row, col):
        aux1 = np.matrix(m)
        aux2 = aux1.reshape((row + 1, col + 1))

        self.A = np.matrix(aux2[1:, 0:-1])
        self.b = np.matrix(aux2[:, -1])
        self.c = np.matrix(aux2[0, 0:-1])

    def fpi(self):
        zeros = np.zeros((1, self.A.shape[0]))
        identity = np.identity(self.A.shape[0])

        c1 = np.concatenate((self.c, zeros), axis=1)
        a1 = np.concatenate((self.A, identity), axis=1)
        a2 = np.concatenate((c1, a1), axis=0)
        self.fpi = np.concatenate((a2, self.b), axis=1)

    def tableau(self):
        zeros = np.zeros((1, self.A.shape[0]))
        identity = np.identity(self.A.shape[0])

        c1 = -1 * self.c
        c2 = np.concatenate((zeros, c1, zeros), axis=1)
        a1 = np.concatenate((identity, self.A, identity), axis=1)
        a2 = np.concatenate((c2, a1), axis=0)
        self.tableau = np.concatenate((a2, self.b), axis=1)

    def auxiliary(self):
        zeros = np.zeros((1, self.A.shape[0]))
        identity = np.identity(self.A.shape[0])

        c1 = np.ones((1, self.A.shape[0]))
        c2 = np.zeros((1, self.c.shape[1]))
        c3 = np.concatenate((zeros, c2, c1), axis=1)
        a1 = np.concatenate((identity, self.A, identity), axis=1)
        a2 = np.concatenate((c3, a1), axis=0)
        self.auxiliary = np.concatenate((a2, self.b), axis=1)

    def pivot(self, row, col):
        multiplier = 0
        for i in self.tableau.T[col]:
            print(i)

        print("pivot")

    def solution(self):
        print("solution")

    def updateValues(self):
        print("fractions")

    def updateBase(self):
        print("base")
