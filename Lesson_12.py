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
    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
              'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    days = int(string[0] + string[1])

    for month in re.findall(r'[а-яА-Я]+', string):
        for index, item in enumerate(months):
            month_number = index + 1
            month_number_str = str(month_number)
            if month == item:
                if month_number == 2:
                    if days <= 28:
                        if month_number < 10:
                            return re.sub(r'\s[а-яА-Я]+\s', '.' + '0' +  month_number_str + '.', string)
                        else:
                            return re.sub(r'\s[а-яА-Я]+\s', '.' + month_number_str + '.', string)
                    else:
                        return ""
                if month_number == 4 or month_number == 6 or month_number == 9 or month_number == 11:
                    if days <= 30:
                        if month_number < 10:
                            return re.sub(r'\s[а-яА-Я]+\s', '.' + '0' +  month_number_str + '.', string)
                        else:
                            return re.sub(r'\s[а-яА-Я]+\s', '.' + month_number_str + '.', string)
                    else:
                        return ""
                elif month_number == 1 or month_number == 3 or month_number == 5 or \
                        month_number == 7 or month_number == 8 or month_number == 10 or month_number == 12:
                    if days <= 30:
                        if month_number < 10:
                            return re.sub(r'\s[а-яА-Я]+\s', '.' + '0' + month_number_str + '.', string)
                        else:
                            return re.sub(r'\s[а-яА-Я]+\s', '.' + month_number_str + '.', string)
                    else:
                        return ""
                else:
                    return ""
        return ""







    months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
              'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    # days = int(string[0] + string[1])
    #
    # for month in re.finditer(r'\w', string):
    #     a = month[0]

            #     month_number_str = str(month_number)
            #     return re.sub(r'\s\W\s', month_number_str, string)
            # else:
            #     return ""


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
    for phone_number in re.findall(r'\+\d\s[(]\d+[)]\s\d+[-]+\d+[-]+\d+', phone):
        ''' TODO '''

"""

 * Результаты спортсмена на соревнованиях в прыжках в длину представлены строкой вида
 * "706 - % 717 % 703".
 * В строке могут присутствовать числа, черточки - и знаки процента %, разделённые пробелами;
 * число соответствует удачному прыжку, - пропущенной попытке, % заступу.
 * Прочитать строку и вернуть максимальное присутствующее в ней число (717 в примере).
 * При нарушении формата входной строки или при отсутствии в ней чисел, вернуть -1.

"""


def best_long_jump(jumps: str) -> int:
    minimal_jump = 0
    if not re.search(r'\d+', jumps) == None:
        if re.search(r'[+]', jumps) != None:
            return -1
        else:
            for number in re.findall(r'\d+', jumps):
                if int(number) > minimal_jump:
                    minimal_jump = int(number)
            return minimal_jump
    else:
        return -1

