import re

"""

Exception handling and regex

"""

try:
    raise Exception("Invalid argument")  # свое бросаем исключение
except Exception as e:
    print("found", e)

try:
    a = []
    for i in range(0, 10):
        a.append(i)
    print(a[11])
except Exception as e:
    print("found", e)
else:
    print("nothing was found")

"""

 * Пример
 *
 * Время представлено строкой вида "11:34:45", содержащей часы, минуты и секунды, разделённые двоеточием.
 * Разобрать эту строку и рассчитать количество секунд, прошедшее с начала дня.

"""


def time_str_to_seconds(string: str) -> int:
    parts = str.split(":")
    result = 0
    for part in parts:
        number = int(part)
        result = result * 60 + number
    return result


"""

Дата представлена строкой вида "15 июля 2016".
 * Перевести её в цифровой формат "15.07.2016".
 * День и месяц всегда представлять двумя цифрами, например: 03.04.2011.
 * При неверном формате входной строки вернуть пустую строку.
 *
 * Обратите внимание: некорректная с точки зрения календаря дата 
 * (например, 30.02.2009) считается неверными входными данными.

"""


def date_str_to_digit(string: str) -> str:
    months = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
              'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}

    def str_add(number: str):
        if int(number) < 10:
            return "0" + str(number)
        else:
            return str(number)

    if re.fullmatch(r'\d+\s[а-яА-Я]+\s\d+', string) is not None:
        date_list = string.split(" ")
        if date_list[1] in months:
            return str_add(date_list[0]) + '.' + str_add(months[date_list[1]]) + '.' + date_list[2]
    return ""



"""

 * Номер телефона задан строкой вида "+7 (921) 123-45-67".
 * Префикс (+7) может отсутствовать, код города (в скобках) также может отсутствовать.
 * Может присутствовать неограниченное количество пробелов и чёрточек,
 * например, номер 12 --  34- 5 -- 67 -89 тоже следует считать легальным.
 * Перевести номер в формат без скобок, пробелов и чёрточек (но с +), например,
 * "+79211234567" или "123456789" для приведённых примеров.
 * Все символы в номере, кроме цифр, пробелов и +-(), считать недопустимыми.
 * При неверном формате вернуть пустую строку.
 *
 * PS: Дополнительные примеры работы функции можно посмотреть в соответствующих тестах.

"""


def flatten_phone_number(phone: str) -> str:
    if re.fullmatch(r'^(\+\d+)?[-\s]*(\(([-\s]*\d+)+[-\s]*\))?([-\s]*\d+)+[-\s]*$', phone) is not None:
        formatted_phone_number = ''
        for digit in re.findall(r'[+\d+]', phone):
            formatted_phone_number += digit
        return formatted_phone_number
    else:
        return ""


"""

 * Результаты спортсмена на соревнованиях в прыжках в длину представлены строкой вида
 * "706 - % 717 % 703".
 * В строке могут присутствовать числа, черточки - и знаки процента %, разделённые пробелами;
 * число соответствует удачному прыжку, - пропущенной попытке, % заступу.
 * Прочитать строку и вернуть максимальное присутствующее в ней число (717 в примере).
 * При нарушении формата входной строки или при отсутствии в ней чисел, вернуть -1.

"""


def best_long_jump(jumps: str) -> int:
    max_jump = 0
    if re.search(r'[^-%\s\d]|[-%]{2}', jumps) is not None or re.search(r'\d+', jumps) is None:
        return -1
    else:
        for number in re.findall(r'\d+', jumps):
            if int(number) > max_jump:
                max_jump = int(number)
        return max_jump
