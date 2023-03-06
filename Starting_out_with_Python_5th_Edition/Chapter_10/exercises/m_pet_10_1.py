# Класс Pet

class Pet:
    # Инициализируем объект, если при этом значение атрибутов
    # не передано, устанавливаем их значение как None
    def __init__(self, name = None, animal_type = None, age = None):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # метод устанавливает значение атрибута: __name
    def set_name(self, name):
        self.__name = name

    # метод устанавливает значение атрибута: __animal_type
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # метод устанавливает значение атрибута: __age
    def set_age(self, age):
        self.__age = age

    # Метод возвращает значение атрибута: __name
    def get_name(self):
        return self.__name

    # Метод возвращает значение атрибута: __animal_type
    def get_animal_type(self):
        return self.__animal_type

    # Метод возвращает значение атрибута: __age
    def get_age(self):
        return self.__age

    # Метод возвращает текущее состояние объекта
    def __str__(self):
        return f'Имя: {self.__name}, ' \
               f'Тип питомца: {self.__animal_type}, ' \
               f'Возраст питомца: {self.__age}'