'''

Классы

класс - это инструкция по которой создаются объекты

объектом в python является все (переменные, строки, массивы и тд)

метод в классе - это функция

Название классов с большой буквы

self - ссылка на экземпляр класса, например показывает методу jump что мы работаем с экземпляром класса Dog

'''


class Dog(): # Определяем класс с именем Dog
    '''Конструкт собаки'''

    def __init__(self, name, age): # метод который выполняется всегда при создании экземпляра класса (базовый функционал объекта)
        '''инициализируем атрибуты: имя и возраст'''
        self.name = name
        self.age = age
        # print("Вы создали собаку")

    def sit(self):
        '''Команда сидеть'''
        print(self.name.title() + " собака села")

    def jump(self):
        '''Команда прыжка'''
        print(self.name.title() + " собака прыгнула")

    def gav(self):
        '''Собака гавкает'''
        print("Гав-гав")



my_pet = Dog('Jess', 2) # Экземпляр класса
my_pet2 = Dog('Rex', 5) # Экземпляр класса

print(my_pet.age)
my_pet.sit()
print(my_pet2.name)
my_pet2.jump()
Simon = Dog('Simon', 3)
Simon.gav()


'''

Работа с классами и экземплярами

1.Если создаем атрибут без указания его в скобках то ему можно задавать любые значения
2.Изменить значение атрибута можно через:
1)Экземпляр класса
2)С помощью метода
3.Местонахождение метода в классе не влияет на его работу в коде

'''

class Car():
    '''Класс - автомобиль'''
    def __init__(self, make, model, date):
        '''Инициализация атрибутов автомобиля'''
        self.make = make
        self.model = model
        self.date = date
        self.odometer = 0 # Можно задать любое значение (атрибут по умолчанию)

    def description_of_car(self):
        '''Инф. о автомобиле'''
        desc = self.make + ' ' + self.model + ' ' + self.date
        print(desc.title())

    def read_odometer(self):
        '''Пробег автомобиля'''
        print("Пробег авто равен " + str(self.odometer) + ' км')

    def update_odometer(self, kilometers): # Изменение атрибута с помощью метода
        '''Изменение пробега'''
        if kilometers >= self.odometer:
            self.odometer = kilometers
        else:
            print('Пробег нельзя уменьшить')

    def increment_odometer(self, kilometers):
        '''Увеличиваем показания пробега (на постоянной основе)'''
        if kilometers >= 0:
            self.odometer += kilometers
        else:
            print('Нельзя прибавлять отрицательные числа')



'''Изменение атрибута с помощбю экземпляра класса'''

my_car = Car('mercedes', 'w220', '2020')
# my_car.odometer = 30 - Обращение к атрибуту на прямую и его последующее изменение
my_car.update_odometer(44)
my_car.increment_odometer(118)


my_car.read_odometer()


'''

Наследование

Наследование - это использование методов одного класса в другом

super() - функция для связи потомка и родителя



'''

class Hero(): # Родительский класс или super class
    '''Класс транспорта'''
    def __init__(self, name, level, xp):
        self.name = name
        self.level = level
        self.xp = xp

    def description_of_hero(self): # Универсальный метод
        '''Статы героя'''
        stats = self.name + ' ' + self.level + ' ' + self.xp
        print(stats.title())

class Sword():
    '''Модель меча для война'''
    def __init__(self, sword="metal"):
        self.sword = sword

    def description_of_sword(self): # Не универсальный метод
        '''Выводит урон от атаки'''
        print('Ваша меч сделан из ' + self.sword)


class Warrior(Hero): # потомок или sub class
    '''Аспекты для воина'''
    def __init__(self, name, level, xp):
        '''Инициализация атрибутов класса родителя'''
        super().__init__(name, level, xp)
        self.sword = Sword() # атрибут меча равен классу Меч (Экземпляр класса Sword используем как атрибут крч)

    def description_of_hero(self): # Переопределение метода родительского класса
        '''Переопределение родительского метода'''
        stats = self.name + ' ' + self.level + ' ' + self.xp
        print(stats.title())




man = Warrior('Max', '10', '250')

man.sword.description_of_sword()




# man.description_of_hero()
# man.attack_damage()
