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
               ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"],
               ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"],
               ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"],
               ["тысяча", "две тысячи", "три тысячи", "четыре тысячи", "пять тысячь", "шесть тысячь", "семь тысячь", "восемь тысячь", "девять тысячь"]]

    def russian_unites(units: int) -> str:
        if units == 0:
            return ""
        for number_of_unites in range(units):
            number_of_unites += units
            if number_of_unites <= 9:
                return numbers[0][number_of_unites - 1]

    def russian_dozens(dozen: int, units: int) -> str:
        if dozen == 0:
            return ""
        for number_of_dozens in range(dozen):
            number_of_dozens += dozen
            if 1 <= number_of_dozens <= 9:
                if number_of_dozens == 1 and units == 0:
                    return numbers[2][0]
                elif number_of_dozens == 1 and units >= 0:
                    return numbers[1][number_of_dozens - 1]
                else:
                    return numbers[2][number_of_dozens - 1]
    #
    # def russian_hundreds(hundred: int) -> str:
    #     for number_of_hundreds in range(hundred):
    #         number_of_hundreds += hundred
    #         if 1 <= number_of_hundreds <= 9:
    #             return numbers[3][number_of_hundreds - 1]
    #
    # def russia_thousands(thousand: int) -> str:
    #     for number_of_thousand in range(thousand):
    #         number_of_thousand += thousand
    #         if 1 <= number_of_thousand <= 9:
    #             return numbers[4][number_of_thousand - 1]

    return russian_dozens(n % 1000 % 100 // 10, n % 1000 % 100 % 10) + russian_unites(n % 1000 % 100 % 10)
