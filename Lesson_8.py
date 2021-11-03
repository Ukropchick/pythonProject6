"""

 Перевести натуральное число n > 0 в римскую систему.
 Римские цифры: 1 = I, 4 = IV, 5 = V, 9 = IX, 10 = X, 40 = XL, 50 = L,
 90 = XC, 100 = C, 400 = CD, 500 = D, 900 = CM, 1000 = M.
 Например: 23 = XXIII, 44 = XLIV, 100 = C

"""


def roman(n: int) -> str:
    def units(unit: int):
        number_units = ""
        if 0 <= unit <= 3:
            number_units += "I" * unit
        elif unit == 4:
            number_units += "IV"
        elif 5 <= unit <= 8:
            number_units += "V" + "I" * (unit - 5)
        else:
            number_units += "IX"
        return number_units

    def dozens(dozen: int):
        number_dozens = ""
        if 0 <= dozen <= 3:
            number_dozens += "X" * dozen
        elif dozen == 4:
            number_dozens += "XL"
        elif 5 <= dozen <= 8:
            number_dozens += "L" + "X" * (dozen - 5)
        else:
            number_dozens += "XC"

    def hundreds(hundred: int):
        number_hundred = ""
        if 0 <= hundred <= 3:
            number_hundred += "C" * hundred
        elif hundred == 4:
            number_hundred += "CD"
        elif 5 <= hundred <= 8:
            number_hundred += "D" + "C" * (hundred - 5)
        else:
            number_hundred += "CM"

    def thousands(thousand: int):
        number_thousand = ""
        if thousand == 1:
            number_thousand += "M"
        else:
            number_thousand += "M" * thousand

    return units(n)