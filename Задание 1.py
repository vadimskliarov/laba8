


def test(c):
    if c >= 0:
        positive(c)
    elif c < 0:
        negative(c)

def positive(c):
    print('Положительное')

def negative(c):
    print('Отрицательное')

if __name__ == '__main__':
    c = int(input('Введите целое число: '))

    test(c)
