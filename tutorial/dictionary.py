"""

Dictionary

"""

"""

Чтобы понять первую структуру данных --- ассоциативный массив --- далеко ходить не надо,
достаточно вспомнить о такой штуке как толковый словарь. Он связывает элементы отношением "ключ"-"значение":
для определенных слов (ключей) он содержит их описание (значения), для всех остальных --- не содержит ничего. 
Подобной структурой обладают, на самом деле, многие вещи: набор товаров с их ценами, список контактов в телефоне, 
рестораны и рейтинги, и т.д. Основная операция, которую они поддерживают, --- это достать значение, 
соответствующее интересующему нас ключу, т.е. то, что вы делаете, когда ищете значение неизвестного вам слова в словаре.

"""

"""

Ассоциативный массив является обобщенным способом представить подобное отношение. 
Давай на следующем примере посмотрим, как с ним можно работать. 
Представим, что нам необходимо посчитать стоимость нашего списка покупок для заданного набора товаров. 
Сделать это можно при помощи следующей функции.

"""


def shopping_list_cost(
        shopping_list: list,
        costs: dict) -> float:
    total_cost = 0.0

    for item in shopping_list:
        if item in costs:
            item_cost = costs[item]
            total_cost += item_cost

    return total_cost


# item_costs = {"Хлеб": 50, "Молоко": 100, "Мясо": 600, "Рыба": 800, "Мыло": 80}
# print(shopping_list_cost(["Хлеб", "Молоко"], item_costs))
# print(shopping_list_cost(["Молоко"], item_costs))
# print(shopping_list_cost(["Хлеб"], item_costs))
# print(shopping_list_cost(["Хлеб", "Молоко", "кефир"], item_costs))

"""

А теперь поговорим о всех синтаксических приколах)

"""

"""

Создание dict

"""
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1: 'apple', 2: 'ball'})

# from sequence having each item as a pair
my_dict = dict([(1, 'apple'), (2, 'ball')])

"""

Доступ к элементам dict

"""


def access():
    # get vs [] for retrieving elements
    my_dictionary = {'name': 'Jack', 'age': 26}

    # Output: Jack
    print(my_dictionary['name'])

    # Output: 26
    print(my_dictionary.get('age'))

    # Trying to access keys which doesn't exist throws error
    # Output None
    print(my_dictionary.get('address'))

    # KeyError
    print(my_dictionary['address'])


def remove():
    # Removing elements from a dictionary

    # create a dictionary
    squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    # remove a particular item, returns its value
    # Output: 16
    print(squares.pop(4))

    # Output: {1: 1, 2: 4, 3: 9, 5: 25}
    print(squares)

    # remove an arbitrary item, return (key,value)
    # Output: (5, 25)
    print(squares.popitem())

    # Output: {1: 1, 2: 4, 3: 9}
    print(squares)

    # remove all items
    squares.clear()

    # Output: {}
    print(squares)

    # delete the dictionary itself
    del squares

    # Throws Error
    print(squares)


def change_or_add_elemnts():
    # Changing and adding Dictionary Elements
    my_dict = {'name': 'Jack', 'age': 26}

    # update value
    my_dict['age'] = 27

    # Output: {'age': 27, 'name': 'Jack'}
    print(my_dict)

    # add item
    my_dict['address'] = 'Downtown'
    # Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
    print(my_dict)


"""

Примеры

"""


def filter_by_country_code(
        phone_book: dict,
        country_code: str):
    names_to_remove = list()

    for name in phone_book:
        phone = phone_book[name]
        print(name, phone)
        if not phone.startswith(country_code):
            names_to_remove.append(name)

    for name in names_to_remove:
        del phone_book[name]

    return phone_book


def filter_by_country_code_optimal(
        phone_book: dict,
        country_code: str):
    for name in phone_book:
        phone = phone_book[name]
        print(name, phone)
        if phone.startswith(country_code):
            del phone_book[name]

    return phone_book


phoneBook = {
    "Quagmire": "+1-800-555-0143",
    "Adam's Ribs": "+82-000-555-2960",
    "Pharmakon Industries": "+1-800-555-6321"
}

new_book = filter_by_country_code(phoneBook, "+1")
print("2", len(new_book))

"""

    По заданному ассоциативному массиву "студент"-"оценка за экзамен" построить
    обратный массив "оценка за экзамен"-"список студентов с этой оценкой".
    Например:
        {"Марат": 3, "Семён": 5, "Михаил": 5}
        -> {5: ["Семён", "Михаил"], 3: ["Марат"]}
    
"""


def build_grades(grades: dict) -> dict:
    revers = {}

    for name in grades:
        grade = grades[name]
        if not (grade in revers):
            revers[grade] = list()
        revers[grade].append(name)
    return revers


print(build_grades({"Марат": 3, "Семён": 5, "Михаил": 5}))

"""

Определить, входит ли ассоциативный массив a в ассоциативный массив b;
это выполняется, если все ключи из a содержатся в b с такими же значениями.

"""


def contains_in(a: dict, b: dict) -> bool:
    for key in a:
        value = a[key]
        if key in b:
            if value != b[key]:
                return False
        else:
            return False
    return True


print(contains_in({"Андрей": 3, "Семён": 5}, {"Марат": 3, "Семён": 5, "Михаил": 5}))
"""

    Удалить из b все записи,
    которые встречаются в a.
    Записи считать одинаковыми, если и ключи, и значения совпадают.

"""


def subtract_of(a: dict, b: dict):
    dict_a = a
    dict_b = b
    for key in dict_a:
        value = dict_a[key]
        if key in dict_b:
            if value == dict_b[key]:
                del dict_b[key]


def main():
    a = {"Андрей": 3, "Семён": 5}
    b = {"Марат": 3, "Семён": 5, "Михаил": 5}
    subtract_of(a, b)
    print(b)

main()