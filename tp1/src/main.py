from simplex import matrix
from simplex import selection
from utils import entry


def main():
    (aux, row, col) = entry()
    matrix.init(aux, row, col)
    matrix.tableau()
    print(matrix.base)
    print(matrix.tableau, '\n\n')
    selection()
    # np.set_printoptions(precision=6, suppress=True)


if __name__ == '__main__':
    main()
