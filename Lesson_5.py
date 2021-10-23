"""

    Треугольник задан длинами своих сторон a, b, c.
    Проверить, является ли данный треугольник остроугольным (вернуть 0),
    прямоугольным (вернуть 1) или тупоугольным (вернуть 2).
    Если такой треугольник не существует, вернуть -1.

"""


def triangle_kind(a: float, b: float, c: float) -> int:
    max_side = max(a, b, c)
    average_side1 = 0
    average_side2 = 0

    if max_side == a:
        average_side1 = b
        average_side2 = c
    elif max_side == b:
        average_side1 = a
        average_side2 = c
    else:
        average_side1 = a
        average_side2 = b

    if max_side > average_side1 + average_side2:
        return -1

    sqr_max_side = max_side ** 2
    sum_of_squares = average_side1 ** 2 + average_side2 ** 2

    if sqr_max_side == sum_of_squares:
        return 1
    elif sqr_max_side > sum_of_squares:
        return 2
    else:
        return 0


"""

    Даны четыре точки на одной прямой: A, B, C и D.
    Координаты точек a, b, c, d соответственно, b >= a, d >= c.
    Найти длину пересечения отрезков AB и CD.
    Если пересечения нет, вернуть -1.

"""


def segment_length(a: int, b: int, c: int, d: int) -> int:
    if c <= b and d >= a:
        if c < a:
            if b < d:
                return b - a
            else:
                return d - a
        else:
            if d < b:
                return d - c
            else:
                return b - c
    else:
        return -1



"""

    Лежит ли точка (x, y) внутри окружности с центром в (x0, y0) и радиусом r?

"""


def point_inside_circle(x: float, y: float, x0: float, y0: float, r: float) -> bool:
    return (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2


"""

    Четырехзначное число назовем счастливым, если сумма первых двух ее цифр равна сумме двух последних.
    Определить, счастливое ли заданное число, вернуть true, если это так.

"""


def is_number_happy(number: int) -> bool:
    first_sum = (number // 1000) + (number % 1000 // 100)
    second_sum = (number % 1000 % 100 // 10) + (number % 1000 % 100 % 10)
    return first_sum == second_sum


"""

    На шахматной доске стоят два ферзя (ферзь бьет по вертикали, горизонтали и диагоналям).
    Определить, угрожают ли они друг другу. Вернуть true, если угрожают.
    Считать, что ферзи не могут загораживать друг друга.

"""


def queen_threatens(x1: int, y1: int, x2: int, y2: int) -> bool:
    return (x1 == x2 or y1 == y2) or (abs(x1 - x2) == abs(y1 - y2))



"""

    Дан номер месяца (от 1 до 12 включительно) и год (положительный).
    Вернуть число дней в этом месяце этого года по григорианскому календарю.

"""


def days_in_month(month: int, year: int) -> int:

    if month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return 29
        else:
            return 28

    if month == 1 or\
            month == 3 or\
            month == 5 or\
            month == 7 or\
            month == 8 or\
            month == 10 or\
            month == 12:
        return 31
    else:
        return 30
