from simplex import *
from sys import argv


def main():
    start()
    matrix.tableau()
    print(matrix.tableau)
    matrix.updateFractions()
    matrix.divide()

def start():
    file = open(argv[3], 'r')
    row = int(file.readline())
    col = int(file.readline())
    aux = file.readline()
    matrix.init(aux, row, col)


if __name__ == '__main__':
    main()
