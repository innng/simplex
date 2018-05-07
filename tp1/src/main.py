from simplex import Simplex
from utils import getEntry

simplex = Simplex()


def main():
    (aux, row, col) = getEntry()
    simplex.init(aux, row, col)


if __name__ == '__main__':
    main()
