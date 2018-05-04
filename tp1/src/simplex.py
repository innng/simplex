from matrix import Matrix


matrix = Matrix()


def algorithmSelector():
    c = True
    b = True

    for i in range(0, matrix.parts['c'].shape[1]):
        if(matrix.parts['c'][0, i] < 0):
            c = False
            break

    for i in range(0, matrix.parts['b'].shape[0]):
        if(matrix.parts['b'][i, 0] < 0):
            b = False
            break

    if(c == False and b == True):
        print("primal")
    elif(c == True and b == False):
        print("dual")
    elif(c == False and b == False):
        print("auxiliar")


def primalPivot():
    print("primal")


def dualPivot():
    print("dual")


def primal():
    print("primal")


def dual():
    print("dual")
