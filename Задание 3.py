

def program():
    while True:
        a = int(input("a = "))
        b = int(input("b = "))

        if a == 0 or b == 0:
            break

        d = a * b
        print("Произведение a и b =", d)

if __name__ == '__main__':
    program()