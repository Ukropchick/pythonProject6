"""

Файлы!

"""

'''
Режимы чтения

r - чтение
w - запись
a - добавление файла
b - Binary mode 

'''


# Открытие существующего файла
def open_file():
    file_1 = open("myfile.txt")  # открываем файл в директории питоновского файла (по умолчанию только чтение, mode="r")
    file_2 = open("C:/README.txt")  # открываем с определением путя
    # после всех операций над файлом - закрываем
    file_1.close()
    file_2.close()


def create_file():
    f = open(file="newFile.txt", mode="w")  # пишем несуществующее имя и задаем параметр write - для записи
    # или же просто открываем на запись сущекствующий файл))

    f.close()


def how_to_be_good():
    # тем не менее так никто файлы не открывает, потому что потом надо самому его закрывать нормально и... ме крч
    # норм пацаны делают так
    with open("myfile.txt", "w") as file_to_edit:
        for line in file_to_edit:
            print(line)
    # ничего закрывать не нужно и код выглядит чище!
    # то есть мы просто выходим из тела with и все!


# ну и по файлам это в принципе все...


# выравнивание текста! по заданной ширине строки (line_length)
def align_file(input_name: str, line_length: int, output_name: str):
    with open(output_name, "w") as file_to_edit:
        with open(input_name, "r") as file_to_read:
            current_line_length = 0
            for line in file_to_read:
                if line.isspace() or len(line) == 0:
                    # file_to_edit.write("\n")
                    if current_line_length > 0:
                        file_to_edit.write("\n")
                        current_line_length = 0
                    continue
                for word in line.rsplit(" "):
                    if current_line_length > 0:
                        if len(word) + current_line_length >= line_length:
                            file_to_edit.write("\n")
                            current_line_length = 0
                        else:
                            file_to_edit.write(" ")
                            current_line_length += 1
                    file_to_edit.write(word)
                    current_line_length += len(word)


align_file("align_1.txt", 50, "output.txt")






test = "люк, лок, сом"

if "Лю" in test:
    print(('л'))
