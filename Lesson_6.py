from math import sqrt
from decimal import *

"""

    Проверить, лежит ли окружность с центром в (x1, y1) и радиусом r1 целиком внутри
    окружности с центром в (x2, y2) и радиусом r2.
    Вернуть true, если утверждение верно

"""


def circle_inside(
        x1: float, y1: float, r1: float,
        x2: float, y2: float, r2: float
) -> bool:
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + r1 ** 2 <= r2 ** 2


"""

    Определить, пройдет ли кирпич со сторонами а, b, c сквозь прямоугольное отверстие в стене со сторонами r и s.
    Стороны отверстия должны быть параллельны граням кирпича.
    Считать, что совпадения длин сторон достаточно для прохождения кирпича, т.е., например,
    кирпич 4 х 4 х 4 пройдёт через отверстие 4 х 4.
    Вернуть true, если кирпич пройдёт

"""


def brick_passes(a: int, b: int, c: int, r: int, s: int) -> bool:
    if s >= a and r >= (b and c):
        return True
    else:
        return s >= b and r >= c


"""

    /// Пример ///
    
    Вычисление факториала

"""


def factorial(n: int) -> float:
    result = 1.0
    for i in range(1, n + 1):
        result = result * i
    return result


"""

    /// Пример ///
    
    Проверка числа на простоту -- результат True, если число простое

"""


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for m in range(3, int(sqrt(n) + 1), 2):
        if n % m == 0:
            return False
    return True


"""

    /// Пример ///
    
    Проверка числа на совершенность -- результат True, если число совершенное

"""


def is_perfect(n: int) -> bool:
    sum = 1
    for m in range(2, n // 2 + 1):
        if n % m > 0:
            continue
        sum += m
        if sum > n:
            break
    return sum == n


"""

    /// Пример (рекурсия) ///
    Функция вызывает сама себя в теле if
    
    Найти число вхождений цифры m в число n

"""


def digit_count_in_number(n: int, m: int) -> int:
    if n == m:
        return 1
    elif n < 10:
        return 0
    else:
        digit_count_in_number(n // 10, m) + digit_count_in_number(n % 10, m)


"""

    Найти количество цифр в заданном числе n.
    Например, число 1 содержит 1 цифру, 456 -- 3 цифры, 65536 -- 5 цифр.
    
    Использовать операции со строками в этой задаче запрещается.

"""


def digit_number(n: int) -> int:
    count = 1
    while n >= 10:
        count += 1
        n = n // 10
    return count


"""

    Найти число Фибоначчи из ряда 1, 1, 2, 3, 5, 8, 13, 21, ... с номером n.
    Ряд Фибоначчи определён следующим образом: fib(1) = 1, fib(2) = 1, fib(n+2) = fib(n) + fib(n+1)

"""


def fib(n: int) -> int:
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib2


#   Для заданного числа n > 1 найти минимальный делитель, превышающий 1

def minimal_divisor(n: int) -> int:
    divisor = 2
    while n % divisor != 0:
        divisor += 1
    return divisor


'''
Определить, являются ли два заданных числа m и n взаимно простыми. 
Взаимно простые числа не имеют общих делителей, кроме 1. 
Например, 25 и 49 взаимно простые, а 6 и 8 — нет.'''


def is_co_prime(m: int, n: int) -> int:
    divisor = 2
    for divisor in range(2, min(m, n)):
        if m % divisor == 0 and n % divisor == 0:
            return False
    return True
    # while m % divisor != 0 and n % divisor != 0:
    #     divisor += 1
    #     if divisor == n or divisor == m:
    #         return True
    #     elif m % divisor == 0 and n % divisor == 0:
    #         return False

