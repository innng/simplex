from sys import argv
import numpy as np

pivotingFile = open("pivoting.txt", "a")
pivoting = 0
conclusaoFile = open("conclusao.txt", "w")
conclusao = 1


def getEntry():
    file = open(argv[4], 'r')
    row = int(file.readline())
    col = int(file.readline())
    aux = file.readline()
    file.close()
    return (aux, row, col)


def printPivoting(matrix):
    printMatrix(pivoting, matrix)


def printConclusao(flag, certificate, optimalValue=None, solution=None):
    if(flag >= 0 and flag <= 2):
        conclusaoFile.write(str(flag) + '\n')
    if(flag == 2 and solution is not None):
        printMatrix(conclusao, solution)
    if(flag == 2 and optimalValue is not None):
        conclusaoFile.write(np.format_float_positional(float(optimalValue), precision=5) + '\n')
    printMatrix(conclusao, certificate)

    pivotingFile.close()
    conclusaoFile.close()


def printMatrix(flag, matrix):
    if(flag == pivoting):
        pivotingFile.write('[')
        for i in range(0, matrix.shape[0]):
            pivotingFile.write('[')

            for j in range(0, matrix.shape[1]):
                pivotingFile.write(np.format_float_positional(float(matrix[i, j]), precision=5))

                if(j != (matrix.shape[1] - 1)):
                    pivotingFile.write(', ')

            pivotingFile.write(']')
            if(i != (matrix.shape[0] - 1)):
                pivotingFile.write(', ')
        pivotingFile.write(']' + '\n\n')
    else:
        conclusaoFile.write('[')
        for i in range(0, matrix.shape[0]):
            conclusaoFile.write('[')

            for j in range(0, matrix.shape[1]):
                conclusaoFile.write(np.format_float_positional(float(matrix[i, j]), precision=5))
                if(j != (matrix.shape[1] - 1)):
                    conclusaoFile.write(', ')

            conclusaoFile.write(']')
            if(i != (matrix.shape[0] - 1)):
                conclusaoFile.write(', ')
        conclusaoFile.write(']' + '\n')
