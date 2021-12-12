"""

Для заданного набора символов определить, можно ли составить из него
указанное слово (регистр символов игнорируется)

Например:
canBuildFrom(('a', 'b', 'o'), "baobab") -> true

"""


def can_build_from(chars: list, word: str) -> bool:
    chars_set = set(chars)
    for letters in word:
        if letters in chars_set:
            return True
        else:
            return False


"""

 * Для заданного списка слов определить, содержит ли он анаграммы.
 * Два слова здесь считаются анаграммами, если они имеют одинаковую длину
 * и одно можно составить из второго перестановкой его букв.
 * Скажем, тор и рот или роза и азор это анаграммы,
 * а поле и полено -- нет.
 *
 * Например:
 *   hasAnagrams(("рот", "свет", "код", "дверь")) -> true

"""


def has_anagrams(words: list) -> bool:
    first_index = 0

    while first_index < (len(words) - 1):
        first_word = words[first_index]
        second_index = first_index + 1
        while second_index < len(words):
            second_word = words[second_index]
            second_index += 1
            if len(first_word) == len(second_word):
                if set(first_word) == set(second_word):
                    return True

        first_index += 1
    return False


"""

 * Для заданного списка неотрицательных чисел и числа определить,
 * есть ли в списке пара чисел таких, что их сумма равна заданному числу.
 * Если да, верните их индексы ;
 * если нет, верните пару (-1, -1).
 *
 * Индексы в результате должны следовать в порядке (меньший, больший).
 *
 * Постарайтесь сделать ваше решение как можно более эффективным.
 *
 * Например:
 *   findSumOfTwo((1, 2, 3), 4) -> (0, 2)
 *   findSumOfTwo((1, 2, 3), 6) -> (-1, -1)

"""


def find_sum_of_two(input_list: list, number: int) -> tuple:
    first_index = 0
    while first_index < (len(input_list) - 1):
        first_number = input_list[first_index]
        second_index = first_index + 1
        while second_index < len(input_list):
            second_number = input_list[second_index]
            second_index += 1
            if first_number + second_number == number:
                second_index -= 1
                return first_index, second_index

        first_index += 1
    return -1, -1