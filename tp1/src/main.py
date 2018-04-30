from matrix import Matrix
from sys import argv

filename = argv[3]
matrix = Matrix()


def main():
    start()
    matrix.default()
    matrix.updateFractions()


def start():
    file = open(filename, 'r')
    row = int(file.readline())
    col = int(file.readline())
    aux = file.readline()
    matrix.init(aux, row, col)


if __name__ == '__main__':
    main()
