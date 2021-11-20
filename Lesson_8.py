"""

 Перевести натуральное число n > 0 в римскую систему.
 Римские цифры: 1 = I, 4 = IV, 5 = V, 9 = IX, 10 = X, 40 = XL, 50 = L,
 90 = XC, 100 = C, 400 = CD, 500 = D, 900 = CM, 1000 = M.
 Например: 23 = XXIII, 44 = XLIV, 100 = C

"""


def roman(n: int) -> str:
    def roman_digit(digit: int, alphabet: list):
        if 0 <= digit <= 3:
            return alphabet[0] * digit
        elif digit == 4:
            return alphabet[0] + alphabet[1]
        elif 5 <= digit <= 8:
            return alphabet[1] + alphabet[0] * (digit - 5)
        else:
            return alphabet[0] + alphabet[2]

    return "M" * (n // 1000) + \
           roman_digit(n % 1000 // 100, ["C", "D", "M"]) + \
           roman_digit(n % 100 // 10, ["X", "L", "C"]) + \
           roman_digit(n % 10, ["I", "V", "X"])


'''

Записать заданное натуральное число 1..[99(9)[999] прописью по-русски.
Например, 375 = "триста семьдесят пять",
23964 = "двадцать три тысячи девятьсот шестьдесят четыре"

'''


def russian(n: int) -> str:
    numbers = [["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"],
               ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"],
               ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"],
               ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]]

    is_number_complex = False

    result = []
    for (index, digit) in enumerate(str(n)):
        int_digit = int(digit)
        list_index = len(str(n)) - 1 - index
        if list_index == 3:
            if is_number_complex:
                result.append("тысяч")
            else:
                if int_digit == 0:
                    result.append("тысяч")
                elif int_digit == 1:
                    result.append("одна тысяча")
                elif int_digit == 2:
                    result.append("две тысячи")
                elif int_digit <= 4:
                    result.append(numbers[list_index % 3][int_digit - 1] + " тысячи")
                elif int_digit <= 9:
                    result.append(numbers[list_index % 3][int_digit - 1] + " тысяч")
            is_number_complex = False # чтобы проверить несколько раз число
        elif int_digit == 0 or is_number_complex:
            continue
        elif list_index % 3 == 1 and int_digit == 1 and int(str(n)[index + 1]) != 0:
            result.append(numbers[3][int(str(n)[index + 1]) - 1])
            is_number_complex = True
        else:
            result.append(numbers[list_index % 3][int_digit - 1])

    return " ".join(result)