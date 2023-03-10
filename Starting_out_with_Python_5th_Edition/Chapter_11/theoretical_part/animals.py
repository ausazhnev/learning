# Класс Mammal поредставляет род млекопитающих.
class Mammal:
    # Метод __init__ принимает аргумент для
    # вида млекопитающего.
    def __init__(self, species):
        self.__species = species

    # Метод show_species выводит сообщение
    # о виде млекопитающего.
    def show_species(self):
        print(f'Я - {self.__species}')

    # Метод make_sound издает характерный
    # звук для всех млекопитающих.
    def make_sound(self):
        print(f'Гррррр. . .')


# класс Dog является подклассом класса Mammal.
class Dog(Mammal):
    # Метод __init__ вызывает метод __init__
    # надкласса, передавая 'собака' в качестве вида.
    def __init__(self):
        Mammal.__init__(self, 'собака')

    # Метод make_sound переопределяет
    # метод make_sound надкласса.
    def make_sound(self):
        print(f'Гав- гав!')


# класс Cat является подклассом класса Mammal.
class Cat(Mammal):
    # Метод __init__ вызывает метод __init__
    # надкласса, передавая 'кот' в качестве вида.
    def __init__(self):
        Mammal.__init__(self, 'кот')

    # Метод make_sound переопределяет
    # метод make_sound надкласса.
    def make_sound(self):
        print(f'Мяу!')