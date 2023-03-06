# 1. Предположим, что my_car - это имя переменной, которая ссылается на объект, и go - это имея
# метода. Напишите инструкцию, которая использует переменную my_car  для вызова метода go().
# (В метод go() аргументы не должны передаваться.)
my_car.go()

# 2. Напишите определение класса с именем Book. Класс Book должен иметь атрибуты данных для
# заголовка книги, имени автора и имени издателя. Этот класс должен также иметь следующие методы:
# - метод __init__() для класса должен принимать аргумент для каждого атрибута данных;
# - методы-получатели и методы мутаторы для каждого атрибута данных;
# - метод __str__(), который возвращает строковое значение, сообщающее о состоянии объекта.
class Book:
    def __init__(self, name, author, publisher):
        self.__name = name
        self.__author = author
        self.__publisher = publisher

    def set_name(self, name):
        self.__name = name

    def set_author(self, author):
        self.__author = author

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def get_publisher(self):
        return self.__publisher

    def __str__(self):
        return f'Заголовок: {self.__name} Автор: {self.__author} Издатель:{self.__publisher}'



