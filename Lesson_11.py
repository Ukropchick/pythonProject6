"""

 * Во входном файле с именем inputName содержится некоторый текст.
 * Некоторые его строки помечены на удаление первым символом _ (подчёркивание).
 * Перенести в выходной файл с именем outputName все строки входного файла, убрав при этом помеченные на удаление.
 * Все остальные строки должны быть перенесены без изменений, включая пустые строки.
 * Подчёркивание в середине и/или в конце строк значения не имеет.

"""


def delete_marked(input_name: str, output_name: str):
    with open(output_name, "w") as file_to_edit:
        with open(input_name, "r") as file_to_read:
            for line in file_to_read:
                if line[0] != "_":
                    file_to_edit.write(line)


"""

 * Во входном файле с именем inputName содержится некоторый текст.
 * На вход подаётся список строк substrings.
 * Вернуть ассоциативный массив с числом вхождений каждой из строк в текст.
 * Регистр букв игнорировать, то есть буквы е и Е считать одинаковыми.

"""


def count_substrings(input_name: str, substrings: list) -> dict:
    repeat = {}
    start_count = 1

    with open(input_name, "r", encoding='utf-8') as file_to_read:
        for line in file_to_read:
            for word in substrings:
                if word in repeat:
                    repeat[word] += line.lower().count(word.lower())
                elif not (word in line):
                    repeat[word] = 0
        return repeat




















        #             if not is_count_changed:
        #                 is_count_changed = True
        #                 start_count = line.count(word.lower())  # считаем количество слов в строке
        #                 repeat[word] = start_count  # задаем это количество в переменную в словаре
        #             if start_count > line.count(word.lower()) or start_count < line.count(word.lower()):
        #                 repeat[word] += line.count(word.lower())
        # return repeat  # выводим
















    # repeat = {}
    # origin_number = 0
    #
    # with open(input_name, "r", encoding='utf-8') as file_to_read:
    #     for line in file_to_read:
    #         number = 0
    #         for word in substrings:
    #             if word.lower() in line.lower():
    #                 number += line.lower().count(word.lower())
    #                 origin_number = line.lower().count(word.lower())
    #                 if origin_number == number:
    #                     repeat[word] = origin_number
    #                 else:
    #                     repeat[word] = origin_number + number
    # return repeat
