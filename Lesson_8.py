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
    return "M" * (n // 1000) +\
           roman_digit(n % 1000 // 100, ["C", "D", "M"]) +\
           roman_digit(n % 100 // 10, ["X", "L", "C"]) +\
           roman_digit(n % 10, ["I", "V", "X"])