# Класс Person
class Person:
    def __init__(self, name=None, address=None, phone=None):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone


# Класс Customer
class Customer(Person):
    def __init__(self, name=None, address=None, phone=None, id_num=None, mailing=None):
        super().__init__(name, address, phone)
        self.__id_num = id_num
        self.__mailing = mailing

    def set_id_num(self, id_num):
        self.__id_num = id_num

    def set_mailing(self, mailing):
        self.__mailing = mailing

    def get_id_num(self):
        return self.__id_num

    def get_mailing(self):
        return self.__mailing