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
               ["тысяча", "две тысячи", "три тысячи", "четыре тысячи", "пять тысячь", "шесть тысячь", "семь тысячь", "восемь тысячь", "девять тысячь"],
               ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]]

    flag = True

    def russian_unites(units: int) -> str:
        if units == 0 or not flag:
            return ""
        else:
            return numbers[0][units - 1]

    def russian_dozens(dozen: int, units: int) -> str:
        if dozen == 0:
            return ""
        if 1 <= dozen <= 9:
            if dozen == 1 and units == 0:
                return numbers[2][0]
            elif dozen == 1 and units >= 0:
                flag = False
                return numbers[1][dozen - 1]
            else:
                return numbers[2][dozen - 1]

    # def russian_hundreds(hundred: int) -> str:
    #     if hundred == 0:
    #         return ""
    #     for number_of_hundreds in range(hundred):
    #         number_of_hundreds += hundred
    #         if 1 <= number_of_hundreds <= 9:
    #             return numbers[3][number_of_hundreds - 1]
    #
    # def russia_thousands(thousand: int) -> str:
    #     if thousand == 0:
    #         return "тысяч"
    #     for number_of_thousand in range(thousand):
    #         number_of_thousand += thousand
    #         if 1 <= number_of_thousand <= 9:
    #             return numbers[4][number_of_thousand - 1]
    a = '102'
    result = []
    for (index, digit) in enumerate(str(n)):
        int_digit = int(digit)
        list_index = (len(str(n)) - 1 - index) % 4
        list_index2 = len(str(n)) - 1 - index
        if list_index == 3:
            flag = True
        if int_digit == 0 or not flag:
            continue
        elif list_index == 1 and int_digit == 1 and str(n)[index + 1] != 0:
            result.append(numbers[4][int(str(n)[index + 1]) - 1])
            flag = False
        elif list_index2 == 4:
            result.append(numbers[list_index2][int_digit - 1])
        else:
            result.append(numbers[list_index][int_digit - 1])

    return " ".join(result)
