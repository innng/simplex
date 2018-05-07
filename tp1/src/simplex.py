from utils import printConclusao
from utils import printPivoting
from fractions import Fraction
from matrix import Matrix
import numpy as np

NONVIABLE = 0
UNBOUNDED = 1
LIMITED = 2


class Simplex:
    matrix = Matrix()
    auxiliary = False

    def init(self, m, r, c):
        self.matrix.init(m, r, c)
        self.matrix.tableau()
        self.selection()

    def selection(self):
        c = True
        b = True

        for i in range(0, self.matrix.getC().shape[1]):
            if(self.matrix.getC()[0, i] < 0):
                c = False
                break

        for i in range(1, self.matrix.getB().shape[0]):
            if(self.matrix.getB()[i, 0] < 0):
                b = False
                break

        if(c is True and b is False):
            (index, valid) = self.testNonViable()
            if(valid is True):
                self.dual()
            else:
                self.nonViable(index)
        elif(c is False and b is True):
            (index, valid) = self.testUnbounded()
            if(valid is True):
                self.primal()
            else:
                self.unbounded(index)
        elif(c is False and b is False):
            self.auxiliary = True
            self.adjustMatrix()
        elif(c is True and b is True):
            self.end()

    def testNonViable(self):
        index = -1
        for i in range(1, self.matrix.getB().shape[0]):
            valid = False
            if(self.matrix.getB()[i, 0] < 0):
                index = i
                for j in range(0, self.matrix.getA().shape[1]):
                    if(self.matrix.getA()[i - 1, j] < 0):
                        valid = True
                        break
                if(valid is False):
                    return (index, False)
        return (-1, True)

    def testUnbounded(self):
        for i in range(0, self.matrix.getC().shape[1]):
            valid = False
            if(self.matrix.getC()[0, i] < 0):
                index = i
                for j in range(0, self.matrix.getA().shape[0]):
                    if(self.matrix.getA()[j, i] > 0):
                        valid = True
                        break
                if(valid is False):
                    return (index, False)
        return (-1, True)

    def nonViable(self, rIndex=None):
        if(self.auxiliary is True):
            printConclusao(NONVIABLE, self.matrix.getMem()[0])
        else:
            printConclusao(NONVIABLE, self.matrix.getMem()[rIndex])

    def unbounded(self, cIndex=None):
        certificate = np.zeros((1, self.matrix.c.shape[1]), dtype='object')
        certificate[0, cIndex] = 1

        print(certificate)

    def end(self):
        if(self.auxiliary is True):
            self.evalAuxiliary()
        else:
            solution = self.getSolution()
            printConclusao(LIMITED, self.matrix.getMem()[0], self.matrix.getB()[0, 0], solution)

    def primalPivot(self):
        rIndex = -1
        cIndex = -1

        for i in range(0, self.matrix.getC().shape[1]):
            if(self.matrix.getC()[0, i] < 0):
                cIndex = i
                break

        ratio = float('inf')
        for i in range(0, self.matrix.getA().shape[0]):
            if(self.matrix.getA()[i, cIndex] > 0):
                aux = Fraction(self.matrix.getB()[i + 1, 0], self.matrix.getA()[i, cIndex])
                if(aux < ratio):
                    ratio = aux
                    rIndex = i

        return (self.matrix.getC().shape[0] + rIndex, self.matrix.getMem().shape[1] + cIndex)

    def primal(self):
        (row, col) = self.primalPivot()
        self.matrix.pivoting(row, col)
        printPivoting(self.matrix.tableau)
        self.selection()

    def dualPivot(self):
        rIndex = -1
        cIndex = -1

        for i in range(1, self.matrix.getB().shape[0]):
            if(self.matrix.getB()[i, 0] < 0):
                rIndex = i - 1
                break

        ratio = float('inf')
        for i in range(0, self.matrix.getA().shape[1]):
            if(self.matrix.getA()[rIndex, i] < 0):
                aux = abs(Fraction(self.matrix.getC()[0, i], self.matrix.getA()[rIndex, i]))
                if(aux < ratio):
                    ratio = aux
                    cIndex = i

        return(self.matrix.getC().shape[0] + rIndex, self.matrix.getMem().shape[1] + cIndex)

    def dual(self):
        (row, col) = self.dualPivot()
        self.matrix.pivoting(row, col)
        printPivoting(self.matrix.tableau)
        self.selection()

    def adjustMatrix(self):
        for i in range(1, self.matrix.getB().shape[0]):
            if(self.matrix.getB()[i, 0] < 0):
                self.matrix.getB()[i, 0] = -1 * self.matrix.getB()[i, 0]

                for j in range(0, self.matrix.getMem().shape[1]):
                    self.matrix.getMem()[i, j] = -1 * self.matrix.getMem()[i, j]

                for j in range(0, self.matrix.getA().shape[1]):
                    self.matrix.getA()[i-1, j] = -1 * self.matrix.getA()[i-1, j]

        self.matrix.extendAuxiliary()

        for i in range(0, len(self.matrix.base)):
            self.matrix.pivoting(self.matrix.base[i][0], self.matrix.base[i][1])

        if(self.matrix.getB()[0, 0] == 0):
            self.selection()
        else:
            self.nonViable()

    def evalAuxiliary(self):
        if(self.matrix.getB()[0, 0] == 0):
            self.matrix.destroyAuxiliary()
            self.auxiliary = False
            self.selection()
        elif(self.matrix.getB()[0, 0] < 0):
            self.nonViable()

    def getSolution(self):
        solution = np.zeros((1, self.matrix.c.shape[1]), dtype='object')

        for i in self.matrix.base:
            (rIndex, cIndex) = (i[0], i[1])

            if(cIndex > self.matrix.getMem().shape[1] and cIndex < (self.matrix.c.shape[1] + self.matrix.getMem().shape[1])):
                solution[0, cIndex - self.matrix.getMem().shape[1]] = self.matrix.getB()[rIndex, 0]

        return solution
