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
    merged_dict = {}
    for key in dict_a:
        merged_dict[key] = dict_a[key]
        if key in dict_b:
            if not dict_a[key] == dict_b[key]:
                merged_dict[key] += ", " + dict_b[key]
            del dict_b[key]
    for key in dict_b:
        merged_dict[key] = dict_b[key]
    return merged_dict



"""

 * Входными данными является ассоциативный массив
 * "название товара"-"пара (тип товара, цена товара)"
 * и тип интересующего нас товара.
 * Необходимо вернуть название товара заданного типа с минимальной стоимостью
 * или None в случае, если товаров такого типа нет.
 *
 * Например:
 *   find_cheapest_stuff(
 *     {"Мария": ("печенье", 100.0), "Орео": ("печенье", 20.0)},
 *     "печенье"
 *   ) -> "Мария"

"""


def find_cheapest_stuff(stuff: dict, kind: str):
    name = ''
    lowest_price = -1
    is_lp_changed = False

    for key in stuff:
        value = stuff[key]
        if value[0] == kind:
            if not is_lp_changed:
                is_lp_changed = True
                lowest_price = value[1]
            if value[1] <= lowest_price:
                lowest_price = value[1]
                name = key
    if name == "":
        return None
    else:
        return name


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
        for item in input_list:
            result = input_list.count(item)
            if result > 1:
                repeat[item] = result
                index = 0
                while index < len(input_list):
                    new_item = input_list[index]
                    if new_item == item:
                        del input_list[index]
            else:
                return repeat
    else:
        return repeat
