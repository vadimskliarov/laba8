

import sys


def getInput():
    return float(input("Введите число "))


def testInput(A):
    try:
        int(A)
        return True
    except ValueError:
        return False


def strToInt(B):
    return int(B)


def printInt(C):
    print(C)


if __name__ == '__main__':
    d = getInput()
    if testInput(d) is True:
        e = strToInt(d)
        printInt(e)
    if testInput(d) is False:
        print("Ошибка", file=sys.stderr)
        exit(1)