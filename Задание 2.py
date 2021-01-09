



import math

def cylinder(r, h, full=True):
    def circle(r):
        return math.pi * (r ** 2)

    s_bor_cylinder = 2 * math.pi * r * h

    if full:
        return s_bor_cylinder + 2 * circle(r)
    else:
        return s_bor_cylinder

if __name__ == '__main__':
    r = float(input("Введите радиус: "))
    h = float(input("Введите высоту: "))
    c = input("s_bor_cylinder(площадь боковой поверхности) или full(полная площадь)?")
    s = cylinder(r, h, full=(c == 'full'))
    print(s)