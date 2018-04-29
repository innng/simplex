from matrix import Matrix
from sys import argv

filename = argv[3]
matrix = Matrix()


def main():
    start()
    matrix.fpi()
    print("fpi:")
    print(matrix.fpi)
    matrix.tableau()
    print("tableau:")
    print(matrix.tableau)
    matrix.auxiliary()
    print("auxiliar:")
    print(matrix.auxiliary)


def start():
    file = open(filename, "r")
    row = int(file.readline())
    col = int(file.readline())
    aux1 = file.readline()
    matrix.init(aux1, row, col)


if __name__ == '__main__':
    main()
