def string_init():
    my_string = 'Hello'
    print(my_string)

    my_string = "Hello"
    print(my_string)

    print("hell\no")


def access_character():
    new_str = "hello!"
    new_list = list(new_str)
    print('str = ', new_str)
    print("list = ", new_list)

    # first character
    print('str[0] = ', new_str[0])

    # last character
    print('str[-1] = ', new_str[-1])

    # slicing 2nd to 5th character
    print('str[1:5] = ', new_str[1:5])

    # slicing 6th to 2nd last character
    print('str[5:-2] = ', new_str[5:-2])


def out_of_range_exeption():
    new_str = "hello!"
    new_list = [0] * 11

    print(new_str[9])
    print(new_list[10])


def iterating():
    count = 0
    for letter in 'Hello World':
        if (letter == 'l'):
            count += 1
    print(count, 'letters found')


def character_to_find():
    new_string = "hello"
    new_list = [9, 8, 7]
    print("e" in new_string)
    print("a" in new_string)
    print(9 in new_list)


def enumerate_list():
    str = 'cold'
    list_enumerate = list(enumerate(str))
    print('list(enumerate(str) = ', list_enumerate)

    for (index, letter) in list_enumerate:
        print(index, end=" ")
        print(letter)


def string_formatting():
    # using triple quotes
    print('''He said, "Hello!"''')

    # escaping single quotes
    print('He said, "What\'s there?"')

    # escaping double quotes
    print("He said, \"What's there?\"")


my_list = [1, 2, 4, 5, 6]
my_list_string = ["1", "2", "3", "4", "5", "6"]

print(my_list[0], my_list[1], sep=" ", end=" ")
print(my_list[0], my_list[1], sep=" ", end=" ")
str(my_list)
",".join(my_list)
