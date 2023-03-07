# Класс Patient
class Patient:
    def __init__(self, name,  address, phone, confidant):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__confidant = confidant

    # Методы-мутаторы
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def set_confidant(self, confidant):
        self.__confidant = confidant

    # Методы-получатели
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_confidant(self):
        return self.__confidant