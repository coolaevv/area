
def circul():
    pi = 3.1415
    r = int(input('Введите радиус: '))
    s = pi * (r * r)
    print('Площадь круга равна:', s)

def triangle():
    import math
    a = int(input('Введите сторону A: ' ))
    b = int(input('Введите сторону B: ' ))
    c = int(input('Введите сторону C: ' ))
    if a == b or a == c or b == a or b == c:
        print('Треугольник является равнобедренным')
        h = math.sqrt((a * a) - ((b * b) / 4)) #высота
        s = (1 / 2 * b * h) #площадь
        print('Площадь треугольника равна: ', s)
    else:
        print('Треугольник является НЕ равнобедренным')
        p = a + b + c #периметр
        pp = p/2 #полупериметр
        s = math.sqrt(pp * (pp - a) * (pp - b) * (pp - c)) #площадь
        print('Площадь треугольника равна: ', s)
    return triangle()