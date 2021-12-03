"""

 * Объединить два ассоциативных массива `dict_a` и `dict_b` с парами
 * "имя"-"номер телефона" в итоговый ассоциативный массив, склеивая
 * значения для повторяющихся ключей через запятую.
 * В случае повторяющихся *ключей* значение из dict_a должно быть
 * перед значением из dict_b.
 *
 * Повторяющиеся *значения* следует добавлять только один раз.
 *
 * Например:
 *   merge_phone_books(
 *     {"Emergency": "112", "Police": "02"},
 *     {"Emergency": "911", "Police": "02"}
 *   ) -> {"Emergency": "112, 911", "Police": "02"}

"""


def merge_phone_books(dict_a: dict, dict_b: dict) -> dict:
    # join = {}
    #
    # for key in dict_a:
    #     value = dict_a[key]
    #     if key in dict_b:
    #         join[key] = []
    #         if value == dict_b[key]:
    #             join[key].append(value)
    #     elif not (key in dict_b):
    #         join[key] = value
    #
    # for key2 in dict_b:
    #     value2 = dict_b[key2]
    #     if key2 in dict_a:
    #         if value2 == dict_a[key2]:
    #             join[key] += value2
    #         else:
    #             join[key] += value2
    #     elif not (key2 in dict_a):
    #         join[key] = value2

    return join


"""

 * Входными данными является ассоциативный массив
 * "название товара"-"пара (тип товара, цена товара)"
 * и тип интересующего нас товара.
 * Необходимо вернуть название товара заданного типа с минимальной стоимостью
 * или None в случае, если товаров такого типа нет.
 *
 * Например:
 *   find_cheapest_stuff(
 *     {"Мария": ("печенье" to 20.0), "Орео": ("печенье" to 100.0)),
 *     "печенье"
 *   ) -> "Мария"

"""


def find_cheapest_stuff(stuff: dict, kind: str) -> str:
    keys = []
    names = []
    prices = []

    for key in stuff:
        keys.append(key)
        name = stuff[key][0]
        names.append(name)
        price = stuff[key][1]
        prices.append(price)
    if names[0] == kind or names[1] == kind:
        if prices[0] < prices[1]:
            return keys[0]
        else:
            return keys[1]


"""

 * Найти в заданном списке повторяющиеся элементы и вернуть
 * ассоциативный массив с информацией о числе повторений
 * для каждого повторяющегося элемента.
 * Если элемент встречается только один раз, включать его в результат
 * не следует.

 Например:
 *   extract_repeats(["a", "b", "a"]) -> {"a": 2}
 
"""


def extract_repeats(input_list: list) -> dict:
    repeat = {}

    if len(input_list) != 0:
        for keys in input_list:
            value = keys
            if input_list.count(value) > 1:
                repeat[value] = input_list.count(value)
            else:
                return repeat
    else:
        return repeat


