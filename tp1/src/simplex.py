from fractions import Fraction
from matrix import Matrix


matrix = Matrix()


def selection():
    c = True
    b = True

    for i in range(0, matrix.getC().shape[1]):
        if(matrix.getC()[0, i] < 0):
            c = False
            break

    for i in range(1, matrix.getB().shape[0]):
        if(matrix.getB()[i, 0] < 0):
            b = False
            break

    if(c is True and b is False):
        valid = testNonViable()
        if(valid is True):
            dual()
        else:
            nonViable()
    elif(c is False and b is True):
        valid = testUnbounded()
        if(valid is True):
            primal()
        else:
            unbounded()
    elif(c is False and b is False):
        adjustMatrix()
    elif(c is True and b is True):
        limited()


def testNonViable():
    for i in range(1, matrix.getB().shape[0]):
        valid = False
        if(matrix.getB()[i, 0] < 0):
            for j in range(0, matrix.getA().shape[1]):
                if(matrix.getA()[i - 1, j] < 0):
                    valid = True
                    break
            if(valid is False):
                return False
    return True


def testUnbounded():
    for i in range(0, matrix.getC().shape[1]):
        valid = False
        if(matrix.getC()[0, i] < 0):
            for j in range(0, matrix.getA().shape[0]):
                if(matrix.getA()[j, i] > 0):
                    valid = True
                    break
            if(valid is False):
                return False
    return True


def nonViable():
    print("inviável")


def unbounded():
    print("ilimitada")


def limited():
    print("end")


def primalPivot():
    rIndex = -1
    cIndex = -1

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
    matrix.pivoting(row, col)
    selection()


def dualPivot():
    rIndex = -1
    cIndex = -1

    for i in range(1, matrix.getB().shape[0]):
        if(matrix.getB()[i, 0] < 0):
            rIndex = i - 1
            break

    ratio = float('inf')
    for i in range(0, matrix.getA().shape[1]):
        if(matrix.getA()[rIndex, i] < 0):
            aux = abs(Fraction(matrix.getC()[0, i], matrix.getA()[rIndex, i]))
            if(aux < ratio):
                ratio = aux
                cIndex = i

    return(matrix.getC().shape[0] + rIndex, matrix.getMem().shape[1] + cIndex)


def dual():
    (row, col) = dualPivot()
    matrix.pivoting(row, col)
    selection()


def adjustMatrix():
    print("adjust")
