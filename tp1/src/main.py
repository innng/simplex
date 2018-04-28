from matrix import Matrix
from sys import argv
import numpy as np

FILENAME = argv[2]
matrix = 0


def main():
    matrix = start()
    matrix.fpi()
    print("fpi:\n", matrix.matrix)
    matrix.tableau()
    print("tableau:\n", matrix.tableau)
    matrix.auxiliary()
    print("auxiliar:\n", matrix.auxiliary)


def start():
    file = open(FILENAME, 'r')
    row = int(file.readline())
    col = int(file.readline())
    aux1 = file.readline()
    aux2 = np.matrix(aux1)
    aux3 = aux2.reshape((row + 1, col + 1))
    m = Matrix(aux3, row, col)
    return m


if __name__ == '__main__':
    main()
