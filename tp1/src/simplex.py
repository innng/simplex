from fractions import Fraction
from matrix import Matrix


matrix = Matrix()


def selector():
    c = True
    b = True

    for i in range(0, matrix.getC().shape[1]):
        if(matrix.getC()[0, i] < 0):
            c = False
            break

    for i in range(0, matrix.getB().shape[0]):
        if(matrix.getB()[i, 0] < 0):
            b = False
            break

    if(c is False and b is True):
        primal()
    elif(c is True and b is False):
        dual()
    elif(c is False and b is False):
        adjustMatrix()
    elif(c is True and b is True):
        print("done")


def primalPivot():
    rIndex = 0
    cIndex = 0

    for i in range(0, matrix.getC().shape[1]):
        if(matrix.getC()[0, i] < 0):
            cIndex = i
            break

    ratio = float('inf')
    for i in range(0, matrix.getA().shape[0]):
        if(matrix.getA()[i, cIndex] > 0):
            aux = Fraction(matrix.getB()[i + 1, 0], matrix.getA()[i, cIndex])
        if(aux < ratio):
            ratio = aux
            rIndex = i

    return (matrix.getC().shape[0] + rIndex, matrix.getMem().shape[1] + cIndex)


def primal():
    (row, col) = primalPivot()
    matrix.pivot(row, col)
    selector()


def dualPivot():
    print("pivot")


def dual():
    (row, col) = dualPivot()
    matrix.pivot(row, col)
    selector()


def adjustMatrix():
    print("adjust")
