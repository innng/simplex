from sys import argv


def entry():
    file = open(argv[4], 'r')
    row = int(file.readline())
    col = int(file.readline())
    aux = file.readline()
    file.close()
    return (aux, row, col)
    # print(matrix.base)
    # np.set_printoptions(precision=6, suppress=True)
    # print(matrix.tableau.astype(float), '\n\n', )


def printPivot(matrix):
    file = open("pivoting.txt", "a")
    file.write(str(matrix))
