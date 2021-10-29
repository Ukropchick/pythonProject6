from math import sqrt

"""
 * Пример
 *
 * Найти все корни уравнения x^2 = y
 """


def sq_roots(y: float) -> list:
    if y < 0:
        return []
    elif y == 0:
        return [0.0]
    else:
        root = sqrt(y)
        return [-root, root]


"""
 * Пример
 *
 * Выделить в список отрицательные элементы из заданного списка
"""


def negative_list(input_list: list) -> list:
    result = []
    for element in input_list:
        if element < 0:
            result.append(element)
    return result


"""

 * Рассчитать среднее арифметическое элементов списка list. Вернуть 0.0, если список пуст
 
"""


def mean(input_list: list) -> float:
    if len(input_list) == 0:
        return 0
    elif len(input_list) != 0:
        sum = 0
        for number in input_list:
            sum += number
        number_of_characters = len(input_list)
        return sum / number_of_characters





"""

 * Центрировать заданный список list, уменьшив каждый элемент на среднее арифметическое всех элементов.
 * Если список пуст, не делать ничего. Вернуть изменённый список.

"""


def center(input_list: list) -> list:
    if len(input_list) == 0:
        return 0
    elif len(input_list) != 0:
        number = sum(input_list)
        average = number / len(input_list)
        new_list = []
        for numbers in input_list:
            new_list.append(numbers - average)
        return new_list




"""

 * Рассчитать значение многочлена при заданном x:
 * p(x) = p0 + p1*x + p2*x^2 + p3*x^3 + ... + pN*x^N.
 * Коэффициенты многочлена заданы списком p: (p0, p1, p2, p3, ..., pN).
 * Значение пустого многочлена равно 0 при любом x.

"""


def polynom(p: list, x: int) -> int:
    if len(p) == 0:
        return 0
    elif len(p) > 0:
        N = 0
        multiplier = []
        for factor in p:
            multiplier.append(factor * x ** N)
            N += 1
        return sum(multiplier)




"""

 * Разложить заданное натуральное число n > 1 на простые множители.
 * Результат разложения вернуть в виде списка множителей, например 75 -> (3, 5, 5).
 * Множители в списке должны располагаться по возрастанию.

"""


def factorize(n: int) -> list:
    multiplier = []
    for i in range(n + 1):
        if i < 2:
            continue
        while n % i == 0:
            multiplier.append(i)
            n /= i
    return multiplier





"""

 * Перевести заданное целое число n >= 0 в систему счисления с основанием base > 1.
 * Результат перевода вернуть в виде списка цифр в base-ичной системе от старшей к младшей,
 * например: n = 100, base = 4 -> (1, 2, 1, 0) или n = 250, base = 14 -> (1, 3, 12)

"""


def convert(n: int, base: int) -> list:
    number_in_another_system = []
    for divider in range(n):
        n //= base
        while n < base:
            number_in_another_system.append(n)
            break
        number_in_another_system.reverse()
        # if n % base == 0:
        #     n //= base
        #     number_in_another_system.append(n)
    return number_in_another_system
