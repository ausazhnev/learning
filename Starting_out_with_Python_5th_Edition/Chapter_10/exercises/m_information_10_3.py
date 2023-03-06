# Класс Information

# Инициализирует класс information и присваивает
# атрибутам переданные значения
class information:
    def __init__(self, name = None, address = None, age = None, phone = None):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    # метод устанавливает значение атрибута: __name
    def set_name(self, name):
        self.__name = name

    # метод устанавливает значение атрибута: __address
    def set_address(self, address):
        self.__address = address

    # метод устанавливает значение атрибута: __age
    def set_age(self, age):
        self.__age = age

    # метод устанавливает значение атрибута: __phone
    def set_phone(self, phone):
        self.__phone = phone

    # Метод возвращает значение атрибута: __name
    def get_name(self):
        return self.__name

    # Метод возвращает значение атрибута: __address
    def get_address(self):
        return self.__address

    # Метод возвращает значение атрибута: __age
    def get_age(self):
        return self.__age

    # Метод возвращает значение атрибута: __phone
    def get_phone(self):
        return self.__phone
