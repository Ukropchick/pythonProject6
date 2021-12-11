"""

Set

"""


def create_set():
    # set of integers
    my_set = {1, 2, 3}
    print(my_set)

    # set of mixed datatypes
    my_set = {1.0, "Hello", (1, 2, 3)}
    print(my_set)


def duplicates_and_sets():
    # У сетов не может быть дупликатов
    # Output: {1, 2, 3, 4}
    my_set = {1, 2, 3, 4, 3, 2}
    print(my_set)

    # Можем преобразовать лист в сет
    # Output: {1, 2, 3}
    my_set = set([1, 2, 3, 2])
    print(my_set)

    # в сетах не может находиться изменяемый элемент
    # Тут [3, 4] изменяемый лист
    # при попытке запустить код выдаст ошибку "unhashable type: 'list"

    my_set = {1, 2, [3, 4]}
    print(my_set)

def empty_set_creation():
    # создадим пустой "сет"
    a = {}

    # а теперь проверим его тип
    print(type(a))

    # Поэтому лучше сеты задавать как set(), а словари, как dict()
    a = set()

    #  теперь проверим его тип
    print(type(a))

def modify_set():
    # по своей натуре изменяемые, но индексов не имеют
    # Это значит, что мы не можем поменять элемент сета просто так

    # создаем my_set
    my_set = {1, 3}
    print(my_set)

    # my_set[0]
    # если раскомментировать - выдаст ошибку

    # add an element
    # Output: {1, 2, 3}
    my_set.add(2)
    print(my_set)

    # add multiple elements
    # Output: {1, 2, 3, 4}
    my_set.update([2, 3, 4])
    print(my_set)

    # add list and set
    # Output: {1, 2, 3, 4, 5, 6, 8}
    my_set.update([4, 5], {1, 6, 8})
    print(my_set)

def set_delete_ops():
    # Difference between discard() and remove()

    # создаем my_set
    my_set = {1, 3, 4, 5, 6}
    print(my_set)

    # удалим элемент
    # Output: {1, 3, 5, 6}
    my_set.discard(4)
    print(my_set)

    # удалим элемент
    # Output: {1, 3, 5}
    my_set.remove(6)
    print(my_set)

    # за'discard'им несуществующий элемент
    # Output: {1, 3, 5}
    my_set.discard(2)
    print(my_set)

    # за'remove'им несуществующий элемент
    # получим ошибку
    # Output: KeyError

    my_set.remove(2)

def pop_and_clear():
    # initialize my_set
    # Output: set of unique elements
    my_set = set("HelloWorld")
    print(my_set)

    # pop an element
    # Output: random element
    print(my_set.pop())

    # pop another element
    my_set.pop()
    print(my_set)

    # clear my_set
    # Output: set()
    my_set.clear()
    print(my_set)

    print(my_set)

# Основные операции - пересечение | и объединение & сетов
